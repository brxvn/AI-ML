import unittest

def suma(a,b):
    return a + b


class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1,num2)
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -7

        resultado = suma(num1,num2)
        self.assertEqual(resultado, -17)



if __name__ == "__main__":
    unittest.main()