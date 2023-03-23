import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return "I" * decimal
    elif decimal == 5:
        return "V"
    elif decimal > 5 and decimal < 9: 
        return "V" + "I"*(decimal-5)
    elif decimal == 50:
        return "L"
    elif decimal == 100:
        return "C"
    elif decimal == 500:
        return "D"
    elif decimal == 1000:
        return "M"
    elif decimal == 10:
        return "X"
    elif decimal > 10 and decimal < 14:
        return "X" + "I"*(decimal-10)
    elif decimal > 100 and decimal < 400:
        return "C"*(decimal//100)


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

    def test_50(self):
        self.assertEqual(decimal_to_roman(50), "L")

    def test_100(self):
        self.assertEqual(decimal_to_roman(100), "C")

    def test_500(self):
        self.assertEqual(decimal_to_roman(500), "D")
    
    def test_1000(self):
        self.assertEqual(decimal_to_roman(1000), "M")

    def test_200(self):
        self.assertEqual(decimal_to_roman(200), "CC")


if __name__ == "__main__":
    unittest.main()