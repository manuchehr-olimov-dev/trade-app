from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDBottomAppBar, MDActionBottomAppBarButton
from kivymd.uix.button import MDIconButton, MDFlatButton, MDTextButton
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.config import Config
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from components.ChangeDefaultSettings import ChangeDefaultSettings

from components.account import Account
from components.main import Main
from components.deals import Deals

Config.set('graphics', 'width', 480)
Config.set('graphics', 'height', 600)
Config.set('graphics', 'resizable', False)
Config.write()

Builder.load_file("layout.kv")





# MainApp
class MainApp(MDApp):
    def build(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        self.theme_cls.primary_palette = "Indigo"

        self.sm = ScreenManager(transition=NoTransition())

        self.sm.add_widget(Main(name="Main"))
        self.sm.add_widget(Deals(name="Deals"))
        self.sm.add_widget(Account(name="Account"))
        self.sm.add_widget(ChangeDefaultSettings(name="ChangeDefaultSettings"))

        return self.sm

    def change_screen(self, scr):
        self.sm.current = scr


if __name__ == "__main__":
    MainApp().run()
