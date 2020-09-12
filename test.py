from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout


class MyFileChooser(FileChooserListView):

    def on_submit(*args):
        print(args[1][0])


class MyLayout(BoxLayout):

    def __init__(self,**kwargs):
        super(MyLayout,self).__init__(**kwargs)
        # filter added. Since windows will throw error on sys files
        self.fclv = MyFileChooser(filters= [lambda folder, filename: not filename.endswith('.sys')])
        self.add_widget(self.fclv)


class MyApp(App):

    def build(self):
        return MyLayout()


MyApp().run()