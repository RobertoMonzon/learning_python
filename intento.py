columna = int(input("Teclea un numero al 10 "));

for a in range (1,columna +1,1):
    for b in range (1,a+1,1):
        print(b,end=" ");
    print("");
for c in range (1,columna +1,1):
    for d in reversed(range (columna-c,0,-1)):
        print(d,end=" ");
    print("");
