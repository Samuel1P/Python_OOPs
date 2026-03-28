# Course Index — Python Deep Dive Part 4

This index documents the Part 4 content from the course repository
[`python-deepdive/Part 4`](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204) and is meant to be a practical map for your local study flow.

## Big picture

Part 4 is the “OOP and advanced Python mechanics” band of the course. It progresses from class fundamentals to practical inheritance and polymorphism, then shifts into
real-world design topics (descriptors, metaprogramming, exceptions, enums), and periodically inserts projects to force integration.

## Course section map

### [Section 02 — Classes](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2002%20-%20Classes)
- Core object-oriented foundations in Python
- Class definitions, instances, attributes, and methods
- The transition from script-style code to behavior-focused class modeling
- First-pass use of `__init__`, state, and simple method design

### [Section 03 — Project 1](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2003%20-%20Project%201)
- First applied mini-project in this section
- Reinforces class composition, object lifecycle, and method implementation in context
- Good checkpoint for “does this class model behave as expected in use”

### [Section 04 — Polymorphism and Special Methods](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2004%20-%20Polymorphism%20and%20Special%20Methods)
- Core polymorphism concepts in Python
- Operator/custom behavior customization through dunder methods (`__str__`, `__repr__`, etc.)
- Design for interface consistency between different classes

### [Section 05 — Project 2](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2005%20-%20Project%202)
- Second applied project
- Usually applies learned OOP + special methods in a more realistic structure
- Good point to compare class-level ideas to reusable patterns

### [Section 06 — Single Inheritance](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2006%20-%20Single%20Inheritance)
- Focused topic on deriving behavior from parent class
- Super/child initialization and method reuse
- Shared base behavior vs specialized subclass behavior

### [Section 07 — Project 3](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2007%20-%20Project%203)
- Your current local implementation target
- In-memory inventory modeling project (Resource/CPU/HDD/SSD)
- Validates inheritance, property usage, and state-safe methods (`claim`, `freeup`, `died`, `purchased`)
- Local mapping:
  - `InheritanceSection/Project_Inheritance`

### [Section 08 — Descriptors](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2008%20-%20Descriptors)
- Python descriptor protocol (`__get__`, `__set__`, `__set_name__`)
- Why descriptors are the shared mechanism behind properties and attribute control
- Practical use in reusable validation and controlled attribute behavior

### [Section 09 — Project 4](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2009%20-%20Project%204)
- Another consolidation project before enumerations and exceptions
- Usually blends descriptors and advanced object behavior patterns

### [Section 10 — Enumerations](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2010%20-%20Enumerations)
- Enum classes for constrained, readable constants
- Better-than-magical-number/domain-value modeling
- Cleaner branching and status/role/type handling

### [Section 11 — Project 5](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2011%20-%20Project%205)
- Further project-based integration
- Reinforces composition/inheritance/enums together in small app-style shape

### [Section 12 — Exceptions](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2012%20-%20Exceptions)
- Error design and handling strategy
- Custom error types and meaningful failure messaging
- Writing resilient, user-friendly domain code

### [Section 13 — Project 6](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2013%20-%20Project%206)
- Larger capstone project inside Part 4
- Brings all practical patterns together at the end of this segment

### [Section 14 — Metaprogramming](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2014%20-%20Metaprogramming)
- Dynamic behavior and class/attribute manipulation techniques
- Advanced-level patterns that power reusable frameworks
- Great place to connect descriptor knowledge to runtime behavior control

### [Section 15 — Python Updates](https://github.com/fbaptiste/python-deepdive/tree/main/Part%204/Section%2015%20-%20Python%20Updates)
- Notes on modern features and syntax changes
- Useful for keeping older projects compatible with newer Python versions

## Recommended local study flow

1. Finish with confidence on Project 3 concepts (inventory model) so inheritance and state validation are fresh.
2. Jump into Section 08 descriptors, but keep one objective lens:
   - What problem does this section solve that plain `@property` does not?
3. Immediately apply each concept by adding or refactoring small examples in `section_workspace`-style folders (you can keep the folder strategy you already started with).
4. Before each project section (9/11/13), do a 15-minute “API sketch” from README/problem statement to class design before coding.

## How to use this index

- Treat this as a map, not just a checklist.
- For each section, read requirements first, map expected classes/functions, then code.
- If uncertain, pause and compare with the course implementation in the matching section above.
- Keep notes in your local solution notes so the next revisit is fast.

