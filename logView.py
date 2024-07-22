import pickle
import os

log_file = 'simulation_log.pkl'

def read_simulation_log(log_file):
    if os.path.exists(log_file):
        with open(log_file, 'rb') as f:
            log = pickle.load(f)
            return log
    else:
        print("Log file does not exist.")
        return None

def display_log(log):
    if log is not None:
        for entry in log:
            print(f"Grades: {entry['grades']}")
            print(f"Weighted Average: {entry['weighted_avg']:.2f}")
            print(f"Arithmetic Average: {entry['arithmetic_avg']:.2f}")
            print(f"Graduation Grade: {entry['graduation_grade']:.2f}")
            print("-" * 50)

# Read and display the log
log = read_simulation_log(log_file)
display_log(log)
