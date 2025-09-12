# ex188: In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
def make_negative( number ):
    return -abs(number)


if __name__ == "__main__":
    print(make_negative(1))  # -1
    print(make_negative(-5))  # -5
    print(make_negative(0))  # 0
