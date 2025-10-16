from M2Mp3 import M2Mp3
from kivy.config import Config

def start_kivy() -> None:
    M2Mp3().run()

def main() -> int:

    Config.set('graphics', 'width', '640')
    Config.set('graphics', 'height', '480')

    start_kivy()
    return 0
  
if __name__ == "__main__":
    main()
else:
    print("wrong file")
    print(__name__)