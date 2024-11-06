import unittest




class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        func_run = Runner('walk')
        for i in range(10):
            func_run.walk()
        self.assertEqual(func_run.distance, 50)

    def test_run(self):
        func_run = Runner('run')
        for i in range(10):
            func_run.run()
        self.assertEqual(func_run.distance, 100)

    def test_challenge(self):
        func_run = Runner('walk_1')
        func_run1 = Runner('run_1')
        for i in range(10):
            func_run.walk()
            func_run1.run()
        self.assertNotEqual(func_run.distance, func_run1.distance)


if __name__ == "__main__":
    unittest.main()