import string

def encrypt(phrase, shift):
    encrypted = ""
    for i in range(len(phrase)):
        letter = phrase[i].upper()
        index = string.ascii_uppercase.index(letter)
        index += shift
        if index > len(string.ascii_uppercase) - 1:
            index -= 26
        elif index < 0:
            letter += 26
        encrypted += string.ascii_uppercase[index]
    return encrypted


def decrypt(phrase, shift):
    return encrypt(phrase, -shift)


def main():
    phrase = input("Enter a phrase: ")
    shift = int(input("How much do you want to shift (1-26)? "))
    print(encrypt(phrase, shift))


main()