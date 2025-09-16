# ex180:You are going to be given a non-empty string. Your job is to return the middle character(s) of the string. If the string's length is odd, return the middle character. If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"
def get_middle(s):
    length = (len(s) // 2)
    return s[length-1:length+1] if len(s) % 2 == 0 else s[length]


if __name__ == "__main__":
    print(get_middle("test"))  # es
    print(get_middle("middle"))  # dd
    print(get_middle("half"))  # al
