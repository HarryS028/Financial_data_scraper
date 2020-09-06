import kivy
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class FileWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file("main.kv")
        return kv

if __name__ == "__main__":
    MyApp().run()