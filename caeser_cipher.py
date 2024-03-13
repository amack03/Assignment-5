'''This program will scramble text that a user enters by using a Caeser cipher by an offset number entered by the user.
    The program will not scramble numbers, spaces, special characters, or other letters not used in American English'''

def caeser_cipher(offset, raw_text):
    result = ''
    for i in range(len(raw_text)):
    
        cc = raw_text[i]

        if cc.isalpha():
            if cc.isupper():
                cc = chr((ord(cc)-65 + offset) % 26 + 65)
                result += cc
            else:
                cc = chr((ord(cc)-97 + offset) % 26 + 97)
                result += cc

        else:
            result += cc
    return result

raw_text = str(input("Enter a phrase: "))
offset = int(input("Enter an offest: "))
result =caeser_cipher(offset, raw_text)

print(f'Scrambled Text: {result}')