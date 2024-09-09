
def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto

if __name__=="__main__":
    multiplicando = float(input("Insertar multiplicando: "))
    multiplicador = float(input("Insertar multiplicador: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")

