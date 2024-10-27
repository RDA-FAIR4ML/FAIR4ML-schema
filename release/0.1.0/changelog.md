# ChangeLog

### 27.10.2024. - Feedback from the community:

#### Changes in fair4ml:MLModel Properties:
- fair4ml:ethicalLegalSocial
    - Split into **fair4ml:legal** and **fair4ml:ethicalSocial**
- **fair4ml:hasEvaluation**
    - New property!
- fair4ml:hasCO2eEmissions
    - Amount of CO2 equivalent emissions produced by **training** the model.
- fair4ml:modelCategory
    - Category of this ML model (e.g., Supervised, Unsupervised, Semi-supervised, Reinforcement), learning architecture (e.g., CNN, **transformer**), underlying algorithm (e.g., logistic regression, random forest, **LLM**).
- fair4ml:modelRisks
    - Renamed to: **fair4ml:modelRisksBiasLimitations**
- **fair4ml:codeSampleSnippet**
    - New property!

## NEW fair4ml:MLModelEvaluation type
#### New fair4ml:MLModelEvaluation Properties
- fair4ml:evaluatedMLModel
- fair4ml:evaluationDataset
- fair4ml:evaluationMetrics
- fair4ml:evaluationResults
- fair4ml:evaluationSoftware
- fair4ml:extrinsicEvaluation
