# System Architecture

The application follows a simple modular architecture:

User → Tkinter GUI (`main.py`) → Application Modules → Data Manager → `students.json`

Supporting modules:
- `student_manager.py`: CRUD logic
- `calculator.py`: calculator workflow
- `dashboard.py`: class statistics
- `grade_utils.py`: grade rules
- `validation.py`: input validation
- `config.py`: configuration
