"""
Database of degree courses with their subjects and credits.
Supports both Bachelor's (Triennale) and Master's (Magistrale) degrees.
"""

# Master's Degrees (Magistrale)
MAGISTRALE_COURSES = {
    "Embedded Systems": {
        "type": "magistrale",
        "total_credits": 120,
        "courses": {
            "Electronics for embedded systems": 10,
            "Computer architectures": 10,
            "Operating systems for embedded systems": 8,
            "Specification and simulation of digital systems": 6,
            "Synthesis and optimization of digital systems": 6,
            "Microelectronic systems": 6,
            "Cybersecurity for Embedded Systems": 6,
            "Software engineering": 8,
            "Energy management for IoT": 6,
            "System-on-chip architecture": 6,
            "Testing and fault tolerance": 6,
            "Technologies for Autonomous Vehicles": 6,
            "Modeling and optimization of embedded systems": 6,
            "Final project work": 30
        }
    },
    "Computer Science": {
        "type": "magistrale",
        "total_credits": 120,
        "courses": {
            "Advanced Algorithms": 12,
            "Machine Learning": 12,
            "Distributed Systems": 9,
            "Database Systems": 9,
            "Software Architecture": 9,
            "Cybersecurity": 6,
            "Cloud Computing": 6,
            "Big Data Analytics": 6,
            "Computer Vision": 6,
            "Natural Language Processing": 6,
            "Artificial Intelligence": 9,
            "Final project work": 30
        }
    },
    "Data Science": {
        "type": "magistrale",
        "total_credits": 120,
        "courses": {
            "Statistical Learning": 12,
            "Deep Learning": 12,
            "Data Mining": 9,
            "Big Data Technologies": 9,
            "Business Intelligence": 6,
            "Data Visualization": 6,
            "Time Series Analysis": 6,
            "Optimization Methods": 6,
            "Text Analytics": 6,
            "Computer Vision": 6,
            "Advanced Statistics": 9,
            "Research Methods": 3,
            "Final project work": 30
        }
    }
}

# Bachelor's Degrees (Triennale)
TRIENNALE_COURSES = {
    "Computer Engineering": {
        "type": "triennale",
        "total_credits": 180,
        "courses": {
            "Mathematical Analysis I": 12,
            "Mathematical Analysis II": 9,
            "Linear Algebra": 9,
            "Physics I": 12,
            "Physics II": 9,
            "Computer Programming": 12,
            "Data Structures": 9,
            "Computer Architecture": 9,
            "Operating Systems": 9,
            "Databases": 9,
            "Computer Networks": 9,
            "Software Engineering": 9,
            "Algorithms": 9,
            "Digital Electronics": 6,
            "Signal Processing": 6,
            "Web Technologies": 6,
            "English Language": 3,
            "Elective Course": 6,
            "Final Thesis": 6
        }
    },
    "Information Technology": {
        "type": "triennale",
        "total_credits": 180,
        "courses": {
            "Mathematics I": 12,
            "Mathematics II": 9,
            "Physics": 9,
            "Programming Fundamentals": 12,
            "Object-Oriented Programming": 9,
            "Data Structures and Algorithms": 12,
            "Computer Architecture": 9,
            "Operating Systems": 9,
            "Computer Networks": 9,
            "Database Systems": 9,
            "Software Engineering": 9,
            "Web Development": 9,
            "Mobile Development": 6,
            "Information Security": 6,
            "Systems Administration": 6,
            "Project Management": 6,
            "Statistics": 6,
            "English Language": 3,
            "Final Project": 6
        }
    },
    "Mathematics": {
        "type": "triennale",
        "total_credits": 180,
        "courses": {
            "Mathematical Analysis I": 12,
            "Mathematical Analysis II": 12,
            "Mathematical Analysis III": 9,
            "Linear Algebra": 12,
            "Geometry": 9,
            "Probability": 9,
            "Statistics": 9,
            "Numerical Analysis": 9,
            "Differential Equations": 9,
            "Abstract Algebra": 9,
            "Topology": 6,
            "Mathematical Logic": 6,
            "Physics I": 9,
            "Physics II": 9,
            "Computer Programming": 9,
            "Optimization": 6,
            "English Language": 3,
            "Elective Course": 6,
            "Final Thesis": 6
        }
    }
}

def get_all_courses():
    """Return all available degree courses."""
    return {**TRIENNALE_COURSES, **MAGISTRALE_COURSES}

def get_course_info(course_name):
    """Get information about a specific degree course."""
    all_courses = get_all_courses()
    return all_courses.get(course_name)

def list_courses_by_type(course_type):
    """List all courses of a specific type (triennale or magistrale)."""
    all_courses = get_all_courses()
    return {name: info for name, info in all_courses.items() if info["type"] == course_type}
