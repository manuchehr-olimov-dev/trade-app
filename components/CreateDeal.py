import json

import psycopg2
from kivy.uix.screenmanager import Screen
from kivymd import app
from kivymd.material_resources import dp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.pickers import MDDatePicker


class CreateDeal(Screen):
    settings = open("user_settings.json", "r+")
    data = json.load(settings)
    dropdownTicket = None

    okDialog = None

    def __init__(self, **kwargs):
        super(CreateDeal, self).__init__(**kwargs)

    def openTickets(self):
        tickets = [
            {
                "id": "btc",
                "text": "BTC",
                "on_release": lambda x="BTC": self.menu_callback(x),
            },
            {
                "id": "ton",
                "text": "TON",
                "on_release": lambda x="TON": self.menu_callback(x),
            }
        ]
        self.dropdownTicket = MDDropdownMenu(
            caller=self.ids.ticketButton, items=tickets,
        )
        self.dropdownTicket.open()

    def menu_callback(self, text_item):
        # change text of dropdown button
        self.ids.ticketButton.text = text_item
        self.dropdownTicket.dismiss()

    def show_date_picker(self):
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_save_date)
        date_picker.open()

    def on_save_date(self, instance, value, date_range):
        self.ids.dateButton.text = str(value)
        print(value)

    def print_deposit(self, text):
        print(text)

    def print_percentage_of_risk(self, text):
        print(text)

    def create_deal(self):
        date = self.ids.dateButton.text
        ticket = self.ids.ticketButton.text
        user_id = 1
        deposit = float(self.ids.deposit.text)

        if self.ids.percentageOfRisk.text == "":
            percentage_of_risk = self.data["percentageOfRiskOfDeposit"]
        else:
            percentage_of_risk = float(self.ids.percentageOfRisk.text)

        entry_price = float(self.ids.entryPrice.text)
        stop_price = float(self.ids.stopPrice.text)

        amount_of_money_that_i_can_buy = (deposit * percentage_of_risk / 100) / abs(stop_price - entry_price)

        stop_in_usdt = abs(stop_price - entry_price) * amount_of_money_that_i_can_buy

        if stop_price > entry_price:
            position_direct = "short"
        else:
            position_direct = "long"

        smart_stop = ((entry_price - stop_price) * amount_of_money_that_i_can_buy) / (3000 + stop_price)
        notion = str(self.ids.notion.text)
        result = "Nice"

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
        query = f"""
            INSERT INTO deals (
                ticket,
                user_id,
                date,
                deposit,
                percentage_of_risk, 
                entry_price,
                stop_price,
                amount_of_coins_for_entry,
                stop_in_usdt,
                position_direct,
                notion,
                result,
                smart_stop
            ) VALUES (
                '{ticket}',
                {user_id},
                '{date}',
                {deposit},
                {percentage_of_risk},
                {entry_price},
                {stop_price},
                {amount_of_money_that_i_can_buy},
                {stop_in_usdt},
                '{position_direct}',
                '{notion}',
                '{result}',
                {smart_stop}
            )

        """

        cursor.execute(query)
        connection.commit()
        c = cursor.rowcount

        if not self.okDialog:
            self.okDialog = MDDialog(
                title="Pretty Neat, Right?!",
                text="Все прошло успешно!",
                buttons=[

                    MDRectangleFlatButton(
                        text="Ok", on_release=self.closeOkDialog
                    ),
                ],
            )
        self.okDialog.open()
        print(c, "OK")

    def closeOkDialog(self, obj):
        self.okDialog.dismiss()



