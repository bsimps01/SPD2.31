# import math 

# grade_list = []
# sum_of_mean = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!

# def number_of_students():
#         # Get the inputs from the user
#     n_student = 5
#     for _ in range(0, n_student):
#         grade_list.append(int(input('Enter a number: ')))

# def sum_of_grade():
#         # Calculate the mean and standard deviation of the grades
#     for grade in grade_list:
#         return sum_of_mean + grade
#     mean = sum_of_mean / len(grade_list)

# def print_stat():
#     sd = 0 # standard deviation
#     sum_of_sqrs = 0
#     for grade in grade_list:
#         sum_of_sqrs += (grade - sum_of_mean) ** 2
#     sd = math.sqrt(sum_of_sqrs / len(grade_list))
#     # print out the mean and standard deviation in a nice format.
#     print('****** Grade Statistics ******')
#     print("The grades's mean is:", sum_of_mean)
#     print('The population standard deviation of grades is: ', round(sd, 3))
#     print('****** END ******')

# number_of_students()
# sum_of_grade()
# print_stat()

# LEGAL_DRINKING_AGE = 18
# class Person:
#     def __init__(self, my_age):
#         self.age = my_age
        
# def enter_night_club(individual, age):
#     if age > LEGAL_DRINKING_AGE:
#         print("Allowed to enter.")
#         return True
#     else:
#         print("Enterance of minors is denited.")
#         return False

    
# person = Person(17.9)
# enter_night_club(person, 21)

# def get_price():
#     discount_factor = 0
#     if base_price() > 1000: 
#         discount_factor = 0.95
#     else: 
#         discount_factor = 0.98
#     return base_price() * discount_factor

# def base_price():
#     base_price = quantity * item_price
#     return base_price

# WELL_DONE = 900000
# MEDIUM = 600000
# COOKED_CONSTANT = 0.05

# def is_cookeding_criteria_satisfied():
#     if well_done(): 
#         return True
#     if medium():
#         return True
#     return False

# def well_done(time, temperature, pressure, desired_state):
#     if desired_state == time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE: 
#         print('well-done')
#         return desired_state

# def medium(time, temperature, pressure, desired_state):
#     if desired_state == time * temperature * pressure * COOKED_CONSTANT >= MEDIUM:
#         print('medium')
#         return desired_state

# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# import math

# def estimated_distance():
#     xc1 = 4
#     yc1 = 4.25

#     xc2 = 53
#     yc2 = -5.35
# # Calculate the distance between the two circle
#     distance = math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)
#     print('distance', distance)
# # *** somewhere else in your program ***

# def estimated_length():
#     xa = -36
#     ya = 97

#     xb = .34
#     yb = .91
# # calcualte the length of vector AB vector which is a vector between A and B points.
#     length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
#     print('length', length)

# estimated_distance()
# estimated_length()
# # Written by Kamran Bigdely
# # Example for Compose Methods: Extract Method.
# # import math
# xc1 = 4
# yc1 = 4.25

# xc2 = 53
# yc2 = -5.35
# # Calculate the distance between the two circle
# distance = math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)
# print('distance', distance)
# # *** somewhere else in your program ***
# xa = -36
# ya = 97

# xb = .34
# yb = .91
# # calcualte the length of vector AB vector which is a vector between A and B points.
# length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
# print('length', length)
passed_students = []

class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5 # minimum acceptable GPA
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in passed_students:
            s.send_congrat_email()
            print(s.name)
        print('****************************')
        # Send congrat emails to them.
        # Find the top 10% of them and send their contact to the top employers
        passed_students.sort(key=lambda s: s.get_gpa())

    def elite_students(self):
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'), 
            Student(3.9, 'naruto'), Student(3.2,'kami'), Student(3,'guts')]
school  = School(students)
school.process_graduation()
school.elite_students()