def alphabet_position(letter):
    if ord(letter) < 91:
        return ord(letter) - 65
    elif ord(letter) > 96:
        return ord(letter) - 97


def rotate_character(char, rot):
    rotated = ""
    for item in char:
        if char.isalpha()== False:
            rotated = char
        elif char.isalpha()== True:
            newlet = (alphabet_position(char) + int(rot)) % 26
            if char.isupper():
                rotated = chr(newlet + 65)
            elif char.islower():
                rotated = chr(newlet + 97)
    return rotated

def encrypt(text, rot):
    laststr = ""
    for char in (text):
        rotate_character(char,rot)
        newletter = rotate_character(char,rot)
        laststr += newletter
    return laststr    
