def get_grade(*args):
    #making readability priority
    args1 = len(args)
    avgGrade = sum(args)/ args1
    if 90 <= avgGrade <= 100:
        return 'A'
    elif 80 <= avgGrade < 90:
        return 'B'
    elif 70 <= avgGrade < 80:
        return 'C'
    elif 60 <= avgGrade < 70:
        return 'D'
    else:
        return "F"


print(get_grade(70, 70, 100))
print(get_grade(92, 93, 94))
print(get_grade(92, 50, 43))
print(get_grade(92, 50, 68))
print(get_grade(12, 50, 43))