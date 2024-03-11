import json

import psycopg2
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDBottomAppBar, MDActionBottomAppBarButton
from kivymd.uix.button import MDIconButton, MDFlatButton, MDTextButton
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import ThreeLineListItem


class Deals(Screen):
    settings = open("user_settings.json", "r+")
    data = json.load(settings)

    def __init__(self, **kwargs):
        super(Deals, self).__init__(**kwargs)

    def show_deals(self):
        self.ids.dealsContainer.clear_widgets()
        connection = psycopg2.connect(
            database="trader-db",
            user="postgres",
            password="1",
            host="localhost",
            port=5432
        )

        if (connection):
            print("ok")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from deals"

        cursor.execute(postgreSQL_select_Query)
        deals = cursor.fetchall()

        print("Вывод каждой строки и ее столбцов")
        for deal in deals:
            self.ids.dealsContainer.add_widget(
                ThreeLineListItem(
                    text=f"ID: {deal[0]}",
                    secondary_text=f"Тикет: {deal[1]}",
                    tertiary_text=f"Дата: {deal[3]}"
                )
            )

