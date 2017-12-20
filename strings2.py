#coding=utf-8

"""Pido el numero de alumnos"""
alum=int(raw_input("Introduce el numero de alumnos: "))	
while alum>50 or alum<0:
	print "Puedes añadir entre 0 y 50 alumnos"
	alum=int(raw_input("Introduce el numero de alumnos: "))	
notas=[]

"""Pido las notas"""
for i in range(alum):
	nota_afegir=int(raw_input("Introduce una nota:"))
	while nota_afegir<0 or nota_afegir>10:
		nota_afegir=(int(raw_input("Error. Introduce una nota entre 0 y 10: ")))
	notas.append(nota_afegir)

"""Imprimo las notas"""
print "Notas:",
for c in notas[:len(notas)-1]:
	print c,",",
print notas[len(notas)-1]
print "Mitja:",sum(notas)/len(notas)
print "Màxim:",max(notas)
print "Mínim:",min(notas)

int(raw_input("Introduce la nota a buscar:"))
		
print "Notas:",
for c in notas[:len(notas)-1]:
	print c,",",
print notas[len(notas)-1]
print "Mitja:",sum(notas)/len(notas)
print "Màxim:",max(notas)
print "Mínim:",min(notas)
