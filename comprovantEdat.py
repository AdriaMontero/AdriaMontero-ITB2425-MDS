from datetime import datetime

# Solicitar la fecha de nacimiento
dia = int(input("Día? "))
mes = int(input("Mes? "))
any = int(input("Año? "))

# Obtener la fecha actual
hoy = datetime.now()
actual = hoy.year
diactual = hoy.day
mesactual = hoy.month

# Validar la entrada
if any > actual:
    print("Año incorrecte")
if mes > 12 or mes < 1:
    print("Mes incorrecte")
if dia > 31 or dia < 1:
    print("Día incorrecte")
else:
    # Calcular la edad
    edad = actual - any

    # Ajustar si el cumpleaños aún no ha ocurrido este año
    if (mesactual < mes) or (mesactual == mes and diactual < dia):
        edad -= 1

    print(f"Tens {edad} anys.")
