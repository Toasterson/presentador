from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os


class ScreenManagement(ScreenManager):
    pass


class FileSelector(Screen):
    def load(self, path, filename):
        pass


class MainScreen(Screen):
    pass


class Presentation(Screen):
    pass


presentation = Builder.load_file("main.kv")


class Presentador(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    Presentador().run()
