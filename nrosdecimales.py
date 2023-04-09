def roman_to_decimal(roman):

    valores = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    decimal = 0

    valor_ant = 0

    for i in roman:

        valor_act = valores[i]

        if valor_act > valor_ant:

            decimal += valor_act - 2*valor_ant
        
        else:

            decimal += valor_act

        valor_ant = valor_act

    return decimal

