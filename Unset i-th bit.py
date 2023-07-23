def unsetBit(number,bit):
    n=(1<<bit)
    if number&n:
        number= number &~ n
    return number 


number=int(input())
bit=int(input())
print(unsetBit(number,bit))