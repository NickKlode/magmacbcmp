
def padcode():
    return "00100000"


def padding(string):
    padwith = padcode() 

    num = len(string)%64
    if (num!=0):
        pad = (64 - num)//8
        string = string + padwith*pad

    return string

def depadding(string):
    padwith = padcode()
    padwith = padwith[::-1]
    string = string[::-1]

    while (string[:8]==padwith):
        string = string[8:]

    return string[::-1]