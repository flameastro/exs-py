# ex241: Substring - Peça duas palavras. Verifique se a segunda palavra está contida na primeira.
def substring(p1, p2):
    return p2 in p1


if __name__ == "__main__":
    print(substring("Python", "yth"))  # True
    print(substring("JavaScript", "avo"))  # False
    print(substring("HTML, CSS, React", "3"))  # False
