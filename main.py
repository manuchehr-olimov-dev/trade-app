import random

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.toolbar import MDBottomAppBar, MDActionBottomAppBarButton
from kivymd.uix.button import MDIconButton, MDFlatButton, MDTextButton

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivymd.uix.label import MDLabel

Builder.load_file("layout.kv")


class Main(Screen):
    random_number = StringProperty()

# меняем значения элемента
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(random.randint(1, 100))


class Deals(Screen):
    pass


class MainApp(MDApp):
    def build(self):

        self.sm = ScreenManager(transition=NoTransition())

        self.sm.add_widget(Main(name="Main"))
        self.sm.add_widget(Deals(name="Deals"))

        return self.sm

    def change_screen(self, scr):
        self.sm.current = scr

    def change_label_text(self):
        # self.root.ids.myLabel.text = "123"
        self.sm.ids.myLabel.text = "123"

if __name__ == "__main__":
    MainApp().run()