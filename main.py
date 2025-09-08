import ffmpeg
import os
from pathlib import Path

DIR_NAME = 'musicas'
OUTDIR = 'out'

music_dir = Path(DIR_NAME)
out_dir = Path(OUTDIR)
def main():
    if not music_dir.is_dir():
        os.mkdir(music_dir)
        print(f"Adicione as musicas nesse <{music_dir.absolute()}> diretorio")
        exit(1)

    if len(os.listdir(music_dir)) == 0:
        print(f"Por favor adicione as musicas") 
        exit(1)

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


if __name__ == "__main__":
    main()
else:
    print("wrong file")
    print(__name__)

