# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           "Loop": "Um processo de repetição infinita",}
#
#
# print(programming_dictionary["Loop"])
# # programming_dictionary["Bug"]= "É UM MOSQUITO"
#
#
#
# # for key in programming_dictionary:
# #     print(key + ": " + programming_dictionary[key])
# programming_dictionary = {}
# print(programming_dictionary)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:

    nota = student_scores[student]

    if nota >= 91:
        Grade = "Outstanding"
    elif nota >= 81 and nota <= 90:
        Grade = "Exceeds Expectations"
    elif nota >= 71 and nota <= 80:
        Grade = "Acceptable"
    else:
        Grade = "Fail"

    student_grades[student] = Grade

print(student_grades)










