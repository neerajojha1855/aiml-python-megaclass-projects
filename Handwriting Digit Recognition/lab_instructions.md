# Lab: Day 73: Handwriting Digit Recognition

## Objective

Complete a hands-on build that applies handwriting digit recognition and produces an image-classification experiment with augmentation, learning curves, and class-level error analysis.

## Prerequisites

- Review the lecture reading and cheat sheet.
- Be able to explain convolution and feature map.
- Use only local, synthetic, or explicitly authorized data and services.
- Never place passwords, API keys, tokens, or sensitive personal information in code or submissions.

## Estimated time

60–90 minutes

## Tools

Python with TensorFlow/Keras or PyTorch and image utilities.

## Dataset or inputs

A labeled image dataset with train, validation, and test splits.

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
import torch

model = torch.nn.Sequential(
    torch.nn.Conv2d(3, 16, kernel_size=3, padding=1),
    torch.nn.ReLU(),
    torch.nn.MaxPool2d(2),
    torch.nn.Flatten(),
    torch.nn.Linear(16 * 16 * 16, 10),
)
print(model(torch.randn(4, 3, 32, 32)).shape)
```

### Step 4 — Apply the lecture concepts

Demonstrate **Convolution**, **Feature map**, and **Receptive field** explicitly. Add comments or annotations that explain why each choice is present.

### Step 5 — Exercise the workflow

Follow this sequence and record evidence at each stage:

1. Inspect image shape and labels
2. Create reproducible splits
3. Normalize and augment training images
4. Build a small convolutional baseline
5. Track learning curves and confusion matrix
6. Inspect misclassified images

### Step 6 — Test behavior

Run or review the normal, boundary, and failure cases. Compare actual behavior with the expected output. Do not hide a failed case; explain it and make the response safer or clearer.

### Step 7 — Improve one weakness

Select one likely problem—**Applying validation augmentation randomly** or **Using transformations that change the label**—and improve it using **Visualize transformed samples**. Re-run the relevant test and record the difference.

### Step 8 — Package the result

Add a concise summary, usage or review instructions, test evidence, assumptions, and one limitation. Make the artifact understandable without verbal explanation.

## Expected output

an image-classification experiment with augmentation, learning curves, and class-level error analysis, accompanied by normal, boundary, and failure evidence plus a short interpretation.

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
- Adapt the artifact to defect detection.

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
