from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

import subprocess
import threading
from pathlib import Path

from convert import MusicConvert

class RootWidget(Widget):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        lang = self.app.config.get("general", "language")
        self.MusicConvert = MusicConvert(lang)
        
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

    def open_application_settings(self):
        self.app.open_settings()

    def toggle_application_language(self):
        self.app.set_language("pt_BR")
        self.MusicConvert.change_language("pt_BR")

class MainApp(App):

    def build(self):
        Builder.load_file('gui/RootWidget.kv')
        return RootWidget(self)
    
    def build_config(self, config):
        config.setdefaults("general", {"language": "en_US"})
    
    def set_language(self, lang = "en_US"):
        self.config.set("general", "language", lang)
        self.config.write()