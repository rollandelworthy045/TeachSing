import librosa
import numpy as np

class Analyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze(self):
        y, sr = librosa.load(self.file_path)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        return tempo, beat_frames
