import ffmpeg
import os
from pathlib import Path

DIR_NAME = 'musicas'
OUTDIR = 'out'
ERROR_CODES=["success", 
             f"Add musics into {DIR_NAME} and try again.", 
             "Please add musics.",
             "wrong file... please try the 'run' script."]

music_dir = Path(DIR_NAME)
out_dir = Path(OUTDIR)


def convert_musics_to_mp3() -> int:
    if not music_dir.is_dir():
        os.mkdir(music_dir)
        print(ERROR_CODES[1])
        return 1

    if len(os.listdir(music_dir)) == 0:
        print(ERROR_CODES[2]) 
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




def main() -> int:
    res = convert_musics_to_mp3()
    return res


if __name__ == "__main__":
    main()
else:
    print(ERROR_CODES[3])
    print(__name__)

