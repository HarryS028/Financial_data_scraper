import kivy
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout

class MainWindow(Screen):

    def show_data(self, text):
        return text

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