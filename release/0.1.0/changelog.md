# ChangeLog

### 27.10.2024. - Feedback from the community:

#### Changes in fair4ml:MLModel Properties:
- fair4ml:ethicalLegalSocial
    - Split into **fair4ml:legal** and **fair4ml:ethicalSocial**
- **fair4ml:hasEvaluation**
    - New property! used to link an MLModel with its corresponding MLModelEvaluation
- fair4ml:hasCO2eEmissions
    - Edit in the definition: Amount of CO2 equivalent emissions produced by **training** the model.
- fair4ml:modelCategory
    - Edit in the definition: Category of this ML model (e.g., Supervised, Unsupervised, Semi-supervised, Reinforcement), learning architecture (e.g., CNN, **transformer**), underlying algorithm (e.g., logistic regression, random forest, **LLM**).
- fair4ml:modelRisks
    - Renamed to: **fair4ml:modelRisksBiasLimitations**
- **fair4ml:codeSampleSnippet**
    - New property! Designed to show illustrate how to use a model in code. 

## NEW type: fair4ml:MLModelEvaluation
A MLModelEvaluation is an object that bundles the context of a model evaluation: dataset, metrics used, results obtained, software used, etc. A model may have more than one evaluation.

#### New fair4ml:MLModelEvaluation Properties
- fair4ml:evaluatedMLModel: MLModel evaluated with this evaluation. Reverse property: fair4ml:hasEvaluation
- fair4ml:evaluationDataset: Dataset used for the evaluation
- fair4ml:evaluationMetrics: Description of the metrics used for evaluating the ML model. 
- fair4ml:evaluationResults: Summary of the results from the evaluation
- fair4ml:evaluationSoftware: Code used to performed the evaluation
- fair4ml:extrinsicEvaluation: Indicates whether this evaluation is extrinsic, i.e., done with an existing model, outside the model training scope, and with a totally unseen dataset. It could be done by third-parties or by the authors of the model.
