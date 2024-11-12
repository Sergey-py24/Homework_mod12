
import unittest



class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):
    is_frosen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andy = Runner('Андрей',9)
        self.nick = Runner('Николай', 3)


    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print('{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}')


    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Николай")

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_andy_nick(self):
        tournament = Tournament(90, self.andy, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Николай")

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_usain_andy_nick(self):
        tournament = Tournament(90, self.nick, self.usain, self.andy)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Николай")


class RunnerTest(unittest.TestCase):
    is_frosen = False

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        func_run = Runner('walk')
        for i in range(10):
            func_run.walk()
        self.assertEqual(func_run.distance, 50)

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        func_run = Runner('run')
        for i in range(10):
            func_run.run()
        self.assertEqual(func_run.distance, 100)

    @unittest.skipIf(is_frosen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        func_run = Runner('walk_1')
        func_run1 = Runner('run_1')
        for i in range(10):
            func_run.walk()
            func_run1.run()
        self.assertNotEqual(func_run.distance, func_run1.distance)


if __name__ == '__main__':
    unittest.main(verbosity=2)


