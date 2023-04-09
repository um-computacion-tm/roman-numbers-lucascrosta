from parameterized import parameterized, parameterized_class
import unittest
from nrosromanos import decimal_to_roman
from nrosdecimales import roman_to_decimal
class MyTest(unittest.TestCase):
    @parameterized.expand([
        (1,"I"),
        (2,"II"),
        (3,"III"),
        (5,"V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
        (10,"X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
        (200, "CC"),
        (400, "CD"),
        (253, "CCLIII"),
        (1000, "M"),
        (523, "DXXIII"),
        (950, "CML"),

    ])
    def test(self, decimal, roman):
        self.assertEqual(decimal_to_roman(decimal),roman)

    @parameterized.expand([
        ("I",1),
        ("V",5),
        ("XIV",14),
        ("CMLXVII",967),
        ("M",1000),
        ("CCXXXV",235),
        ("DCXXII", 622),
        ("IX",9),
        ("CML", 950),
        ("DXXIII",523),
        ("L",50),
        ("CD",400),

    ])
    def test(self, roman, decimal):
        self.assertEqual(roman_to_decimal(roman),decimal)

if __name__ == '__main__':
    unittest.main()
