class Modulo7:

    def __init__(self,lista):
        if (type(lista)!=list):
            self.lista=[]
            raise ValueError("El argumento introducido es incorrecto, se ha introducido un ",type(lista), "y se esperaba una lista")
        else:
            self.lista=lista    

    def verif_primo(self):
        lista_primos=[]
        for i in self.lista:
            if (self.__verif_primo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    def conver(self,origen,destino):
        parametros=["C","F","K"]
        lista_conversion=[]
        if origen in parametros:
            if destino in parametros:
                for i in self.lista:
                    lista_conversion.append(self.__conver(i,origen,destino))
            else:
                print("El parametro enviado para el destino no es valido, debe ser:", parametros)
                return []
        else:
            print("El parametro enviado para el origen no es valido, debe ser:", parametros)
            return
        return lista_conversion


    
    def factorial(self):
        lista_factorial=[]
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial


    def __verif_primo (self,num):
        if num>0:
            primo=True
            for i in range(2,num):
                if num%i==0:
                    primo=False
                    break
            return primo
        else:
            return False
        
    def repe (self):
        cont=0
        for i in self.lista:
            if self.lista.count(i) > cont:
                cont=self.lista.count(i)
                numero=i
        return numero,cont
    
    def __conver(self,grado,origen,destino):
        if origen=="C":
            if destino=="F":
                return ((grado * 9/5) +32)
            elif destino=="K":
                return (grado+273.15)
            elif destino=="C":
                return grado
        elif origen=="F":
            if destino=="C":
                return((grado-32)*5/9)
            elif destino=="K":
                return((self.__conver(grado,"F","C"))+273.15)
            elif destino=="F":
                return grado
        elif origen=="K":
            if destino=="C":
                return(grado-273.15)
            elif destino=="F":
                return((self.__conver(grado,"K","C")*9/5)+32)
            elif destino=="K":
                return grado
            
    def __factorial(self,num):
        if type(num)==int:
            if num>1:
                return (num*self.__factorial(num-1))
            elif num==1:
                return 1
            else:
                return None
        else: 
            return None