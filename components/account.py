import json

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu



class Account(Screen):
    settings = open("user_settings.json", "r+")
    data = json.load(settings)

    dropdownStock = None

    dialogDeposit = None

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)

    def getUserName(self):
        if self.data['username']:
            return self.data["username"]

    def getCurrentStock(self):
        if self.data['currentStock']:
            return self.data["currentStock"]

    def open_stocks(self):

        menu_items = [
            {
                "id": "binance",
                "text": "binance",
                "on_release": lambda x="binance": self.menu_callback(x),
            },
            {
                "id": "bybit",
                "text": "bybit",
                "on_release": lambda x="bybit": self.menu_callback(x),
            }
        ]
        self.dropdownStock = MDDropdownMenu(
            caller=self.ids.stockButton, items=menu_items,
        )
        self.dropdownStock.open()

    def menu_callback(self, text_item):

        file = open("user_settings.json", "w+")
        self.data["currentStock"] = text_item
        json.dump(self.data, file)
        file.truncate()

        # change text of dropdown button
        self.ids.stockButton.text = text_item
        self.dropdownStock.dismiss()