import math
import random


def generateOTP():

    digit = "0123456789"
    OTP = ""
    

    for i in range(6):
        OTP += digit[math.floor(random.random()*10)]

    return OTP


if __name__ == "__main__":

    print("Otp of lenght 6 is :", generateOTP())
