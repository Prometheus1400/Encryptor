# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:52:52 2020

@author: Kaleb Dickerson
"""
from random import randint

def Is_It_Prime(x):
    Prime = True
    for i in range(2,x):
        if x % 2 == 0:
            Prime = False
    return Prime
def Encode():
    Input = input('Enter what you wish to encrypt here: ').upper()
    IsPrime1,IsPrime2 = False,False
    Length1,Length2,Code1,Code2 = 0,0,0,0
    while IsPrime1 == False and IsPrime2 == False and Length1 < 4 and Length2 < 4 and len(str(Code1*Code2)) != 8:
        Code1 = str(randint(1,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        Code2  = str(randint(1,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        Code1,Code2 = int(Code1),int(Code2)
        Length1,Length2 = len(str(Code1)),len(str(Code2))
        IsPrime1,IsPrime2 = Is_It_Prime(Code1),Is_It_Prime(Code2)
        Key = Code1 * Code2

    Let2Num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,' ':26,'.':27,',':28,'!':29,'?':30,'/':31,'0':32,'1':33,'2':34,'3':35,'4':36,'5':37,'6':38,'7':39,'8':40,'9':41}
    
    Count = 0
    print('This is your message: ')
    for j in range(len(Input)):
        try:
            Val = str(Let2Num[Input[j]] + int(str(Key)[(Count)]))
        except:
            Val = '42'
        if len(Val) == 1:
            Val = '0'+str(Val)
        print(Val,end='')
        Count += 1
        if Count == 8:
            Count = 0
    print()
    print('----------------------------')
    print('This is your key: ',Key)
    print('----------------------------')
def Decode():
    Num2Let = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:' ',27:'.',28:',',29:'!',30:'?',31:'#',32:'0',33:'1',34:'2',35:'3',36:'4',37:'5',38:'6',39:'7',40:'8',41:'9'}
    InputCode = input('Enter the message you wish to decode here: ')
    if len(InputCode) % 2 != 0:
        InputCode = InputCode[:-1]
    InputKey = input('Enter your 8 digit key here: ')
    while len(InputKey) != 8:
        print('Your code is the wrong length! Try again.')
        InputKey = input('Enter your 8 digit key here: ')
    StringSlice = 0
    CountKey = 0
    for i in range(int(len(InputCode)/2)):
        ToDecode = InputCode[StringSlice:StringSlice+2]
        if ToDecode == '42':
            Text = '*'
        else:
            Text = Num2Let[abs((int(ToDecode) - int(InputKey[CountKey])))]
        print(Text.lower(),end='')
        StringSlice += 2
        CountKey += 1
        if CountKey == 8:
            CountKey = 0
def Main():
    Choice = input('Do you want to Encode or Decode (quit to stop): ').upper()
    
    while Choice != 'QUIT':
        if Choice == 'ENCODE':
            Encode()
        elif Choice == 'DECODE':
            Decode()
        else:
            print('Your choice was not recognized')
        Choice = input('Do you want to Encode or Decode (quit to stop): ').upper()
    print('Program Terminated')

Main()