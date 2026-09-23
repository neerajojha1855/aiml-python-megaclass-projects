# Lab: Day 71: Spam Email Detector

## Objective

Complete a hands-on build that applies spam email detector and produces a classification model with threshold analysis and an error-cost recommendation.

## Prerequisites

- Review the lecture reading and cheat sheet.
- Be able to explain class and decision boundary.
- Use only local, synthetic, or explicitly authorized data and services.
- Never place passwords, API keys, tokens, or sensitive personal information in code or submissions.

## Estimated time

60–90 minutes

## Tools

Python, pandas, and scikit-learn.

## Dataset or inputs

A labeled dataset with at least two classes and a stated consequence for false positives and false negatives.

Create at least three cases before beginning:

1. A normal case that should succeed.
2. A boundary case at an important limit.
3. An invalid, unavailable, or failure case that should produce a controlled response.

## Step-by-step instructions

### Step 1 — Frame the result

Write the user or audience, the problem, the expected output, and one measurable success criterion. Keep the scope to one coherent outcome.

### Step 2 — Inspect the inputs

Record types, shapes, fields, units, labels, or interface expectations. Identify missing information and state any assumption you make.

### Step 3 — Build the baseline

Create a small working implementation using the reusable pattern below. Keep the first version simple and transparent.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
```

### Step 4 — Apply the lecture concepts

Demonstrate **Class**, **Decision boundary**, and **Probability score** explicitly. Add comments or annotations that explain why each choice is present.

### Step 5 — Exercise the workflow

Follow this sequence and record evidence at each stage:

1. Define classes and error costs
2. Create a stratified split
3. Build preprocessing
4. Fit a baseline and classifier
5. Evaluate probabilities and thresholds
6. Inspect subgroup errors and calibrate the decision

### Step 6 — Test behavior

Run or review the normal, boundary, and failure cases. Compare actual behavior with the expected output. Do not hide a failed case; explain it and make the response safer or clearer.

### Step 7 — Improve one weakness

Select one likely problem—**Using accuracy on imbalanced data** or **Selecting a threshold without costs**—and improve it using **Use stratification**. Re-run the relevant test and record the difference.

### Step 8 — Package the result

Add a concise summary, usage or review instructions, test evidence, assumptions, and one limitation. Make the artifact understandable without verbal explanation.

## Expected output

a classification model with threshold analysis and an error-cost recommendation, accompanied by normal, boundary, and failure evidence plus a short interpretation.

## Success criteria

- The problem, input, output, and success criterion are explicit.
- The artifact demonstrates at least three core lecture concepts.
- The baseline can be reproduced from the supplied instructions.
- Normal, boundary, and failure behavior are visible.
- One weakness is repaired and retested.
- The conclusion distinguishes evidence from assumption.

## Stretch goals

- Add a second implementation and compare it using clarity, correctness, performance, and maintainability.
- Create a small automated test or reusable review checklist.
- Improve the user-facing error or explanation behavior.
- Adapt the artifact to spam filtering.

## Troubleshooting

- **The output is unexpected:** reduce the input to one manually verifiable case and inspect each intermediate value.
- **A library or import fails:** confirm the active environment and record the exact command used to install dependencies.
- **Shapes or types do not align:** print or document them before the failing operation.
- **The result changes between runs:** set a seed where supported and identify uncontrolled inputs.
- **The artifact works only once:** reset state and repeat the workflow from a clean start.

## Submission checklist

- [ ] Problem statement and success criterion
- [ ] Input description and assumptions
- [ ] Completed artifact
- [ ] Normal, boundary, and failure evidence
- [ ] Improvement and retest
- [ ] Run or review instructions
- [ ] Limitation and next step
