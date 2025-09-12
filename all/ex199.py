# ex199: The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc. Given a year, return the century it is in.
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28
def century(year):
    return year // 100 if year % 100 == 0 else (year // 100) + 1


if __name__ == "__main__":
    print(century(1189))  # 12
    print(century(2232))  # 23
    print(century(1900))  # 19
