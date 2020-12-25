

def crack_encryption(subjectNumber, divisor, publicKey):
    value = 1
    count = 0
    while True:
        count += 1
        value = value * subjectNumber
        value = value % divisor
        if publicKey == value:
            return count

def transform(loop,divisor,subjectNumber):
    value = 1
    for i in range(loop):
        value *= subjectNumber
        value = value % divisor
    return value


def partOne():
    card = 7573546
    room = 17786549

    # Sample
    # card = 5764801
    # room = 17807724

    # loop = crack_encryption(7,20201227,17807724)
    loop = crack_encryption(7,20201227,room)
    print(loop)
    # answer = transform(loop,20201227,5764801)
    answer = transform(loop,20201227,card)
    print(answer)

if __name__=='__main__':
    partOne()
