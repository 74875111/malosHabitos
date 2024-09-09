def calcular_producto_sumado(multiplicando1, multiplicando2, sumando):

    return multiplicando1 * multiplicando2 + sumando

def mostrar_resultado(resultado):

    print("El resultado es:", resultado)

def ejecutar_programa():

    valor1 = float(input("Insertar medida multiplicando 1: "))
    valor2 = float(input("Insertar medida multiplicando 2:  "))
    valor_suma = float(input("Insertar sumando: "))
    resultado = calcular_producto_sumado(valor1, valor2, valor_suma)
    mostrar_resultado(resultado)

if __name__ == "__main__":
    ejecutar_programa()