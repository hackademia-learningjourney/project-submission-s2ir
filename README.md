# Group Name
S2IR

# Project Title
Attendance Rate and Its Influence on Final Grades

# Group Members
- Sujan Thapa
- Rahul Thapa
- Ishwor Thapa
- Sujan Pun

# Project Description

## Project Idea and Approach
This project investigates the relationship between student attendance rates and final grades. The main goal is to analyze the strength of the connection between high attendance and better academic performance. By classifying students into four groups—"High Achievers," "Average," "Below Average," and "Struggling Students"—the project seeks to uncover patterns in attendance that correlate with academic outcomes. These insights can help educators identify at-risk students and enhance overall performance.

The study used quantitative methods, focusing on a dataset containing the attendance rates and final grades of 13 students. Various statistical analyses, including descriptive statistics, correlation analysis, and linear regression, were performed to determine the relationship between attendance and final grades.

## Tech Stack Used
- **Data analysis tools**: Python
- **Libraries and Packages**:
  - `pandas`: Data manipulation and analysis
  - `scikit-learn`: Machine learning and classification models
  - `numpy`: Numerical computations
  - `matplotlib`: Data visualization
  - `seaborn`: Statistical data visualization
  - `scipy`: Advanced statistical functions
  - `jupyter`: Interactive computing environment
- **Functionalities**:
  - Descriptive statistics (mean, standard deviation)
  - Pearson correlation coefficient analysis
  - Linear regression modeling
  - Scatter plot visualization

The project utilizes a simple classification model to categorize students based on their academic performance and attendance rates, providing insights into the positive relationship between attendance and academic success.


### Installation
- use requirement.txt to install dependencies
- install from requirements: `pip install -r requirements.txt`

### Config MAC (for venv)
- create python env: python3 -m venv env 
- source bin/activate # this will activate the environment for python

### File and Folder structure
- **src**: contain all source code, data, model
  - **data**: contain train data, testing data
    - **student_performance.csv**: use for to train model
  - **student_performance_trainer.ipynb**: This student_performance_trainer.ipynb script installs necessary Python packages (optional), preprocesses data, visualizes relationships between variables, trains a logistic regression model, evaluates the model.
  - **student_performance.ipynb**: This student_performance.ipynb script run the model take input from the user where user need to input student attendance rate.
- **readme.md**: simple readme.md file
- **requirements.txt**: file lists Python project dependencies, allowing easy installation of necessary packages with specified versions via pip.
- **.gitignore**: to prevent unnecessary files, like virtual environments and temporary files, from being tracked and uploaded to GitHub.
- **FinalReport.pdf**: report file. 

### How to?
- To train the model use "student_performance_trainer.ipynb" this is jupyter notebook file it run the whole program. This program first import dataset from the data/student_performance.csv file and train the model after train it will create and save model to model/attendance_rate_and_its_infulence_on_final_grades.pkl
- To evaluate the student performance, use "student_performance.ipynb". This notebook allows you to run the prediction program, which prompts you to input a student's attendance rate. Based on this input, the program will predict the student's academic performance.
- Also student_performance.py can be use as an app to predict student academic performance which is made based on student_performance.ipynb. To run `python student_performance.py`

