def decode(A):
    A=list(str(A))  #Se convierten los datos de int a list
    n=len(A)
    x=0
    for i in range (n):
        A[i]=int(A[i])  # Se convierte cada dato string a int
    for j in range (n-1):
        if (A[j]==1 and A[j+1]<=9) or (A[j]==2 and A[j+1]<=6):
            # Si el elemento esta en el rango de 0 a 26
            x+=1
    w=1
    for i in range(x): # Se obtienen todas las combinaciones
        w+=i+1
    return(w)
    

print (decode(8))
print (decode(12))
