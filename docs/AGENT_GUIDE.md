# Agent Guide — Python OOPs Project

This document is the single source of truth for any agent working in this repository.
Read it before creating or editing code, tests, or notebooks.

---

## CRITICAL — Read This First

This is a personal learning repository based on
[`python-3-deep-dive-part-4`](https://www.udemy.com/course/python-3-deep-dive-part-4/).
The main purpose is to practice and retain object-oriented programming concepts, not to build production software.

Because this is a study repo:

- Preserve beginner-friendly clarity over clever shortcuts.
- Keep examples explicit and readable.
- Focus on repeatable learning, not polished deliverables.
- Avoid assumptions about hidden project patterns.

---

## 1. What the agent is allowed to do

- Create or update files in the appropriate section folders.
- Add or refine docstrings and inline comments that explain intent.
- Refactor for readability when a change clearly improves understanding.
- Add tests for behavior you changed.
- Fix syntax/import/runtime errors when explicitly asked.
- Add small, dependency-light scripts for experiments in relevant folders.

---

## 2. What the agent must NEVER do

- Do not remove instructional or explanatory comments/notes from lessons unless requested.
- Do not rename existing modules/classes in a way that breaks current imports.
- Do not introduce broad architectural changes unless the user explicitly requests them.
- Do not add unnecessary dependencies; keep the repo lightweight.
- Do not claim correctness without clear tests or a short manual demonstration.

---

## 3. Repo Layout

```
root/
├── ClassesSection/          # Class basics and practice snippets
├── Design_patterns/         # OOP design pattern exercises
├── InheritanceSection/      # Inheritance-focused projects and notes
├── PolymorphismSection/     # Polymorphism-focused projects and notes
├── older_stuff/             # Archived historical work; do not use for new files
├── tests/                   # Pytest tests (where they exist)
├── docs/                   # Learning docs and agent guidance
├── requirements.txt         # Keep existing minimal dependency list
├── TO_DO.list               # Current priorities/tasks
└── README.md
```

---

## 4. Naming and Structure Conventions

- Prefer descriptive, readable identifiers.
- Class names: `PascalCase`.
- Method names: `snake_case` unless inheriting a known external API.
- Folder names: keep existing convention; avoid creating new top-level folders unless asked.
- For new notebooks/scripts:
  - Use clear names like `section_topic_exploration.py` or `Project_X_Name.ipynb`.
  - Keep code runnable and self-documenting.
- Maintain a direct relationship between implementation and tests.

---

## 5. Python File Template (practice code)

```python
"""Notes:
Brief learning notes for this file.

Key idea:
- Point 1
- Point 2
"""


class Example:
    def __init__(self, value=None):
        self.value = value

    def describe(self):
        return f"value={self.value!r}"
```

Rules:

- Keep `__main__` blocks minimal.
- Prefer explicit type hints when it improves clarity.
- Keep behavior easy to trace.

---

## 6. Test Conventions

Use `pytest` with simple and direct tests.

```python
"""Tests for Example."""
from section_name.module_name import Example


class TestExample:
    def test_describe_returns_value(self):
        obj = Example(5)
        assert obj.describe() == "value=5"
```

Rules:

- Tests should be deterministic and readable.
- Prefer clear input/output naming (`actual`, `expected`) for multi-step checks.
- Keep tests scoped to one behavior per test.

---

## 7. Imports and Dependencies

- Import from stdlib first, then local modules.
- Avoid external libraries unless they already exist in `requirements.txt` or are explicitly approved.
- If you add a new dependency, add it only in `requirements.txt` with a short reason.

---

## 8. Practical Editing Rules for Agents

- Do not create/delete large swathes of files without checking folder purpose.
- Do not alter tests to force passing behavior.
- Do not replace learning artifacts with shortened "productionized" versions.
- If two implementations are possible, keep the more explicit one.
- When uncertain, add small TODO-style comments only when the next step is clear.

---

## 9. Workflow Check Before Finalizing

For any change:

1. Confirm it aligns with the target course topic.
2. Ensure the new/edited code is understandable by someone reading after a long break.
3. Confirm no unrelated behavior was changed.
4. Verify imports and references still resolve.
5. Keep the file’s educational value high.

---

## 10. Git and Maintenance Notes

- Track focused changes tied to TO_DO and user-requested work.
- Keep `.pytest_cache` and other generated folders out of new commits.
- Avoid touching unrelated files unless required by the current change.
- Do not reorder or rewrite old completed sections unless explicitly asked.

---

This guide is meant to help learning flow. If a request is unclear, ask one clarifying question before making structural changes.

