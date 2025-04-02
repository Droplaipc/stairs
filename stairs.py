# /*
#  * Crea una función que dibuje una escalera según su número de escalones.
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
#  * - Si el número es negativo, será descendente de izquiera a derecha.
#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
#  *
#  * Ejemplo: 4
#  *         _
#  *       _|
#  *     _|
#  *   _|
#  * _|
#  *
#  */

def stairs(number_steps:int):
    if number_steps > 0:
        print(" " * number_steps * 2, "_", sep="")
        for i in range(number_steps):
            print(" " * (number_steps - i - 1) * 2, "_|", sep="")

    elif number_steps < 0:
        print("_", sep="")
        for i in range(abs(number_steps)):
            print(" " * (2 * i + 1), "|_", sep="")

    else:
        print("_")
