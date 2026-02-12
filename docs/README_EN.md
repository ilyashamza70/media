# 🎓 Advanced Grade Calculator & Graduation Score Predictor

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive grade calculator and graduation score simulator with interactive interface, support for multiple degree programs (Bachelor's and Master's), and file import capabilities designed for the Italian university system.

## ✨ Key Features

- 🎯 **Full Support**: Bachelor's (180 ECTS) and Master's (120 ECTS) degree programs
- 📊 **Advanced Calculations**: Weighted average, arithmetic average, predicted graduation grade
- 📈 **Detailed Statistics**: Min, max, median, standard deviation, grade analysis
- 🎨 **Beautiful Interface**: Colorful and interactive CLI with Rich library
- 📁 **Multi-format Import**: Support for TXT, CSV, Excel (XLSX)
- 📉 **Professional Charts**: Detailed visualizations with matplotlib
- 💾 **Data Persistence**: Automatic saving of simulation history
- 🔄 **Result Export**: Export to JSON and CSV formats

## 🚀 Quick Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/ilyashamza70/media.git
cd media

# Install dependencies
pip install -r requirements.txt
```

## 📖 Usage Guide

### Starting the Program

```bash
python grade_calculator.py
```

### Input Methods

#### 1. **Manual Entry**
Enter grades directly through interactive prompts:
```
Select degree type → Select specific program → Enter grades one by one
```

#### 2. **Import from TXT File**
Create a `grades.txt` file:
```text
# Format: Course Name = Grade
Mathematical Analysis I = 28
Computer Programming = 30L
Data Structures = 27
```

#### 3. **Import from CSV**
Create a `grades.csv` file:
```csv
Course,Grade
Mathematical Analysis I,28
Computer Programming,30L
Data Structures,27
```

#### 4. **Import from Excel**
Create an Excel file with two columns: `Course` and `Grade`

### Available Degree Programs

#### Bachelor's (180 ECTS)
- **Computer Engineering**: Complete computer engineering curriculum
- **Information Technology**: IT with focus on development and networks
- **Mathematics**: Pure and applied mathematics

#### Master's (120 ECTS)
- **Embedded Systems**: Embedded systems and IoT
- **Computer Science**: Advanced CS with AI/ML
- **Data Science**: Data science and analytics

## 📊 Calculations

### 1. Weighted Average
```
Weighted_Average = Σ(Grade × Credits) / Σ(Credits)
```

### 2. Arithmetic Average
```
Arithmetic_Average = Σ(Grades) / Number_of_Courses
```

### 3. Graduation Grade (Italian System)
```
Base_Grade = (Weighted_Average / 30) × 110
Honors_Bonus = min(Number_of_Honors × 0.5, 5)
Final_Grade = min(Base_Grade + Honors_Bonus, 110)
```

**Note**: In the Italian system:
- Grades range from 18 to 30
- 30L = 30 with honors (cum laude)
- Final graduation grade is out of 110
- 110L = 110 with honors (highest)

## 📈 Visualizations

The program generates professional charts including:

1. **Average Comparison**: Weighted vs arithmetic average
2. **Graduation Grade**: Predicted final grade with color coding
3. **Grade Distribution**: Histogram of grade distribution
4. **Top Grades by Course**: Bar chart of best grades

## 💾 Generated Files

### During Execution
- `sample_grades.txt/csv/xlsx`: Sample files for import
- `grade_analysis_YYYYMMDD_HHMMSS.png`: Analysis charts
- `results_YYYYMMDD_HHMMSS.json`: Detailed results in JSON
- `grades_YYYYMMDD_HHMMSS.csv`: Exported grade table
- `simulation_log.json`: History of all simulations

## 🎯 Usage Examples

### Example 1: Quick Calculation
```bash
python grade_calculator.py
# Select: 1 (Bachelor's)
# Select: 1 (Computer Engineering)
# Select: 1 (Manual entry)
# Enter grades when prompted
```

### Example 2: Import from File
```bash
python grade_calculator.py
# Select: 2 (Master's)
# Select: 1 (Embedded Systems)
# Select: 2 (Import from file)
# Enter: grades.txt
```

### Example 3: Create Sample Files
```bash
python grade_calculator.py
# Select degree type
# Select specific program
# Select: 3 (Create sample files)
# Edit generated files and re-run with option 2
```

## 🔧 Project Structure

```
media/
├── grade_calculator.py      # Main program
├── degree_courses.py        # Degree programs database
├── trial.py                 # Original version (legacy)
├── requirements.txt         # Python dependencies
├── README.md               # Italian documentation
├── README_EN.md            # This file
├── DOCUMENTAZIONE_IT.md    # Complete Italian guide
├── USER_GUIDE.md           # Quick user guide
├── example_grades.txt      # Example TXT file
├── example_grades.csv      # Example CSV file
└── simulation_log.json     # Simulation history
```

## 🎨 Customization

### Adding New Degree Programs

Edit `degree_courses.py`:

```python
MAGISTRALE_COURSES["New Program"] = {
    "type": "magistrale",
    "total_credits": 120,
    "courses": {
        "Course 1": 12,
        "Course 2": 9,
        # ... other courses
        "Final project work": 30
    }
}
```

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Issue: File not found during import
- Verify the file is in the same directory as the program
- Use absolute paths: `/path/to/file.txt`
- Check file encoding (UTF-8 recommended)

### Issue: Charts not displayed
```bash
# On Linux, you may need a backend
sudo apt-get install python3-tk
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Changelog

### Version 2.0.0 (Current)
- ✨ Completely redesigned interface with Rich
- 🎓 Support for Bachelor's and Master's programs
- 📁 Multi-format import (TXT, CSV, Excel)
- 📊 Advanced statistics
- 🎨 Improved professional charts
- 💾 Logging and export system
- 🌍 Multiple pre-configured degree programs

### Version 1.0.0 (Legacy)
- Basic calculator for Embedded Systems
- Sequential manual input
- Simple charts

## 📄 License

This project is released under the MIT License. See the `LICENSE` file for details.

## 👨‍💻 Author

**Ilyas Hamza**
- GitHub: [@ilyashamza70](https://github.com/ilyashamza70)

## 🙏 Acknowledgments

- Rich library for the colorful interface
- Matplotlib for visualizations
- Pandas for data management
- The open source community

---

⭐ If you found this project useful, please leave a star on GitHub!

## 🌍 Language

This project is primarily designed for Italian universities but can be adapted for other educational systems. Documentation available in:
- 🇮🇹 Italian: `README.md` and `DOCUMENTAZIONE_IT.md`
- 🇬🇧 English: `README_EN.md` (this file)
