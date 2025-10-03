from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
import subprocess
from pathlib import Path

from convert import MusicConvert


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.MusicConvert = MusicConvert("EN_US")

    def add_music(self):
        self.MusicConvert.add_music_dir()
        subprocess.Popen(['xdg-open', Path.cwd().joinpath('musicas') ])
        return 0
    def convert_music(self):
        self.MusicConvert.convert_musics_to_mp3()
        pass


class MainApp(App):

    def build(self):
        Builder.load_file('gui/RootWidget.kv')
        return RootWidget()