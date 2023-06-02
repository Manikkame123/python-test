
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "S"
            else:
                translation = translation + "s"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter Phrase :")))
