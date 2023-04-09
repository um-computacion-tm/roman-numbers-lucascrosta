

def decimal_to_roman(decimal):

    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    conv = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    i = 0
    
    while decimal > 0:
        for _ in range(decimal // numeros[i]):
            roman += conv[i]
            decimal -= numeros[i]

        i += 1

    return roman

