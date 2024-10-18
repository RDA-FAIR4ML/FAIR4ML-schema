# ChangeLog

### 18.10.2024. - Feedback from the community:

#### Propoerty:
- fair4ml:ethicalLegalSocial
    - Lars: May devlop some issues with interoperability as it gives high variation
    - Lars: migth want to split legal from social and ethical inorder to make the legal frameworks more searchable 
    - Gnana: Agree with splitting Responsible AI considerations
    - LJ: Based on what we have observed in Hugging Face models, there is no way to split it unless we use some NER. This info also comes from the same Model Card section as fair4ml:modelRisks

    - Change:
        - Nothing for now as Huggung Face doesn't sport it

- fair4ml:evaluatedOn
    - Dan Katz: in addition to the dataset used for the evaluation, should there also be more that makes the evaluation reproducible? e.g. how was the evaluation done? What should the result be compared to in order to know that it's correct?
    - Gnana: Should the propertiesof the dataset be summarized or dataset shared? 

    - Change:
        - TBD
    

- fair4ml:hasCO2eEmissions:
    - Dan Katz: Is this emissions produced by training the model, or by using it?

    - Change:
        - Amount of CO2 equivalent emissions produced by the model **training**. The unit should be included in the field (e.g., 10 tonnes).

- fair4ml:modelCategory
    - Dan Katz: Do LLMs also fit here?

    - Change:
        Category of this ML model (e.g., Supervised, Unsupervised, Semi-supervised, Reinforcement), learning architecture (e.g., CNN, **LLM**), underlying algorithm (e.g., logistic regression, random forest).

- fair4ml:modelRisks
    - LJ: some overlap with fair4ml:legalEthicalSocial. Suggestion: keep this one but rename modelRisksBiasLimitations or add the limitations to the description.

    - Change:
        - Renamed to: fair4ml:modelRisksBiasLimitations

- fair4ml:usageInstructions
    - Dan Katz: should this be automatable / machine actionable? Or is it just a list of instructions that a person has to do
    - Lars: good point Dan, maybe we should split usageInstructions in humanUsageInstructutions and machineUsageInstructions.
    - We could add runExample for the code snippet that would be somehow machine actionable.

    - Change:
        - TBD