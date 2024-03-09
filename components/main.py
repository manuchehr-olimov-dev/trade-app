from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class Main(Screen):
    random_number = StringProperty()
    default_text = "Hello World"

    # меняем значения элемента
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

    def change_text(self):
        pass

