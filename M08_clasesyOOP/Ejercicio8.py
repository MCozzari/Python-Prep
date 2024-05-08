class Modulo7:

    def __init__(self,lista):
        self.lista=lista
    
    def verif_primo(self):
        for i in self.lista:
            if (self.__verif_primo(i)):
                print("El numero", i, "es primo")
            else:
                print("El numero", i, "no es primo")

    def conver(self,origen,destino):
        for i in self.lista:
            print("La conversion de",i,"grado",origen, "a", destino, "es", self.__conver(i,origen,destino))
    
    def factorial(self):
        for i in self.lista:
            print("El factorial de ",i, "es:",self.__factorial(i))

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
            else:
                print("El valor ingresado como medida de destino es incorrecto, por favor ingrese: C para Celsius, F para Farenheit y K para Kelvin")
        elif origen=="F":
            if destino=="C":
                return((grado-32)*5/9)
            elif destino=="K":
                return((self.__conver(grado,"F","C"))+273.15)
            elif destino=="F":
                return grado
            else:
                print("El valor ingresado como medida de destino es incorrecto, por favor ingrese: C para Celsius, F para Farenheit y K para Kelvin")
        elif origen=="K":
            if destino=="C":
                return(grado-273.15)
            elif destino=="F":
                return((self.__conver(grado,"K","C")*9/5)+32)
            elif destino=="K":
                return grado
            else:
                print("El valor ingresado como medida de destino es incorrecto, por favor ingrese: C para Celsius, F para Farenheit y K para Kelvin")
        else:
            print("El valor ingresado como medida de Origen es incorrecto, por favor ingrese: C para Celsius, F para Farenheit y K para Kelvin")

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