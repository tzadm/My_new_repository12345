import unittest
import Runner_tests
import Tournament_tests

run_tour_tests = unittest.TestSuite()
run_tour_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(Runner_tests.RunnerTest))
run_tour_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(Tournament_tests.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_tests)