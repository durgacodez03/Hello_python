import math, random

def generateOTP():
    
    string_var = "0123456789abcdefghijklmnop"
    OTP=""
    length = len(string_var)
    print(length)

    for i in range(6):
        OTP += string_var[math.floor(random.random()*length)]
    
    return OTP

if __name__ == "__main__":

    print("Otp of lenght 6 is :" ,generateOTP())