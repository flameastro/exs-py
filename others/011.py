# Check File is Empty or Not
# Write a program to check if the given file is empty or not
file = input("Type the file name: ")

try:
    with open(file, "r", encoding="utf-8") as f:
        f.seek(0)

        if f.read() == "":
            print("The file IS EMPTY")
        else:
            print("The file IS NOT EMPTY.")
except Exception as e:
    print(f"Please, verify if this file really exists. Erro: {e}")
