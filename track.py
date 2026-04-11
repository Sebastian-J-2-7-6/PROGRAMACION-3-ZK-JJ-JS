TRACK_WIDTH = 780
TRACK_HEIGHT = 640
CAR_WIDTH = 80

class Track:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self):
        self.canvas.create_rectangle(0, 0, TRACK_WIDTH, TRACK_HEIGHT, outline="white", width=2)

        finish_x = TRACK_WIDTH - CAR_WIDTH - 10 + CAR_WIDTH // 2

        self.canvas.create_line(
            finish_x, 0, finish_x, TRACK_HEIGHT,
            fill="yellow", dash=(5, 3), width=3
        )

        self.canvas.create_text(
            finish_x + 5, 10,
            text="META",
            fill="yellow",
            anchor="nw",
            font=("Arial", 14, "bold")
        )

        for lane in range(10):
            y = 50 + lane * 60 - 10
            self.canvas.create_line(0, y, TRACK_WIDTH, y, fill="#333")