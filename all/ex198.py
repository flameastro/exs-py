# ex198: Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
def get_grade(s1, s2, s3):
    s = sum([s1, s2, s3]) / 3
    return "A" if s <= 100 and s >= 90 else "B" if s >= 80 and s < 90 else "C" if s >= 70 and s < 80 else "D" if s >= 60 and s < 70 else "F"


if __name__ == "__main__":
    print(get_grade(95, 90, 93))  # A
    print(get_grade(39, 100, 89))  # C
    print(get_grade(54, 76, 100))  # C
    print(get_grade(22, 15, 67))  # F
