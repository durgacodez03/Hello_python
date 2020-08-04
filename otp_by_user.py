import math
import random


def generateOTP():

    var = input("Enter the number of charcters")
    string_var = "123456789"
    OTP = ""
    length = len(string_var)
    print(length)

    for i in range(int(var)):
        OTP += string_var[math.floor(random.random()*length)]

    return OTP


if __name__ == "__main__":

    print("Otp of lenght 6 is :", generateOTP())
