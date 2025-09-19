from kivy.app import App
from kivy.lang import Builder

root = Builder.load_file('MainGui.kv')



class Gui(App):
    def build(self):
        return root