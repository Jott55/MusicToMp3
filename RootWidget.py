import subprocess
import threading
from pathlib import Path

from kivy.uix.widget import Widget

from convert import MusicConvert
import sys

_lang_code = {
    "button_add_music": "Add Musics",
    "button_convert_music": "Convert",
    "button_change_language": "Change language"
}

class RootWidget(Widget):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.language_list = ["en_US", "pt_BR"]
        self.lang = self.app.config.get("general", "language")

        self.lang_code = _lang_code
        self.set_language_code(self.lang)
        self.change_gui_language()
        self.MusicConvert = MusicConvert(self.lang)
        
    def add_music(self):
        self.MusicConvert.add_music_dir()
        open_folder(self.MusicConvert.music_dir.absolute())
    
    def progress_bar_callback(self, file_quantity: int, file_completed: int):
        self.ids.convert_progress_bar.max = file_quantity
        self.ids.convert_progress_bar.value = file_completed


    def convert_music(self):
        self.MusicConvert.set_options('-n')
        def new_thread_conversion():
            self.MusicConvert.convert_musics_to_mp3(self.progress_bar_callback)
            open_folder(self.MusicConvert.out_dir.absolute())
        threading.Thread(target=new_thread_conversion, daemon=True).start()

    def open_application_settings(self):
        self.app.open_settings()


    def toggle_application_language(self):        
        index = self.language_list.index(self.lang)
        if (index < len(self.language_list) - 1):
            self.lang = self.language_list[index+1]
        else:
            self.lang = self.language_list[0]

        self.app.set_language(self.lang)
        self.MusicConvert.set_language(self.lang)
        
        self.set_language_code(self.lang)
        self.change_gui_language()

    def set_language_code(self, lang):
        if lang == "pt_BR":
            self.lang_code["button_add_music"] = "Adicionar Musicas"
            self.lang_code["button_convert_music"] = "Converter"
            self.lang_code["button_change_language"] = "Portugues Brasileiro"
        else:
            self.lang_code["button_add_music"] = "Add Musics"
            self.lang_code["button_convert_music"] = "Convert"
            self.lang_code["button_change_language"] = "English USA"

    def change_gui_language(self):
        self.ids.button_add_music.text = self.lang_code["button_add_music"]
        self.ids.button_convert_music.text = self.lang_code["button_convert_music"]
        self.ids.button_change_language.text = self.lang_code["button_change_language"]

def open_folder(location):
    platform = sys.platform
    file_manager = ''
    
    if platform == "linux":
        file_manager = "xdg-open"
    elif platform == "win32":
        file_manager = "explorer"
    elif platform == "darwin":
        file_manager = "open"
    else:
        print("ERROR: your platform is not supported")
    
    subprocess.Popen([file_manager, location ])
    