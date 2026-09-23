# Exercises: Day 71: Spam Email Detector

Complete the exercises in order. They progress from explanation to implementation, debugging, and independent judgment.

## Exercise 1 — Explain the foundation

Define **Class** and **Decision boundary** in your own words. Give one example of how each appears in spam email detector.

**Completion evidence:** two concise definitions and two relevant examples.

## Exercise 2 — Trace the reusable pattern

Read the pattern below without running it. Annotate each line, predict the output or artifact, and identify the input, transformation, output, and validation point.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
```

**Completion evidence:** a line-by-line trace and a predicted result.

## Exercise 3 — Change one requirement

Modify the pattern or conceptual workflow so it handles a second realistic requirement. Examples include an additional category, a missing value, a new user action, a larger input shape, or a different decision threshold. Keep the change small enough to explain clearly.

**Completion evidence:** the revised artifact plus a three-sentence explanation of the change.

## Exercise 4 — Find and repair a failure

Create or describe one failure related to **Using accuracy on imbalanced data**. Show the observable symptom, explain the cause, and repair it using **Use stratification**.

**Completion evidence:** before-and-after behavior and a short root-cause note.

## Exercise 5 — Compare two choices

Compare the baseline approach with one alternative. Use four criteria: clarity, correctness, maintainability, and cost or complexity. Do not select an option only because it is more advanced.

**Completion evidence:** a comparison table and a justified recommendation.

## Exercise 6 — Apply it to a new context

Apply spam email detector to fraud screening. State the user, input, expected output, one risk, and one acceptance test.

**Completion evidence:** a five-part application brief.

## Reflection prompt

Which assumption had the greatest effect on your solution, and what new evidence would cause you to change the design?

## Practical challenge

Produce a classification model with threshold analysis and an error-cost recommendation. Make the result understandable to another learner who did not attend the lecture. Include run instructions or review steps, representative evidence, and one limitation.

## Submission checklist

- [ ] Definitions are written in original language.
- [ ] The pattern is traced before modification.
- [ ] At least one failure is reproduced and repaired.
- [ ] Two approaches are compared using explicit criteria.
- [ ] The final challenge includes evidence and limitations.
