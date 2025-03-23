#a=input("podaj pierwszy bok")
#b=input("podaj drugi bok ")
#a=int(a)
#b=int(b)
#pole=a*b
#print("pole wynosi",pole )

#warunek istnienia trójkąta 
a=input("podaj pierwszy bok")
b=input("podaj drugi bok ")
c=input("podaj trzeci bok ")
a=int(a)
b=int(b)
c=int(c)
if a+b>c and b+c>a and c+a>b:
 print("trójkąt powstanie")
else:
 print("trójkąt nie powstanie")