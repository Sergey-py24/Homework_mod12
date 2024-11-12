import unittest
import tests_12_3



testingST = unittest.TestSuite()
testingST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testingST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testingST)