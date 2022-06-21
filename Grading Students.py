def gradingStudents(grades):
    final_grade = []
    for i in grades:
        if i > 37:
            next_multiple_of_5 = ((i // 5)*5 + 5)
            if next_multiple_of_5 - i < 3:
                final_grade.append(next_multiple_of_5)
            else:
                final_grade.append(i)
        else:
            final_grade.append(i)
    
    return final_grade
