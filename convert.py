from pathlib import Path
import os
import subprocess

_lang_code = {
    "addMusic": "Add Musics to this directory and try again: ",
    "plsAdd": "Please add musics in the diretory",
    "musicDir": "songs",
    "outDir": "out",
    "directoryAlready": "Directory already created"
}

class MusicConvert():
    def __init__(self, lang = "en_US"):
        self.lang_code = {}
        self.set_language(lang)
        
    def set_language(self, language = "en_US"):
        if (language == "pt_BR"):
            self.lang_code["addMusic"] = "Adicione mas musicas no diretorio e tente de novo: "
            self.lang_code["plsAdd"] = "Por favor adicione as musicas no diretorio"
            self.lang_code["musicDir"] = "musicas"
            self.lang_code["outDir"] = "saida"
            self.lang_code["directoryAlready"] = "diretorio ja foi criado"
        else:
            self.lang_code["addMusic"] = "Add Musics to this directory and try again: "
            self.lang_code["plsAdd"] = "Please add musics in the diretory"
            self.lang_code["musicDir"] = "songs"
            self.lang_code["outDir"] = "out"
            self.lang_code["directoryAlready"] = "Directory already created"

        self.music_dir = Path(self.lang_code["musicDir"])
        self.out_dir = Path(self.lang_code["outDir"])

    def add_music_dir(self) -> int:
        if not self.music_dir.is_dir():
            os.mkdir(self.music_dir)
            print(self.lang_code["addMusic"] + f"<{self.music_dir.absolute()}>")
            return 1
        else:
            print(self.lang_code["directoryAlready"])
            
    def convert_musics_to_mp3(self, files_completed_callback = None, files_quantity_callback = None ) -> int:
        if not self.music_dir.is_dir():
            print(self.lang_code["plsAdd"])

        if len(os.listdir(self.music_dir)) == 0:
            print(self.lang_code["plsAdd"]) 
            return 2

        if not self.out_dir.is_dir():
            os.mkdir(self.out_dir)

        options_verbose =  {
            "no_overwrite": "-n"
        }
        options = ' '.join(options_verbose.values())
        
        files_completed = 0

        for root, dirs, files in os.walk(self.music_dir):
            if (files_quantity_callback):
                files_quantity_callback(len(files))
            for file in files:
                extension_location = file.rfind('.')
                if (extension_location != -1):
                    output_file_name = file[:extension_location]
                else: output_file_name = file
                print(output_file_name)
        
                input_path = os.path.join(root, file)
                print(f"ffmpeg -i '{input_path}' " + options + f" '{os.path.join(self.out_dir, output_file_name)}.mp3'")
                subprocess.Popen(f"ffmpeg -i '{input_path}' " + options + f" '{os.path.join(self.out_dir, output_file_name)}.mp3'", shell=True).wait()
                files_completed+=1
                if files_completed_callback:
                    files_completed_callback(files_completed)
