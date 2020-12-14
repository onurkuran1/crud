
import logging
import time
import names
from random import randint

def numGen():
    number = ""
    for i in range(9):
        value = randint(0, 9)
        value = str(value)
        number = number + value
    return number



def memberReg():
    name = names.get_full_name()
    firstValue = randint(1, 9)
    num = numGen()
    phoneNumber = str(0) + str(firstValue) + num
    num = numGen()
    firstValue = randint(1, 9)
    secondValue = randint(0, 9)
    identificationNumber = str(firstValue) + str(secondValue) + num
    return name,phoneNumber,identificationNumber