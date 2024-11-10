import  unittest




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
    @classmethod
    def setUpClass(cls):
        cls.all_results = []


    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andy = Runner('Андрей',9)
        self.nick = Runner('Николай', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print('{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}')


    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Николай")

    def test_andy_nick(self):
        tournament = Tournament(90, self.andy, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Николай")

    def test_usain_andy_nick(self):
        tournament = Tournament(90, self.andy, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Николай")


if __name__ == '__main__':
    unittest.main()


