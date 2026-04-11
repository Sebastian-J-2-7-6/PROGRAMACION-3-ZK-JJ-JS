import random
import tkinter as tk

CAR_WIDTH = 80
CAR_HEIGHT = 40
START_X = 10
FINISH_X = 780 - CAR_WIDTH - 10


class Car:
    def __init__(self, canvas, lane, color, index):
        self.canvas = canvas
        self.lane = lane
        self.color = color
        self.index = index

        self.distance = 0
        self.speed = 0
        self.total_time = 0
        self.lap_time = 0
        self.finished = False

        self.image = self.create_image()

        self.sprite = canvas.create_image(
            START_X, self.y_pos(), anchor="nw", image=self.image
        )

        # NOMBRE DEL AUTO
        self.label = canvas.create_text(
            START_X + 10,
            self.y_pos() + CAR_HEIGHT + 5,
            text=f"Auto {index + 1}",
            fill="white",
            anchor="w",
            font=("Arial", 9, "bold"),
        )

    def y_pos(self):
        return 50 + self.lane * 60

    def create_image(self):
        img = tk.PhotoImage(width=CAR_WIDTH, height=CAR_HEIGHT)
        for x in range(CAR_WIDTH):
            for y in range(CAR_HEIGHT):
                color = self.color if (5 < x < CAR_WIDTH - 5 and 5 < y < CAR_HEIGHT - 5) else "black"
                img.put(color, (x, y))
        return img

    def reset(self):
        self.distance = 0
        self.speed = random.uniform(5, 9)
        self.total_time = 0
        self.lap_time = 0
        self.finished = False
        self.update_position()

    def move(self, dt):
        if self.finished:
            return

        self.distance += self.speed * dt
        self.lap_time += dt

        if self.distance >= FINISH_X - START_X:
            self.distance = FINISH_X - START_X
            self.finished = True
            self.total_time += self.lap_time

        self.update_position()

    def update_position(self):
        x = START_X + self.distance
        y = self.y_pos()

        self.canvas.coords(self.sprite, x, y)
        self.canvas.coords(self.label, x + 10, y + CAR_HEIGHT + 5)
