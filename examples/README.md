# Examples Directory

This directory contains example files for importing grades and demo outputs.

## Files

### example_grades.txt
Example file in TXT format for importing grades.

Format:
```
# Format: Course Name = Grade
Mathematical Analysis I = 28
Computer Programming = 30L
Data Structures = 27
```

### example_grades.csv
Example file in CSV format for importing grades.

Format:
```csv
Corso,Voto
Mathematical Analysis I,28
Computer Programming,30L
Data Structures,27
```

### DEMO_OUTPUT.txt
Example output from a demo run of the application showing the expected results.

## Usage

To import grades from these examples:

```bash
# Run the application
python main.py

# Select your degree type and course
# Choose option 2: Import from file
# Enter the path: examples/example_grades.txt
```

## Creating Your Own Import Files

You can create your own import files based on these examples:

1. **TXT format**: Use `=` to separate course name and grade
2. **CSV format**: Two columns (Corso, Voto)
3. **Excel format**: Same as CSV but in .xlsx format

For grades, use:
- Numbers from 18 to 30 for regular grades
- "30L" for 30 e Lode (cum laude)
