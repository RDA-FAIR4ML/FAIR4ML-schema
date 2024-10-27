release_date = "2024.11.04"
version = "0.1.0"
status = "Draft (under review)"
version_uri = "https://w3id.org/fair4ml/0.0.1"
latest_version_uri = "https://w3id.org/fair4ml#"
authors = [
    {"name": "Leyla-Jael Castro", "affiliation": "ZB MED", "affiliation_url": "https://www.zbmed.de/en/"},
    {"name": "Daniel Garijo", "affiliation": "Universidad Politécnica de Madrid", "affiliation_url": "https://www.upm.es/"},
    {"name": "Dietrich Rebholz-Schuhmann", "affiliation": "ZB MED", "affiliation_url": "https://www.zbmed.de/en/"},
    {"name": "Dhwani Solanki", "affiliation": "ZB MED", "affiliation_url": "https://www.zbmed.de/en/"},
    {"name": "Jenifer Tabita Ciuciu-Kiss", "affiliation": "Universidad Politécnica de Madrid", "affiliation_url": "https://www.upm.es/"},
    {"name": "", "affiliation": "Research Data Alliance FAIR4ML Task Force", "affiliation_url": "https://www.rd-alliance.org/groups/fair-machine-learning-fair4ml-ig/members/all-members/"}
]

context_desciption = "'In this document we propose a simple way for MLModel to self-describe their genetic variant cardinality service for better integration.'"

namespaces = [
    {"prefix": "rdf", "url": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"},
    {"prefix": "rdfs", "url": "http://www.w3.org/2000/01/rdf-schema#"},
    {"prefix": "owl", "url": "http://www.w3.org/2002/07/owl#"},
    {"prefix": "schema", "url": "http://schema.org/"},
    {"prefix": "codemeta", "url": "https://w3id.org/codemeta/"},
    {"prefix": "fair4ml", "url": "https://w3id.org/fair4ml/"},
    {"prefix": "cr", "url": "http://mlcommons.org/croissant/1.0"}
]

schema_hierarchy = [
    {"name": "schema:Thing", "url": "http://schema.org/Thing"},
    {"name": "schema:CreativeWork", "url": "http://schema.org/CreativeWork"},
    {"name": "fair4ml:MLModel", "url": "https://github.com/RDA-FAIR4ML/FAIR4ML-schema"}
]

url_mapping = {
    "CreativeWork": "http://schema.org/CreativeWork",
    "MediaReview": "http://schema.org/MediaReview",
    "MediaReviewItem": "http://schema.org/MediaReviewItem",
    "Person": "http://schema.org/Person",
    "Organization": "http://schema.org/Organization",
    "ArchiveComponent": "http://schema.org/ArchiveComponent",
    "ArchiveOrganization": "http://schema.org/ArchiveOrganization",
    "Certification": "http://schema.org/Certification",
    "Grant": "http://schema.org/Grant",
    "ownershipFundingInfo": "http://schema.org/ownershipFundingInfo",
    "Thing": "http://schema.org/Thing",
    "availableLanguage": "http://schema.org/availableLanguage",
    "isBasedOn": "http://schema.org/isBasedOn",
    "Dataset": "http://schema.org/Dataset",
    "SoftwareApplication": "http://schema.org/SoftwareApplication",
    "Project": "http://schema.org/Project",
    "TextObject": "http://schema.org/TextObject",
    "ScholarlyArticle": "http://schema.org/ScholarlyArticle"
    # Add additional mappings as needed
}

codemeta_properties_data = {
    "buildInstructions": {
        "type": "schema:URL",
        "desc": "Link to installation instructions/documentation."
    },
    "developmentStatus": {
        "type": "schema:Text",
        "desc": "Description of development status, e.g. Active, inactive, suspended. See repostatus.org ."
    },
    "issueTracker": {
        "type": "schema:URL",
        "desc": "Link to software bug reporting or issue tracking system."
    },
    "readme": {
        "type": "schema:URL",
        "desc": "Link to software Readme file."
    },
    "referencePublication": {
        "type": "schema:ScholarlyArticle",
        "desc": "An academic publication related to the software."
    }
}