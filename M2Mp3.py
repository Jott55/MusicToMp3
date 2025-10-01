import kivy

from kivy.app import App
from kivy.lang import Builder
root = Builder.load_file('gui/m2mp3.kv')

class M2Mp3App(App):
    def build(self):
        return root