def POLI_DIV(d, po):
    f = list(d)
    n = po[0]
    for i in range(len(d)-(len(po)-1)):
        f[i] = f[i]/n 
        co = f[i]
        if co != 0: 
            for j in range(1, len(po)):
                f[i + j] += -po[j] * co
    b = -(len(po)-1)
    x=f[b:]
    while x[0]==0:
        x.pop(0)
    return f[:b], x

def raicesenintervalo (funcion,inicio,final):
    lista=[]
    lista.append(funcion)
    derivada=[]
    for i in range(len(funcion)-1):
        aux_3=-(i-len(funcion)+1)*funcion[i]
        derivada.append(aux_3)
    n=len(derivada)
    lista.append(derivada)
    lista_1=[]
    lista_2=[]
    cambio_1=0
    cambio_2=0
    while n > 1 :
        n_1=len(lista)
        a=lista[n_1-2]
        b=lista[n_1-1]
        h,c=POLI_DIV(a, b)
        for i in range(len(c)):
            c[i]=c[i]*-1
        lista.append(c)
        n=len(c)
        #hasta aqui va bien
    for i in range(len(lista)):
        aux=0
        r=len(lista[i])
        for l in range(r):
            aux=aux*inicio+lista[i][l]
        lista_1.append(aux)
        aux=0
        for k in range(r):
            aux=aux*final+lista[i][k]
        lista_2.append(aux)
    print(lista_1)
    print(lista_2)
    #checkpoint, aún funciona
    for i in range(len(lista_1)-1):
        if lista_1[i]>0:
            if lista_1[i+1]>0:
                cambio_1+=0
            else:
                cambio_1+=1
        else:
            if lista_1[i+1]<0:
                cambio_1+=0
            else:
                cambio_1+=1
    for i in range(len(lista_2)-1):
        if lista_2[i]>0:
            if lista_2[i+1]>0:
                cambio_2+=0
            else:
                cambio_2+=1
        else:
            if lista_2[i+1]<0:
                cambio_2+=0
            else:
                cambio_2+=1
    
    print("Se encontraron ",cambio_1-cambio_2, " raíces en el intervalo ","[",inicio,",", final,"]")
raicesenintervalo([1,0,0,-4,0,1,-2],-2,2)
