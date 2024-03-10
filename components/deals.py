import json

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDBottomAppBar, MDActionBottomAppBarButton
from kivymd.uix.button import MDIconButton, MDFlatButton, MDTextButton
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import ThreeLineListItem


class Deals(Screen):
    settings = open("user_settings.json", "r+")
    data = json.load(settings)

    def __init__(self, **kwargs):
        super(Deals, self).__init__(**kwargs)

    def on_start(self):
        for _ in range(39):
            self.root.ids.container.add_widget(
                OneLineListItem(
                    text=f"This is elem #{_}"
                )
            )
