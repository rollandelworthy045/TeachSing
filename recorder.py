import sounddevice as sd
import numpy as np
import wave

class Recorder:
    def __init__(self, file_path, duration=5, fs=44100):
        self.file_path = file_path
        self.duration = duration
        self.fs = fs

    def record(self):
        print("Recording...")
        recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2, dtype='int16')
        sd.wait()
        print("Recording finished")

        with wave.open(self.file_path, 'w') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(self.fs)
            wf.writeframes(recording.tobytes())
