# PROGRAMACION-3-ZK-JJ-JS
import math

class Calculadora:
    def validar_numero(self, valor):
        try:
            numero = float(valor)
            if math.isnan(numero) or math.isinf(numero):
                raise ValueError("Número inválido")
            return numero
        except:
            return 0
    
    def suma(self):
        resultado = 0
        while True:
            A = input("Ingrese los números que desea operar, pulse '.' para terminar: ")
            if A == ".":
                break
            numero = self.validar_numero(A)
            if numero is not 0:
                resultado += numero
            else:
                print("Error: Ingrese un número válido")
        print(f"La suma es: {resultado}")
        return resultado

    def resta(self):
        resultado = 0
        primero = True
        while True:
            B = input("Ingrese los números que desea operar, pulse '.' para terminar: ")
            if B == ".":
                break
            numero = self.validar_numero(B)
            if numero is not 0:
                if primero:
                    resultado = numero
                    primero = False
                else:
                    resultado -= numero
            else:
                print("Error: Ingrese un número válido")
        print(f"La resta es: {resultado}")
        return resultado
    
    def multiplicacion(self):
        resultado = 1
        while True:
            C = input("Ingrese los números que desea operar, pulse '.' para terminar: ")
            if C == ".":
                break
            numero = self.validar_numero(C)
            if numero is not 0:
                resultado *= numero
            else:
                print("Error: Ingrese un número válido")
        print(f"La multiplicación es: {resultado}")
        return resultado

    def division(self):
        resultado = 0
        primero = True
        while True:
            D = input("Ingrese los números que desea operar, pulse '.' para terminar: ")
            if D == ".":
                break
            numero = self.validar_numero(D)
            if numero is not 0:
                if primero:
                    resultado = numero
                    primero = False
                else:
                    if numero == 0:
                        print("ERROR: NO SE PUEDE DIVIDIR ENTRE 0")
                    else:
                        resultado /= numero
            else:
                print("Error: Ingrese un número válido")
        print(f"La división es: {resultado}")
        return resultado

    def seno(self, angulo):
        resultado = math.sin(math.radians(angulo))
        return round(resultado, 4)
    
    def coseno(self, angulo):
        resultado = math.cos(math.radians(angulo))
        return round(resultado, 4)
    
    def tangente(self, angulo):
        if abs(angulo % 180 - 90) < 0.0001:
            raise ValueError("Tangente indefinida en 90°")
        resultado = math.tan(math.radians(angulo))
        return round(resultado, 4)
    
    def factorial(self, numero):
        if numero < 0:
            raise ValueError("No se permite negativos")
        resultado = math.factorial(numero)
        return resultado
    
    def mcd(self, num1, num2):
        resultado = math.gcd(abs(num1), abs(num2))
        return resultado

    def raiz (self,num1, num2):
        num1=float(input("Ingrese el Radicando -> "))
        num2=int(input("Ingrese el Indice -> "))
        if num2==0:
            print("ERROR, No se Existe raiz con indice 0 ")
        else:
            num2=1/num2
            Resultado=math.pow(num1,num2)
            print(f"El resultado es: {Resultado}")
    def Fibonacci (self,num1):
        a, b= 0, 1
        n=int(input("Ingrese la posicion del numero a ver -> "))
        if n==0:
            print (f"El numero Fibonaci en la posicion {n} es:  {a}")
        elif n==1:
            print (f"El numero Fibonaci en la posicion {n} es: {b}")
        else:
            for i in range(2, n+1):
                c=a+b
                a, b=b,c
        print (f"El numero Fibonaci en la posicion {n} es: {b}")

    def iva (self, valor, iva):
        valor=float(input("Ingrse el precio -> "))
        iva=float(input("Ingrese el valor del iva -> "))
        Tiva=valor*iva/100
        total=valor+Tiva
        print(f"EL valor total con iva es : {total} ")
    
class Interfaz:
    def __init__(self):
        self.calc = Calculadora()
    
    def obtener_numero(self, msg):
        while True:
            entrada = input(msg)
            numero = self.calc.validar_numero(entrada)
            if numero is not 0:
                return numero
            print("Error: Ingrese un número válido (no imaginarios)")
    
    def obtener_entero(self, msg):
        while True:
            try:
                entrada = input(msg)
                numero = self.calc.validar_numero(entrada)
                if numero is not 0:
                    return int(numero)
                else:
                    print("Error: Ingrese un número válido (no imaginarios)")
            except ValueError:
                print("Error: Debe ser un número entero")
    
    def menu_opbasicas(self):
        while True:
            print("\n" + "="*40)
            print("OPERACIONES BÁSICAS")
            print("="*40)
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Volver")
            print("="*40)
            
            opcion = input("Opción: ").strip()
            
            match opcion:
                case "1":
                    self.calc.suma()
                case "2":
                    self.calc.resta()
                case "3":
                    self.calc.multiplicacion()
                case "4":
                    self.calc.division()
                case "5":
                    break
                case _:
                    print("Opción inválida")

    def menu_trigonometricas(self):
        while True:
            print("\n" + "="*40)
            print("TRIGONOMÉTRICAS")
            print("="*40)
            print("1. Seno")
            print("2. Coseno")
            print("3. Tangente")
            print("4. Volver")
            print("="*40)
            
            opcion = input("Opción: ").strip()
            
            match opcion:
                case "1":
                    try:
                        ang = self.obtener_numero("Ángulo en grados: ")
                        print(f"✓ Resultado: {self.calc.seno(ang)}")
                    except ValueError as e:
                        print(f"Error: {e}")
                case "2":
                    try:
                        ang = self.obtener_numero("Ángulo en grados: ")
                        print(f"✓ Resultado: {self.calc.coseno(ang)}")
                    except ValueError as e:
                        print(f"Error: {e}")
                case "3":
                    try:
                        ang = self.obtener_numero("Ángulo en grados: ")
                        print(f"✓ Resultado: {self.calc.tangente(ang)}")
                    except ValueError as e:
                        print(f"Error: {e}")
                case "4":
                    break
                case _:
                    print("Opción inválida")
    
    def menu_factorial(self):
        try:
            num = self.obtener_entero("Número: ")
            print(f"✓ Resultado: {self.calc.factorial(num)}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def menu_mcd(self):
        try:
            num1 = self.obtener_entero("Primer número: ")
            num2 = self.obtener_entero("Segundo número: ")
            print(f"✓ Resultado: {self.calc.mcd(num1, num2)}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def ejecutar(self):
        print("\n" + "="*40)
        print("CALCULADORA")
        print("="*40)
        
        while True:
            print("\n" + "="*40)
            print("MENÚ PRINCIPAL")
            print("="*40)
            print("1. Operaciones Básicas")
            print("2. Trigonométricas")
            print("3. Factorial")
            print("4. MCD")
            print("5. Raices)
            print("6. IVA)
            print("7. Fibonacci)
            print("8. Salir")
            print("="*40)
            
            opcion = input("Opción: ").strip()
            
            match opcion:
                case "1":
                    self.menu_opbasicas()
                case "2":
                    self.menu_trigonometricas()
                case "3":
                    self.menu_factorial()
                case "4":
                    self.menu_mcd()
                case "5":
                    self.menu_Raices()
                case "6":
                    self.menu_iva()
                case "7":
                    self.menu_Fibonacci()
                case "8":
                    print("\n¡Hasta luego!\n")
                    break
                case _:
                    print("Opción inválida")


if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.ejecutar()
