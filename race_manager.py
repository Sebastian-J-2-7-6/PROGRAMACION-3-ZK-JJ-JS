from car import Car

CAR_COLORS = [
    "red","orange","yellow","green","cyan",
    "blue","magenta","white","lightgreen","pink"
]

class RaceManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cars = [Car(canvas, i, CAR_COLORS[i], i) for i in range(10)]
        self.running = False
        self.rounds = 1
        self.current_round = 0

    def start(self, rounds):
        self.running = True
        self.rounds = rounds
        self.current_round = 1

        for car in self.cars:
            car.reset()

    def reset(self):
        self.running = False
        self.current_round = 0
        for car in self.cars:
            car.reset()

    def update(self, dt):
        if not self.running:
            return

        all_finished = True

        for car in self.cars:
            if not car.finished:
                all_finished = False
                car.move(dt)

        if all_finished:
            self.next_round()

    def next_round(self):
        if self.current_round < self.rounds:
            self.current_round += 1
            for car in self.cars:
                car.distance = 0
                car.lap_time = 0
                car.finished = False
        else:
            self.running = False

    def get_ranking(self):
        return sorted(self.cars, key=lambda c: c.total_time)