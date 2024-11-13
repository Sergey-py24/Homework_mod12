import logging
import unittest




class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                            format='%(levelname)s | %(message)s')

    def test_walk(self):
        try:
            func_run = Runner(name='Usain', speed=-10)
            for i in range(10):
                func_run.walk()
                self.assertEqual(func_run.distance, 50)
        except:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        logging.info('Тест "test_walk" выполнен успешно')

    def test_run(self):
        try:
            func_run = Runner(name=99, speed=9)
            for i in range(10):
                func_run.run()
                self.assertEqual(func_run.distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        logging.info('Тест "test_run" выполнен успешно')


    def test_challenge(self):
        func_run = Runner('walk_1')
        func_run1 = Runner('run_1')
        for i in range(10):
            func_run.walk()
            func_run1.run()
        self.assertNotEqual(func_run.distance, func_run1.distance)


if __name__ == '__main__':
    unittest.main(verbosity=2)
