# import random

# # chars = ['0'...'9']


# def encrypt(plain, key):
#     encrypted_text = ""

#     # 1234 -> 2345 with key of 1

#     for char in plain:
#         num = int(char)
#         shifted_num = (num + key) % 10
#         encrypted_text += str(shifted_num)

#     return encrypted_text


# def decrypt(encoded, key):
#     return encrypt(encoded, -key)


# if __name__ == "__main__":
#     pins = [
#         "1234",
#         "9876",
#         "0000",
#         "9999",
#     ]

#     for pin in pins:
#         key = random.randint(1, 9)
#         print("plain pin", pin)
#         encrypted_pin = encrypt(pin, key)
#         print("encrypted_pin", encrypted_pin)
#         decrypted_pin = decrypt(encrypted_pin, key)
#         print("decrypted_pin", decrypted_pin)

def encrypt(pin: str, key: int) -> str:
    encrypted_string = ""
    # for each character in the pin 
    for char in pin:
        # convert the character to an integer
        num = int(char)
        # add the key to the integer and modulo 10 to wrap it
        shifted_num = (num + key) % 10 # 1 - 1 = 0 , 0 % 10 =0
        # convert the new integer to a string and it to the string
        encrypted_string += str(shifted_num)
    return encrypted_string

def decrypt(pin: str, key: int) -> str:
    return encrypt(pin, -key)

if __name__ == "__main__":
    pins = [
        "1234",
        "2464",
        "0345",
        "8442",
    ]
    # key = 8
    import random
    for pin in pins:
        key = random.randint(1, 9)
        print("plain pin", pin)
        encrypted_pin = encrypt(pin, key)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, key)
        print("decrypted_pin", decrypted_pin)



