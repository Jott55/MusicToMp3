from pathlib import Path
import os
import ffmpeg

class MusicConvert():
    def __init__(self, lang = "en_US"):
        LANG_CODE = {
            "addMusic": "Add Musics to this directory and try again: ",
            "plsAdd": "Please add musics in the diretory",
            "musicdir": "songs",
            "outdir": "out"
        }

        if (lang == "pt_BR"):
            LANG_CODE["addMusic"] = "Adicione mas musicas no diretorio e tente de novo: "
            LANG_CODE["plsAdd"] = "Por favor adicione as musicas no diretorio"
            LANG_CODE["musicdir"] = "musicas"
            LANG_CODE["outdir"] = "saida"

        self.LANG_CODE = LANG_CODE

        self.music_dir = Path(self.LANG_CODE["musicdir"])
        self.outdir = Path(self.LANG_CODE["outdir"])
    def add_music_dir(self) -> int:
        if not self.music_dir.is_dir():
            os.mkdir(self.music_dir)
            print(self.LANG_CODE["addMusic"] + f"<{self.music_dir.absolute()}>")
            return 1

    def convert_musics_to_mp3(self) -> int:
        if not self.music_dir.is_dir():
            print(self.LANG_CODE["plsAdd"])

        if len(os.listdir(self.music_dir)) == 0:
            print(self.LANG_CODE["plsAdd"]) 
            return 2

        if not self.out_dir.is_dir():
            os.mkdir(self.out_dir)

        for root, dirs, files in os.walk(self.music_dir):
            for file in files:
                input = ffmpeg.input(os.path.join(root, file))
                extloc = file.rfind('.')
                if (extloc != -1):
                    outputname = file[:extloc]
                else: outputname = file
                print(outputname)
                out = ffmpeg.output(input, f"{os.path.join(self.out_dir, outputname)}.mp3")
                out = ffmpeg.overwrite_output(out)
                ffmpeg.run(out)