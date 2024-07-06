import simpleaudio as sa

class Player:
    def __init__(self, file_path):
        self.file_path = file_path

    def play(self):
        wave_obj = sa.WaveObject.from_wave_file(self.file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
