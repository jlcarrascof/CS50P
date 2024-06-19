# Exercise III - Lesson 00 - Functions and Variables

# Faces

def convert(str):
    if ":(" in str:
        str = str.replace(":(", "🙁")
    elif ":)" in str:
        str = str.replace(":)", "🙂")
    return str

def main():
    str = input()
    print(convert(str))

main()
