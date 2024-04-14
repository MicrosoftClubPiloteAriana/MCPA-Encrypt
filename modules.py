import random

rand_chars = ":;,%*/-+^¨£#~&}]|"


def encrypt(message):
    encrypted = []
    key = []

    for i in range(len(message)):  # characters to ascii
        encrypted.append(str(ord(message[i])))
    #print(encrypted)
    for code in encrypted: # keep the length of numbers in the ascii code
        key.append(str(len(code)))
    key = "".join(key)
    #print(key)
    message = "".join(encrypted)
    #print(message)

    for i in range(len(message)):  # add random numbers
        x = random.randrange(0, len(message))
        message = message[0:x] + random.choice(rand_chars) + message[x:]
        #print(message)

    i = 0
    count_symbol = 0
    count_picker = 0
    while i < len(message):  # replace some numbers with "!"
        if message[i].isdigit() and count_picker % 3 == 0:
            if int(message[i]) != 0:
                count_symbol = int(message[i])
                message = message[:i] + "!" * count_symbol + message[i + 1:]
            i += count_symbol
            i += 1
        else:
            i += 2
        count_picker += 1
        #print(message)

    code = message + '$' + key
    #print(code)
    return code


def decrypt(code):
    message = ""
    key = code.split("$")[1]
    code = code.split("$")[0]
    for i in range(len(code)):  # remove random characters
        if code[i] not in rand_chars:
            message += code[i]
        #print(message)
    
    count_symbol = 0
    decoded_message = ""
    for i in range(len(message)):
        if message[i] == "!":
            count_symbol += 1
            if i!=len(message)-1:
                if message[i+1] != "!":
                    decoded_message = decoded_message+str(count_symbol)
                    count_symbol = 0
            else:
                decoded_message = decoded_message+str(count_symbol)
                count_symbol = 0
        else:
            decoded_message = decoded_message + message[i]
    #print(decoded_message)
    
    ascii_list = []
    start = 0
    for i in range(len(key)):
        end = int(key[i]) + start
        ascii_code = decoded_message[start:end]
        # print(ascii_code)
        # print(start)
        # print(end)
        ascii_list.append(ascii_code)
        start = end
    #print(ascii_list)
    message = ""
    for i in range(len(ascii_list)):
        message += chr(int(ascii_list[i]))
    return message