def parseRawData(raw_data):
  """
  This function parses raw data (assumed to be student information in string format)
  and converts it into a list of dictionaries. Each dictionary represents a student
  with 'name' and 'score' keys.

  Args:
      raw_data: String containing student information, one student per line.

  Returns:
      A list of dictionaries, where each dictionary represents a student.
  """
  students = []
  for line in raw_data.split('\n'):
    if line.strip():  # Check if line is not empty after removing whitespace
      name, score = line.split(', ')  # Split line by comma and space
      students.append({'name': name, 'score': int(score)})  # Add student data as dictionary
  return students

def calcAvgScore(students):
  """
  This function calculates the average score of all students in a provided list.

  Args:
      students: A list of dictionaries representing students (output from parseRawData).

  Returns:
      The average score (float) of all students.
  """
  total_score = sum(student['score'] for student in students)  # Sum all scores
  return total_score / len(students)  # Calculate average

def identifyUniqueStudents(class1, class2):
  """
  This function identifies students who are unique to each class (not present in both).

  Args:
      class1: A list of dictionaries representing students in Class 1.
      class2: A list of dictionaries representing students in Class 2.

  Returns:
      A tuple containing two lists:
          - Unique students in Class 1 (not in Class 2).
          - Unique students in Class 2 (not in Class 1).
  """
  unique_class1 = [student for student in class1 if student not in class2]
  unique_class2 = [student for student in class2 if student not in class1]
  return unique_class1, unique_class2

def identifyCommonStudents(class1, class2):
  """
  This function identifies students who are present in both Class 1 and Class 2.

  Args:
      class1: A list of dictionaries representing students in Class 1.
      class2: A list of dictionaries representing students in Class 2.

  Returns:
      A list of dictionaries representing students present in both classes.
  """
  common_students = []
  for student1 in class1:
    for student2 in class2:
      if student1['name'] == student2['name']:  # Check if names match
        common_students.append(student1)
        break  # Only add the first matching student (avoid duplicates)
  return common_students

def calcCombAvg(common_students):
  """
  This function calculates the average score for the common students (present in both classes).

  Args:
      common_students: A list of dictionaries representing students in both classes.

  Returns:
      The average score (float) of the common students.
  """
  total_score = sum(student['score'] for student in common_students)
  return total_score / len(common_students)

def calcUniqueAvg(unique_students):
  """
  This function calculates the average score for students in a provided list (assumed to be unique).

  Args:
      unique_students: A list of dictionaries representing students (unique to a class).

  Returns:
      The average score (float) of the unique students.
  """
  total_score = sum(student['score'] for student in unique_students)
  return total_score / len(unique_students)

# Sample data for Class 1 and Class 2 
class1_raw_data = {
    "John Doe": 85,
    "Jane Smith": 78,
    "Michael Brown": 92,
    "Emily Johnson": 88,
    "Daniel Wilson": 74,
    "Olivia Jones": 95,
    "William Garcia": 81,
    "Ava Martinez": 87,
    "Isabella Rodriguez": 90,
    "Sophia Anderson": 77,
    "Mason Lee": 83,
    "Ella Young": 79,
    "James Hernandez": 84,
    "Charlotte Gonzalez": 91,
    "Benjamin Perez": 75,
    "Amelia Lopez": 89,
    "Ethan White": 93,
    "Mia Thompson": 80,
    "Alexander Harris": 85,
    "Aria Clark": 82,
    "Henry Lewis": 76,
    "Evelyn Walker": 94,
    "Sebastian Hall": 72,
    "Abigail Allen": 86,
    "Liam Scott": 78,
    "Sophie Adams": 73,
    "Oscar Nelson": 88,
    "Luna King": 91,
    "Jack Wright": 79,
    "Lucas Green": 84
}

class2_raw_data = {
    "Isaac Moore": 89,
    "Eva Turner": 88,
    "Nathan Martin": 76,
    "Grace Hill": 92,
    "Samuel Adams": 85,
    "Zoe Davis": 81,
    "Aiden Robinson": 87,
    "Chloe Campbell": 90,
    "Gabriel Mitchell": 77,
    "Lily Anderson": 83,
    "Jane Smith": 82,
    "Emily Johnson": 90,
    "Daniel Wilson": 78,
    "Olivia Jones": 97,
    "Ella Young": 81,
    "Charlotte Gonzalez": 89,
    "Amelia Lopez": 91,
    "Mia Thompson": 82,
    "Alexander Harris": 88,
    "Sophia Anderson": 79,
    "Lucas Green": 86,
    "Jack Wright": 82,
    "Luna King": 93,
    "Oscar Nelson": 90,
    "Sophie Adams": 75,
    "Liam Scott": 80,
    "Henry Lewis": 88,
    "Aria Clark": 84,
    "Ethan White": 95,
    "Benjamin Perez": 77
}


# Process data
class1 = parseRawData(class1_raw_data)
class2 = parseRawData(class2_raw_data)

# Calculate average scores
avg_score_class1 = calcAvgScore(class1)
avg_score_class2 = calcAvgScore(class2)

# Identify common students and calculate their average score
common_students = identifyCommonStudents(class1, class2)
avg_score_common_students = calcCombAvg(common_students)

# Identify unique students for each class and calculate their average scores
unique_class1, unique_class2 = identifyUniqueStudents(class1, class2)
avg_score_unique_class1 = calcUniqueAvg(unique_class1)
avg_score_unique_class2 = calcUniqueAvg(unique_class2)

# Print the results
print("Average score for Class 1:", avg_score_class1)
print("Average score for Class 2:", avg_score_class2)
print("Average score for common students:", avg_score_common_students)
print("Average score for unique students in Class 1:", avg_score_unique_class1)
print("Average score for unique students in Class 2:", avg_score_unique_class2)
