# Задача "Проверка на выносливость":
import unittest
from module_12_0 import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Mike')
        for walk in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner_2 = Runner('Bob')
        for run in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)
    def test_challenge(self):
        runner_3 = Runner('Maks')
        runner_4 = Runner('Billy')
        for run in range(10):
            runner_3.run()
        for walk in range(10):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == "__main__":
    unittest.main()
