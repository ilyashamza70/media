# Source Code Directory

This directory contains all the source code for the Grade Calculator application.

## Files

### grade_calculator.py
The main application file containing the `GradeCalculator` class and all its functionality:
- Interactive UI with Rich library
- Manual grade input
- File import (TXT, CSV, Excel)
- Statistics calculation
- Visualization generation
- Result export
- History tracking

Run directly: `python grade_calculator.py`

### degree_courses.py
Database of degree courses with their subjects and credits.
Supports both Bachelor's (Triennale) and Master's (Magistrale) degrees.

Functions:
- `get_all_courses()` - Get all available courses
- `get_course_info(course_name)` - Get info for specific course
- `list_courses_by_type(degree_type)` - List courses by type

### trial.py
Legacy version of the grade calculator for reference.
This is the original implementation before the major refactoring.

## Usage

The recommended way to run the application is through the main entry point:

```bash
# From project root
python main.py

# Or directly
python src/grade_calculator.py
```

## Adding New Courses

To add a new degree course, edit `degree_courses.py`:

```python
TRIENNALE_COURSES["New Course"] = {
    "type": "triennale",
    "total_credits": 180,
    "courses": {
        "Subject 1": 12,
        "Subject 2": 9,
        # ... more subjects
        "Final Thesis": 6
    }
}
```
