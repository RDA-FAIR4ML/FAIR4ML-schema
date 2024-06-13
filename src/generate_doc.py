import requests
import json
from jinja2 import Environment, FileSystemLoader
from static import namespace_descriptions, codemeta_properties_data
from static import group_leaders, team_members
from static import context_desciption

# Get schema.orh jsonld
schemaorg_url = "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/26.0/schemaorg-all-http.jsonld"
schemaorg_response = requests.get(schemaorg_url)

# Get codemeta jsonld
headers = {
    "Accept": "application/ld+json"
}
codemeta_url = "https://w3id.org/codemeta"
#codemeta_url = "https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld"
codemeta_response = requests.get(codemeta_url, headers=headers)


if schemaorg_response.status_code == 200 and codemeta_response.status_code == 200:
    schemaorg_data = schemaorg_response.json()
    codemeta_data = codemeta_response.json()


with open('development/context.jsonld', 'r') as f:
    data = json.load(f)


def get_item_by_id(graph, item_id):
    """Retrieve an item from the graph by its @id."""
    for item in graph:
        if item.get('@id') == item_id:
            return item
    return None


def get_expected_types_and_urls(item):
    range_includes = item.get('schema:rangeIncludes', [])
    if not isinstance(range_includes, list):
        range_includes = [range_includes]
    expected_types = [rtype.get('@id', '') for rtype in range_includes if isinstance(rtype, dict)]
    expected_types_url = []
    for type in expected_types:
        if 'schema' in type:
            expected_types_url.append('http://schema.org/' + type.split(':')[-1])
        else:
            expected_types_url.append('')
    return expected_types, expected_types_url


def get_description(item, schemaorg_data, codemeta_data):
    if 'schema:' in item.get('@id', ''):
        return next((x['rdfs:comment'] for x in schemaorg_data['@graph'] if x['@id'] == item.get('@id', '')), '')
    elif 'codemeta:' in item.get('@id', ''):
        return next((x['rdfs:comment'] for x in codemeta_data['@context'] if x['@id'] == item.get('@id', '')), '')
    return item.get('rdfs:comment', '')


def format_property(item, schemaorg_data, codemeta_data):
    property_name = item.get('@id', '')
    if property_name.split(':')[-1].isupper():
        return
    property_url = ''
    if 'schema:' in item.get('@id', ''):
        property_url = 'http://schema.org/' + property_name.split(':')[-1]
    
    description = get_description(item, schemaorg_data, codemeta_data)

    expected_types, expected_types_url = get_expected_types_and_urls(item)
    return {
        'property': property_name,
        'property_url': property_url,
        'expected_type_and_urls': list(zip(expected_types, expected_types_url)),
        'description': description
    }

# Extract FAIR4ML properties
fair4ml_properties = [format_property(item, schemaorg_data, codemeta_data) for item in data.get('@graph', []) if item.get('@id', '').startswith('fair4ml:')]

# Extract  schema.org profiles
schema_profiles = []
for key, value in data['@context'].items():
    if type({}) == type(value):
        item_id = value.get('@id')
        item = get_item_by_id(schemaorg_data['@graph'], item_id)
    else:
        continue
    if item_id.split(':')[-1][0].isupper():
        expected_types, expected_types_url = get_expected_types_and_urls(item)
        profile = {
            'profile': item_id,
            'profile_url': 'http://schema.org/' + item_id.split(':')[-1],
            'description': item.get('rdfs:comment', '')
        }
        schema_profiles.append(profile)

# Extract schema.org and codemeta properties
schema_properties = []
codemeta_properties = []
for property, val in data['@context'].items():
    if not isinstance(val, str):
        property_name = val['@id'].split(':')[-1]
        if property_name[0].islower():
            if 'schema' in val['@id'].split(':')[0]:
                item = get_item_by_id(schemaorg_data['@graph'], val['@id'])
                schema_properties.append(format_property(item, schemaorg_data, codemeta_data))
            else:
                codemeta_property_info = codemeta_properties_data[property_name]
                property_json = {
                    'property': property_name,
                    'property_url': "https://w3id.org/codemeta/"+property_name,
                    'expected_type_and_urls': list(zip([codemeta_property_info['type']], "http://schema.org/"+codemeta_property_info['type'])),
                    'description': codemeta_property_info["desc"]
                }
                codemeta_properties.append(property_json)

# Extract namespaces
namespaces = []
for prefix, url in data.get('@context', {}).items():
    if isinstance(url, str):
        namespaces.append({'prefix': prefix, 'url': url, "description": namespace_descriptions[prefix]})

context = {
    'description': context_desciption,
    'fair4ml_properties': fair4ml_properties,
    'schema_properties': schema_properties,
    'codemeta_properties': codemeta_properties,
    'schema_profiles': schema_profiles,
    'namespaces': namespaces,
    'group_leaders': group_leaders,
    'team_members': team_members
}

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('src/template.html')

html_output = template.render(context)

# Save index.html
with open('index.html', 'w') as f:
    f.write(html_output)

#print("HTML file has been generated successfully.")