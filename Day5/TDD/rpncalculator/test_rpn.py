import unittest
from rpn import RPNCalculator, RPNError

class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = RPNCalculator()

    def test_simpleAddition(self):
        rpnMathExpression = "10 15 +"
        actualResult = self.calc.evaluate( rpnMathExpression )
        expectedResult = 25
        self.assertEqual( actualResult, expectedResult )

    def test_simpleSubtraction(self):
        rpnMathExpression = "100 15 -"
        actualResult = self.calc.evaluate( rpnMathExpression )
        expectedResult = 85
        self.assertEqual( actualResult, expectedResult )

    def test_simpleMultiplication(self):
        rpnMathExpression = "100 15 *"
        actualResult = self.calc.evaluate( rpnMathExpression )
        expectedResult = 1500
        self.assertEqual( actualResult, expectedResult )

    def test_simpleDivision(self):
        rpnMathExpression = "100 10 /"
        actualResult = self.calc.evaluate( rpnMathExpression )
        expectedResult = 10
        self.assertEqual( actualResult, expectedResult )

    def test_complexRPNMathExpression(self):
        rpnMathExpression = "10 3 * 100 20 / -"
        actualResult = self.calc.evaluate( rpnMathExpression )
        expectedResult = 25 
        self.assertEqual( actualResult, expectedResult )

if __name__ == "__main__":
    unittest.main()
