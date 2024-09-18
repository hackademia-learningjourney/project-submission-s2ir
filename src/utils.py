class Utils:
  # Define target variables
  def cat_students(grade):
    if grade > 80: return 1 # High Achiver
    elif grade > 60: return 2 # Average
    elif grade > 50: return 3 # Below Average
    else: return 0 # Struggling Students

  def get_cat_student(code):
    if code == 1: return "High Achiver Student"
    elif code == 2: return "Average Student"
    elif code == 3: return "Below Average Student"
    else: return "Struggling Student"