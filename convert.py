from pathlib import Path
import os
import ffmpeg

DIR_NAME = 'musicas'
OUTDIR = 'out'

music_dir = Path(DIR_NAME)
out_dir = Path(OUTDIR)

string_add = "Add Musics to this directory and try again: "
string_pls_add = "Please add musics in the diretory"


class MusicConvert():
    def __init__(self, lang):
        RES_CODE = {}
        if (lang == "PT_BR"):
            RES_CODE = {}
        else: 
            RES_CODE = {
                "addMusic": "Add Musics to this directory and try again: ",
                "plsAdd": ""
            }
        self.RES_CODE = RES_CODE
    def add_music_dir(self) -> int:
        if not music_dir.is_dir():
            os.mkdir(music_dir)
            print(string_add + f"<{music_dir.absolute()}>")
            return 1

    def convert_musics_to_mp3(self) -> int:
        if not music_dir.is_dir():
            print("Please add music dir")

        if len(os.listdir(music_dir)) == 0:
            print(string_pls_add) 
            return 2

        if not out_dir.is_dir():
            os.mkdir(out_dir)

        for root, dirs, files in os.walk(music_dir):
            for file in files:
                input = ffmpeg.input(os.path.join(root, file))
                extloc = file.rfind('.')
                if (extloc != -1):
                    outputname = file[:extloc]
                else: outputname = file
                print(outputname)
                out = ffmpeg.output(input, f"{os.path.join(out_dir, outputname)}.mp3")
                out = ffmpeg.overwrite_output(out)
                ffmpeg.run(out)