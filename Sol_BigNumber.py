import math
from sys import stdout

def CalcularDigitos(n):
  if n < 0:
    return 0
  if n <= 1:
    return 1

 
  num_digitos_log = n * math.log10(n / math.e) + math.log(2 * math.pi * n) / 2
  return int(math.floor(num_digitos_log))


try:
  numero= int(input("Ingrese el Numero: "))
except ValueError:
  print("Error: Debe ingresar un número entero.")
  exit()


cantidad_digitos = CalcularDigitos(numero)
stdout.write(f"La cantidad de dígitos del factorial {numero} es: {cantidad_digitos}\n")
