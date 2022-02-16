import random

def gen_otp():
    main = ''
    for i in range(4): main+=str(random.randrange(0,10))
    return main


if __name__=='__main__':
    pass