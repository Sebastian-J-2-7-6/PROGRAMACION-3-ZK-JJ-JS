import tkinter as tk
from tkinter import ttk
from race_manager import RaceManager
from track import Track

TRACK_WIDTH = 780
TRACK_HEIGHT = 640


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de competencia automovilística")

        self.canvas = tk.Canvas(root, width=TRACK_WIDTH, height=TRACK_HEIGHT, bg="black")
        self.canvas.pack(side="left")

        self.panel = tk.Frame(root, bg="#111", width=350)
        self.panel.pack(side="right", fill="y")

        self.track = Track(self.canvas)
        self.track.draw()

        self.manager = RaceManager(self.canvas)

        self.rounds = tk.IntVar(value=3)
        self.speed = tk.DoubleVar(value=1.0)
        self.bet = tk.IntVar(value=1)

        self.build_controls()
        self.loop()

    def build_controls(self):
        tk.Label(self.panel, text="Panel de control", fg="white", bg="#111",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.panel, text="Apuesta por un auto:", fg="white", bg="#111").pack()
        combo = ttk.Combobox(self.panel, values=[f"Auto {i+1}" for i in range(10)])
        combo.current(0)
        combo.pack()

        def select_bet(event):
            self.bet.set(int(combo.get().split()[1]))

        combo.bind("<<ComboboxSelected>>", select_bet)

        tk.Label(self.panel, text="Número de vueltas:", fg="white", bg="#111").pack(pady=10)
        tk.Spinbox(self.panel, from_=1, to=10, textvariable=self.rounds).pack()

        tk.Label(self.panel, text="Velocidad:", fg="white", bg="#111").pack(pady=10)
        tk.Scale(self.panel, from_=0.5, to=3, resolution=0.1,
                 orient="horizontal", variable=self.speed).pack()

        tk.Button(self.panel, text="Iniciar Carrera", bg="green", fg="white",
                  command=self.start).pack(pady=10)

        tk.Button(self.panel, text="Reiniciar", bg="gray", fg="white",
                  command=self.reset).pack(pady=5)

        self.status = tk.Label(self.panel, text="Preparado.", fg="white", bg="#111")
        self.status.pack(pady=10)

        self.text = tk.Text(self.panel, height=15, bg="#111", fg="white")
        self.text.pack()

    def start(self):
        self.manager.start(self.rounds.get())
        self.status.config(text=f"Apostaste por Auto {self.bet.get()}")

    def reset(self):
        self.manager.reset()
        self.status.config(text="Reiniciado")

    def loop(self):
        self.manager.update(0.05 * self.speed.get())
        self.update_ranking()

        if not self.manager.running and self.manager.current_round > 0:
            ranking = self.manager.get_ranking()
            winner = ranking[0].index + 1

            if winner == self.bet.get():
                self.status.config(text=f"Ganó Auto {winner} ¡GANASTE!")
            else:
                self.status.config(text=f"Ganó Auto {winner} - Perdiste")

        self.root.after(50, self.loop)

    def update_ranking(self):
        ranking = self.manager.get_ranking()

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, "Pos  Auto  Tiempo\n")
        self.text.insert(tk.END, "--------------------\n")

        for i, car in enumerate(ranking):
            linea = f"{i+1}.  Auto {car.index+1}   {car.total_time:.2f}s\n"
            self.text.insert(tk.END, linea)