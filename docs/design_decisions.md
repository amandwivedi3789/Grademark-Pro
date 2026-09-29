# Design Decisions and Rationale

## Tkinter
Tkinter is used because it is part of the standard Python ecosystem and is suitable for a lightweight desktop GUI.

## JSON
JSON provides simple persistent storage for a small academic record application without requiring a database server.

## Modular structure
The original application contained most functionality in `main.py`. The final submission separates validation, grading, calculation, dashboard statistics, student CRUD, storage, and configuration so each responsibility is easier to maintain and test.

## Validation
Validation is separated from the GUI so invalid input can be handled consistently.

## Limitations
The current application is intended for small-scale academic use and does not provide authentication, multi-user access, database concurrency, or advanced reporting.
