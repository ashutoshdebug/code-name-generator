a=input("Enter name to get code:")
b=len(a)
c=[]
for ch in range(b):
    if a[ch]=='a':
        c.append(1)
    elif a[ch]=='b':
        c.append(2)
    elif a[ch]=='c':
        c.append(3)
    elif a[ch]=='d':
        c.append(4)
    elif a[ch]=='e':
        c.append(5)
    elif a[ch]=='f':
        c.append(6)
    elif a[ch]=='g':
        c.append(7)
    elif a[ch]=='h':
        c.append(8)
    elif a[ch]=='i':
        c.append(9)
    elif a[ch]=='j':
        c.append(10)
    elif a[ch]=='k':
        c.append(11)
    elif a[ch]=='l':
        c.append(12)
    elif a[ch]=='m':
        c.append(13)
    elif a[ch]=='n':
        c.append(14)
    elif a[ch]=='o':
        c.append(15)
    elif a[ch]=='p':
        c.append(16)
    elif a[ch]=='q':
        c.append(17)
    elif a[ch]=='r':
        c.append(18)
    elif a[ch]=='s':
        c.append(19)
    elif a[ch]=='t':
        c.append(20)
    elif a[ch]=='u':
        c.append(21)
    elif a[ch]=='v':
        c.append(22)
    elif a[ch]=='w':
        c.append(23)
    elif a[ch]=='x':
        c.append(24)
    elif a[ch]=='y':
        c.append(25)
    elif a[ch]=='z':
        c.append(26)
    elif a[ch]=='A':
        c.append(1)
    elif a[ch]=='B':
        c.append(2)
    elif a[ch]=='C':
        c.append(3)
    elif a[ch]=='D':
        c.append(4)
    elif a[ch]=='E':
        c.append(5)
    elif a[ch]=='F':
        c.append(6)
    elif a[ch]=='G':
         c.append(7)
    elif a[ch]=='H':
        c.append(8)
    elif a[ch]=='I':
        c.append(9)
    elif a[ch]=='J':
        c.append(10)
    elif a[ch]=='K':
        c.append(11)
    elif a[ch]=='L':
        c.append(12)
    elif a[ch]=='M':
        c.append(13)
    elif a[ch]=='N':
        c.append(14)
    elif a[ch]=='O':
        c.append(15)
    elif a[ch]=='P':
        c.append(16)
    elif a[ch]=='Q':
        c.append(17)
    elif a[ch]=='R':
        c.append(18)
    elif a[ch]=='S':
        c.append(19)
    elif a[ch]=='T':
        c.append(20)
    elif a[ch]=='U':
        c.append(21)
    elif a[ch]=='V':
        c.append(22)
    elif a[ch]=='W':
        c.append(23)
    elif a[ch]=='X':
        c.append(24)
    elif a[ch]=='Y':
        c.append(25)
    elif a[ch]=='Z':
        c.append(26)
print("Your code is:",)
for i in c:
    print(i,end='')

#Abhay's version:
A=input("enter your name: ")
L=A.lower()
B=len(L)
C=[]
for n in range(B):
    if L[n]=='a':
        C.append(1)
    elif L[n]=='b':
        C.append(2)
    elif L[n]=='c':
        C.append(3)
    elif L[n]=='d':
        C.append(4)
    elif L[n]=='e':
        C.append(5)
    elif L[n]=='f':
        C.append(6)
    elif L[n]=='g':
        C.append(7)
    elif L[n]=='h':
        C.append(8)
    elif L[n]=='i':
        C.append(9)
    elif L[n]=='j':
        C.append(10)
    elif L[n]=='k':
        C.append(11)
    elif L[n]=='l':
        C.append(12)
    elif L[n]=='m':
        C.append(13)
    elif L[n]=='n':
        C.append(14)
    elif L[n]=='o':
        C.append(15)
    elif L[n]=='p':
        C.append(16)
    elif L[n]=='q':
        C.append(17)
    elif L[n]=='r':
        C.append(18)
    elif L[n]=='s':
        C.append(19)
    elif L[n]=='t':
        C.append(20)
    elif L[n]=='u':
        C.append(21)
    elif L[n]=='v':
        C.append(22)
    elif L[n]=='w':
        C.append(23)
    elif L[n]=='x':
        C.append(24)
    elif L[n]=='y':
        C.append(25)
    elif L[n]=='z':
        C.append(26)
    else:
        print("error")
print("your name's numarical value is; ",)
for i in C:
    print(i,end="")