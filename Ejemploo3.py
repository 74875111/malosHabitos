def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):

    return 0.5 * base * altura

def mostrar_area_rectangulo(area):

    print("Área del rectángulo:", area)

def mostrar_area_triangulo(area):

    print("Área del triángulo:", area)

def ejecutar_calculos():

    base_rectangulo = float(input("Insertar medida base rectangulo: "))
    altura_rectangulo = float(input("Insertar medida altura rectangulo: "))
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    mostrar_area_rectangulo(area_rectangulo)

    base_triangulo = float(input("Insertar medida base triangulo: "))
    altura_triangulo = float(input("Insertar medida altura triangulo: "))
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    mostrar_area_triangulo(area_triangulo)

if __name__ == "__main__":
    ejecutar_calculos()