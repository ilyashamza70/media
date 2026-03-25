import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

# Definizione dei corsi e dei crediti
courses = {
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
    "Technologies for Autonomous Vehicles" : 6,	
    "Modeling and optimization of embedded systems": 6,
    "Final project work": 30

}

log_file = 'simulation_log.pkl'

def get_courses_from_DB(course):
    # Let's assume that the course is a key in the database
    # and we want to retrieve the corresponding value
    """
    Recupera i crediti di un corso dal database (simulato con un dizionario).
    """
    try:
        return courses[course]
    except KeyError:
        print(f"Errore: il corso '{course}' non esiste nel database.")
        return None
    
    
def calculate_weighted_average(grades):
    total_weight = sum(courses.values())
    weighted_sum = sum(grade * courses[course] for course, grade in grades.items())
    return weighted_sum / total_weight

def calculate_arithmetic_average(grades):
    return sum(grades.values()) / len(grades)

def calculate_graduation_grade(weighted_avg):
    return (weighted_avg / 30) * 110  # Supponendo che 30 sia il voto massimo e 110 il punteggio massimo di laurea

def plot_averages(weighted_avg, arithmetic_avg):
    labels = ['Weighted Average', 'Arithmetic Average']
    values = [weighted_avg, arithmetic_avg]
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title('Averages Comparison')
    plt.ylabel('Average')
    plt.show()

def plot_graduation_grade(graduation_grade):
    plt.bar(['Graduation Grade'], [graduation_grade], color='purple')
    plt.title('Predicted Graduation Grade')
    plt.ylabel('Grade')
    plt.show()

def save_simulation_log(grades, weighted_avg, arithmetic_avg, graduation_grade):
    simulation = {
        'grades': grades,
        'weighted_avg': weighted_avg,
        'arithmetic_avg': arithmetic_avg,
        'graduation_grade': graduation_grade
    }
    
    if os.path.exists(log_file):
        with open(log_file, 'rb') as f:
            log = pickle.load(f)
    else:
        log = []
    
    if simulation not in log:
        log.append(simulation)
        with open(log_file, 'wb') as f:
            pickle.dump(log, f)
        print("Simulation saved.")
    else:
        print("Simulation already exists.")

def main():
    grades = {}
    print("Enter your grades for the following courses:")
    for course in courses:
        grade = float(input(f"{course}: "))
        grades[course] = grade
    
    weighted_avg = calculate_weighted_average(grades)
    arithmetic_avg = calculate_arithmetic_average(grades)
    graduation_grade = calculate_graduation_grade(weighted_avg)
    
    print(f"Weighted Average: {weighted_avg:.2f}")
    print(f"Arithmetic Average: {arithmetic_avg:.2f}")
    print(f"Predicted Graduation Grade: {graduation_grade:.2f}")
    
    plot_averages(weighted_avg, arithmetic_avg)
    plot_graduation_grade(graduation_grade)
    
    save_simulation_log(grades, weighted_avg, arithmetic_avg, graduation_grade)

if __name__ == "__main__":
    main()
