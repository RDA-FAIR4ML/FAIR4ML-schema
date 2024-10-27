import requests
import json
import re
from jinja2 import Environment, FileSystemLoader
from static import codemeta_properties_data
from static import (
    authors,
    release_date,
    version,
    status,
    version_uri,
    latest_version_uri,
    namespaces,
    schema_hierarchy,
    url_mapping
)

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


with open('development/fair4ml.jsonld', 'r') as f:
    data = json.load(f)


def get_item_by_id(graph, item_id):
    """Retrieve an item from the graph by its @id."""
    for item in graph:
        if item.get('@id') == item_id:
            return item
    return None


def get_expected_types_and_urls(item):
    """Retrieve expected types and URLs from schema:rangeIncludes."""
    range_includes = item.get('schema:rangeIncludes', [])
    if not isinstance(range_includes, list):
        range_includes = [range_includes]

    expected_types = []
    expected_types_url = []

    for rtype in range_includes:
        if isinstance(rtype, dict):
            type_id = rtype.get('@id', '')
            expected_types.append(type_id)

            # Determine URL based on prefix
            if type_id.startswith('schema:'):
                url = 'http://schema.org/' + type_id.split(':')[-1]
            elif type_id.startswith('fair4ml:'):
                url = 'https://w3id.org/fair4ml#' + type_id.split(':')[-1]
            elif type_id.startswith('cr:'):
                url = 'http://mlcommons.org/croissant/1.0'
            else:
                url = ''  # Default to empty if prefix is unrecognized

            expected_types_url.append(url)

    return expected_types, expected_types_url



def get_description(item, schemaorg_data, codemeta_data):
    """Retrieve the description based on the item ID prefix (schema or codemeta)."""
    item_id = item.get('@id', '')
    if 'schema:' in item_id:
        return next((x['rdfs:comment'] for x in schemaorg_data['@graph'] if x['@id'] == item_id), '')
    elif 'codemeta:' in item_id:
        return next((x['rdfs:comment'] for x in codemeta_data['@context'] if x['@id'] == item_id), '')
    return item.get('rdfs:comment', '')


def linkify_description(description):
    """Convert terms like [[CreativeWork]] to linked <a> tags with the appropriate URL."""
    def replace_match(match):
        term = match.group(1)
        # Define known terms and their URLs
        url = url_mapping.get(term, "")
        if url:
            return f'<a href="{url}" target="_blank">{term}</a>'
        return term  # Return the term as-is if no URL mapping is found

    # Replace all instances of [[Term]] with linked versions
    return re.sub(r'\[\[(.*?)\]\]', replace_match, description)


def format_property(item, schemaorg_data, codemeta_data):
    """Format a property into a dictionary with its name, URL, expected types, and description."""
    property_name = item.get('@id', '')
    if property_name.split(':')[-1][0].isupper():  # Skip if property name starts with an uppercase letter
        return

    # Determine property URL based on the namespace prefix
    if 'schema:' in property_name:
        property_url = 'http://schema.org/' + property_name.split(':')[-1]
    elif 'cr:' in property_name:
        property_url = 'http://mlcommons.org/croissant/1.0'
    elif 'fair4ml:' in property_name:
        property_url = 'https://w3id.org/fair4ml#' + property_name.split(':')[-1]
    else:
        property_url = ''  # Default empty if no recognized prefix

    description = get_description(item, schemaorg_data, codemeta_data)
    description = linkify_description(description)
    expected_types, expected_types_url = get_expected_types_and_urls(item)
    return {
        'property': property_name,
        'property_url': property_url,
        'expected_type_and_urls': list(zip(expected_types, expected_types_url)),
        'description': description
    }

# Extract FAIR4ML - MLModel and MLModelEvaluation properties
fair4ml_mlmodel_properties = []
fair4ml_mlmodelevaluation_properties = []

for item in data.get('@graph', []):
    # Check if the property belongs to MLModel or MLModelEvaluation based on schema:domainIncludes
    domain = item.get('schema:domainIncludes', {}).get('@id', '')

    # Process MLModel properties
    if domain == "fair4ml:MLModel":
        formatted_property = format_property(item, schemaorg_data, codemeta_data)
        if formatted_property:
            fair4ml_mlmodel_properties.append(formatted_property)

    # Process MLModelEvaluation properties
    elif domain == "fair4ml:MLModelEvaluation":
        formatted_property = format_property(item, schemaorg_data, codemeta_data)
        if formatted_property:
            fair4ml_mlmodelevaluation_properties.append(formatted_property)

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
                    'description': linkify_description(codemeta_property_info["desc"])
                }
                codemeta_properties.append(property_json)

context = {
    'description': context_desciption,
    'fair4ml_mlmodel_properties': fair4ml_mlmodel_properties,
    'fair4ml_mlmodelevaluation_properties': fair4ml_mlmodelevaluation_properties,
    'schema_hierarchy': schema_hierarchy,
    'schema_properties': schema_properties,
    'codemeta_properties': codemeta_properties,
    'namespaces': namespaces,
    'authors': authors,
    'release_date': release_date,
    'version': version,
    'status': status,
    'version_uri': version_uri,
    'latest_version_uri': latest_version_uri,
}

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('src/template.html')

html_output = template.render(context)

# Save index.html
with open('development/index.html', 'w') as f:
    f.write(html_output)

#print("HTML file has been generated successfully.")