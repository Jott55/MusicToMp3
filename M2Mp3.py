from kivy.app import App
from kivy.lang import Builder

from RootWidget import RootWidget


class M2Mp3(App):

    def build(self):
        Builder.load_file('gui/RootWidget.kv')
        return RootWidget(self)
    
    def build_config(self, config):
        config.setdefaults("general", {"language": "en_US"})
    
    def set_language(self, lang = "en_US"):
        self.config.set("general", "language", lang)
        self.config.write()