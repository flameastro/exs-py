# ex182: Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string and return a new string with all vowels removed. For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
def disemvowel(s):
    for v in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        s = s.replace(v, "")

    return s


if __name__ == "__main__":
    print(disemvowel("This website is for losers LOL!"))  # Ths wbst s fr lsrs LL!
    print(disemvowel("We gonna put'n trash this SITE!"))  # W gnn pt'n trsh ths ST!
