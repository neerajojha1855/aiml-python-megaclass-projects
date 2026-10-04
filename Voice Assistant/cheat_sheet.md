# Day 74: Voice Assistant — Cheat Sheet

## One-line purpose

Use voice assistant to design and build Voice Assistant as a small, reliable user-facing Python project.

## Core concepts

| Concept | Practical meaning |
|---|---|
| Tokenization | Breaking text into units that a model or rule system can process. |
| Representation | A numeric or symbolic encoding of text used for comparison or prediction. |
| Intent | The user goal a language application attempts to recognize or fulfill. |
| Context | Prior text or domain information needed to interpret the current input. |
| Evaluation set | Representative examples used to test useful, ambiguous, and failure behavior. |

## Reusable pattern

```python
def normalize_text(text):
    return " ".join(text.lower().strip().split())

positive_words = {"helpful", "clear", "excellent"}

def simple_sentiment(text):
    tokens = set(normalize_text(text).split())
    return "positive" if tokens & positive_words else "review"
```

## Working sequence

1. Define the user task and boundaries
2. Collect representative text
3. Normalize without erasing meaning
4. Build a rule or model baseline
5. Evaluate useful and adversarial cases
6. Add fallback, feedback, and human escalation

## Decision guide

- **Use this approach when:** the problem matches natural language processing, the input and desired output are explicit, and the result can be tested with representative cases.
- **Start simpler when:** a transparent rule, baseline, or small function can answer the question with less complexity.
- **Pause and clarify when:** the input is unavailable, the target behavior is ambiguous, the data contains sensitive information without authorization, or success cannot be measured.
- **Advance the solution when:** the baseline is reproducible, edge cases are understood, and added complexity produces meaningful evidence.

## Troubleshooting

| Symptom or mistake | Corrective move |
|---|---|
| Over-cleaning text | Preserve raw and normalized text separately |
| Testing only obvious examples | Use a diverse evaluation set |
| Returning confident output for unknown intent | Expose uncertainty |
| Logging sensitive conversations | Provide safe fallback |

## Quality checklist

- The problem and expected output are written before implementation.
- Inputs are validated and representative cases are included.
- Shapes, types, labels, units, or interfaces are inspected explicitly.
- The solution is reproducible from documented commands or steps.
- Normal, boundary, and failure behavior are tested.
- Results are interpreted in practical language.
- Assumptions and limitations are visible.

## Key takeaways

- Preserve raw and normalized text separately
- Use a diverse evaluation set
- Expose uncertainty
- Provide safe fallback
- Protect user data
