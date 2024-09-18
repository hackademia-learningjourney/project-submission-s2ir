import pandas as pd
import pickle
from utils import Utils  # Use Model to test input data and give suggestion

loaded_model = None

# Load the Model
model_name = "model/attendance_rate_and_its_infulence_on_final_grades.pkl"
try:
    with open(model_name, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    print(f"Model file {model_name} not found. Please ensure the model is trained and the path is correct.")

if loaded_model is not None:
    while True:
        try:
            # Input data from the user
            attendance_rate = float(input("Enter student attendance rate (or type 'exit' to quit): "))
            input_data_df = pd.DataFrame([attendance_rate], columns=['AttendanceRate'])
            
            # Making predictions
            predictions = loaded_model.predict(input_data_df)
            
            if predictions and len(predictions) > 0:
                print(f"Predicted data is {Utils.get_cat_student(predictions[0])}")
            else:
                print("No predictions available.")
        
        except ValueError:
            # To handle 'exit' and invalid inputs
            user_input = input("Invalid input! Type 'exit' to quit or press Enter to try again: ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break  # Exit the loop
else:
    print("Please train the model and run again.")
