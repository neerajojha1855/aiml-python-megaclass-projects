# Day 71: Spam Email Detector — Cheat Sheet

## One-line purpose

Use spam email detector to predict categories while choosing thresholds and metrics that reflect the cost of different mistakes.

## Core concepts

| Concept | Practical meaning |
|---|---|
| Class | A discrete outcome category assigned to an observation. |
| Decision boundary | The learned separation between regions associated with different predictions. |
| Probability score | A model’s estimated confidence for a class before a threshold is applied. |
| Precision and recall | Complementary metrics describing positive-prediction quality and positive-case coverage. |
| Confusion matrix | Counts of true and false positives and negatives at a chosen threshold. |

## Reusable pattern

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
```

## Working sequence

1. Define classes and error costs
2. Create a stratified split
3. Build preprocessing
4. Fit a baseline and classifier
5. Evaluate probabilities and thresholds
6. Inspect subgroup errors and calibrate the decision

## Decision guide

- **Use this approach when:** the problem matches supervised machine learning, the input and desired output are explicit, and the result can be tested with representative cases.
- **Start simpler when:** a transparent rule, baseline, or small function can answer the question with less complexity.
- **Pause and clarify when:** the input is unavailable, the target behavior is ambiguous, the data contains sensitive information without authorization, or success cannot be measured.
- **Advance the solution when:** the baseline is reproducible, edge cases are understood, and added complexity produces meaningful evidence.

## Troubleshooting

| Symptom or mistake | Corrective move |
|---|---|
| Using accuracy on imbalanced data | Use stratification |
| Selecting a threshold without costs | Report a confusion matrix |
| Fitting preprocessing before the split | Tune thresholds on validation data |
| Assuming probabilities are calibrated | Inspect precision-recall trade-offs |

## Quality checklist

- The problem and expected output are written before implementation.
- Inputs are validated and representative cases are included.
- Shapes, types, labels, units, or interfaces are inspected explicitly.
- The solution is reproducible from documented commands or steps.
- Normal, boundary, and failure behavior are tested.
- Results are interpreted in practical language.
- Assumptions and limitations are visible.

## Key takeaways

- Use stratification
- Report a confusion matrix
- Tune thresholds on validation data
- Inspect precision-recall trade-offs
- Test stability by subgroup
