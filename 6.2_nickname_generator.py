def nickname_creator (name):
    name = name.lower()
    consonant_list = []
    vowel_list = []

    for letter in name:
        if letter != " ":
            if letter in ("a", "e", "i", "u", "o", "y"):
                vowel_list.append(letter)
            else:
                consonant_list.append(letter)

    nickname_exist = True

    if len(consonant_list) >= 3 and len(vowel_list) >= 3:
        nickname = consonant_list[-1].upper() + vowel_list[-1] + consonant_list[-2] + vowel_list[-2] + consonant_list[
            -3] + vowel_list[-3]
        nickname_exist = True
    elif len(consonant_list) >= 2 and len(vowel_list) >= 2:
        nickname = consonant_list[-1].upper() + vowel_list[-1] + consonant_list[-2] + vowel_list[-2]
        nickname_exist = True
    else:
        print("Not able to generate a nickname.")
        nickname_exist = False

    if nickname_exist == True:
        if nickname.lower() == name.lower():
            print("Not able to generate a nickname.")
        else:
            print(f"Your nickname: {nickname:s}")

def main():
    name=input("Enter your name.\n")
    nickname_creator(name)

main()