from convert import MusicConvert

mc = MusicConvert("en_US")

print(mc.lang_code)

mc = MusicConvert("pt_BR")

print(mc.lang_code)


mc.add_music_dir()
mc.convert_musics_to_mp3()