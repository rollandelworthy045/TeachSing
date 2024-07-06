import tkinter as tk
from tkinter import filedialog
from player import Player
from recorder import Recorder
from analyzer import Analyzer

class TeachSingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TeachSing")

        self.play_button = tk.Button(self.root, text="Play Song", command=self.play_song)
        self.play_button.pack()

        self.record_button = tk.Button(self.root, text="Record", command=self.record)
        self.record_button.pack()

        self.analyze_button = tk.Button(self.root, text="Analyze", command=self.analyze)
        self.analyze_button.pack()

    def play_song(self):
        file_path = filedialog.askopenfilename()
        player = Player(file_path)
        player.play()

    def record(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".wav")
        recorder = Recorder(file_path)
        recorder.record()

    def analyze(self):
        file_path = filedialog.askopenfilename()
        analyzer = Analyzer(file_path)
        tempo, beat_frames = analyzer.analyze()
        tk.messagebox.showinfo("Analysis Result", f"Tempo: {tempo}, Beat Frames: {beat_frames}")

    def run(self):
        self.root.mainloop()
