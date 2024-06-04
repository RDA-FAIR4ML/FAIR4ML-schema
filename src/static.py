group_leaders = ['Daniel Garijo', 'Leyla Jael Castro']
team_members = ['Jenifer Tabita Ciuciu-Kiss', 'Dhwani Solanki', 'Dietrich Rebholz-Schuhmann']

context_desciption = "'In this document we propose a simple way for MLModel to self-describe their genetic variant cardinality service for better integration.'"

namespace_descriptions = {
    "rdf": "This is the RDF Schema for the RDF vocabulary terms in the RDF Namespace, defined in RDF 1.1 Concepts.",
    "rdfs": "The RDF Schema vocabulary (RDFS).",
    "owl": "This ontology partially describes the built-in classes and properties that together form the basis of the RDF/XML syntax of OWL 2.",
    "schema": "Schema.org is a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.",
    "codemeta": "Codemeta is a minimal metadata schema for science software and code, in JSON and XML.",
    "fair4ml": "FAIR4ML metadata schema for machine learning models.",
    "cr": "Datasets are the basis of machine learning (ML). However, a lack of standardization in the description and semantics of ML datasets has made it increasingly difficult for researchers and practitioners to explore, understand, and use all but a small fraction of popular datasets."
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