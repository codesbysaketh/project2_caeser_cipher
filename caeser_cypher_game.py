logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
print("Welcome to caeser cipher!!!")


#caeser() function
def caeser(type, message, shift_par):
    if type == "encrypt":
        encoded_message = ""
        for letter in text:
            index_text = alphabet.index(letter)+shift_par
            if index_text>25:
                index_text = abs(26-index_text)
                encoded_message += alphabet[index_text]
            else:
                encoded_message += alphabet[index_text]
        print(f"The encoded text is {encoded_message}")
    elif type == "decrypt":
        decoded_message = ""
        for letter in text:
            index_text = alphabet.index(letter)-shift_par
            decoded_message += alphabet[index_text]
        print(f"The decoded message is {decoded_message}")
    else:
        print("Invalid input")

service = True

while service:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type encode to encrypt, decode to decrypt: ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Type shift number: "))

    caeser(type = direction, message = text, shift_par = shift)
    result = input("Type yes if you want to go again otherwise type no ").lower()
    if(result == "yes"):
        service = True
    elif(result == "no"):
        print("See you again, bye!")
        service = False
    else:
        print("Invalid input")
        service = False