# ex184: Create a function which answers the question "Are you playing banjo?". If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"


if __name__ == "__main__":
    print(are_you_playing_banjo("Renan"))  # Renan plays banjo
    print(are_you_playing_banjo("Carlos"))  # Carlos does not play banjo
    print(are_you_playing_banjo("John"))  # John does not play banjo
