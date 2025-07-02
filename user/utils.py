import random 

def otp_generater():
    code1 = random.randint(0, 9)
    code2 = random.randint(0, 9)
    code3 = random.randint(0, 9)
    code4 = random.randint(0, 9)

    final_otp = str(code1) + str(code2) + str(code3) + str(code4)
    return int(final_otp)

# print(otp_generater())
