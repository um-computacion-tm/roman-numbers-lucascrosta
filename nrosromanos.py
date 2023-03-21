import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return "I" * decimal
    elif decimal == 5:
        return "V"
    elif decimal > 5 and decimal < 9: 
        return "V" + "I"*(decimal-5)
    else:
        return "X"

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")

    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")

    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")

    def test_2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, "II")

    def test_3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, "III")

    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, "VI")

    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, "VII")

    def test_8(self):
        self.assertEqual(decimal_to_roman(8), "VIII")


if __name__ == "__main__":
    unittest.main()