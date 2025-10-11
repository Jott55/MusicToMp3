from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
import subprocess
from pathlib import Path

from convert import MusicConvert

from kivy.clock import Clock
import threading
class RootWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.MusicConvert = MusicConvert("en_US")
        
    def add_music(self):
        self.MusicConvert.add_music_dir()
        subprocess.Popen(['xdg-open', Path.cwd().joinpath(self.MusicConvert.music_dir) ])
        return 0
    
    def set_progress_bar_max(self, max):
        self.ids.convert_progress_bar.max = max 
    def set_progress_bar_value(self, value):
        self.ids.convert_progress_bar.value = value

    def convert_music(self):
        self.set_progress_bar_value(0)
        def new_thread_conversion():
            self.MusicConvert.convert_musics_to_mp3(self.set_progress_bar_value, self.set_progress_bar_max)
            subprocess.Popen(['xdg-open', Path.cwd().joinpath(self.MusicConvert.out_dir) ])
        threading.Thread(target=new_thread_conversion, daemon=True).start()

class MainApp(App):

    def build(self):
        Builder.load_file('gui/RootWidget.kv')
        return RootWidget()