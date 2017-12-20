lista1=[]
lista2=[]
lista3=[]
valor=int(raw_input("Introduce un valor:"))
for i in range(11):
	lista1.append(valor+i)
valor=int(raw_input("Introduce otro valor:"))
for i in range(11):
	lista2.append(valor+i)		
for i in range(11):
	lista3.append(lista1[i]+lista2[i])
print "[1]",lista1
print "[2]",lista2
print "[1+2]",lista3
