nombre= str(input("donner des nombres séparés par une virgule:"))
liste=split(nombre)
liste_entier=[]
for i in range (len(liste)):
  liste_entier[i]=int(liste[i])

s=0
for i in range (len(liste_entier)):
  s= s+ liste_entier[i]
moyenne= s/len(liste_entier)

sup=0
for i in range (len(liste_entier)):
  if liste_entier[i] > moyenne:
    sup+= 1

print("la somme des nombres est:", s)
print("la moyenne des nombres est:", moyenne)
print(f'il y a {sup} nombres qui sont au-dessus de la moyenne')
