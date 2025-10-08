from convert import MusicConvert

mc = MusicConvert("en_US")

print(mc.LANG_CODE)

mc = MusicConvert("pt_BR")

print(mc.LANG_CODE)


mc.add_music_dir()
mc.convert_musics_to_mp3()