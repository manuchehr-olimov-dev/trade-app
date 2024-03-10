import json
from kivy.uix.screenmanager import Screen
from kivymd import app
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel


class ChangeDefaultSettings(Screen):
    settings = open("user_settings.json", "r+")
    data = json.load(settings)

    okDialog = None

    def __init__(self, **kwargs):
        super(ChangeDefaultSettings, self).__init__(**kwargs)

    def getCurrentDeposit(self):
        if self.data['deposit']:
            return f"Депозит на данный момент: {self.data["deposit"]}%"

    def getCurrentPercentageOfRiskOfDeposit(self):
        if self.data['percentageOfRiskOfDeposit']:
            return f"На данный момент: {self.data["percentageOfRiskOfDeposit"]}%"

    def getCurrentSmartStopPercentage(self):
        if self.data['smartStopPercentage']:
            return f"На данный момент: {self.data["smartStopPercentage"]}%"

    def changeProperties(self):
        file = open("user_settings.json", "w+")

        # Check values from text fields
        if self.ids.deposit.text != "":
            self.ids.deposit.hint_text = f"Депозит на данный момент: {self.ids.deposit.text}%"
            self.data["deposit"] = int(self.ids.deposit.text)

        if self.ids.percentageOfRiskOfDeposit.text != "":
            self.ids.percentageOfRiskOfDeposit.hint_text = f"Депозит на данный момент: {self.ids.percentageOfRiskOfDeposit.text}%"
            self.data["percentageOfRiskOfDeposit"] = int(self.ids.percentageOfRiskOfDeposit.text)

        if self.ids.smartStopPercentage.text != "":
            self.ids.smartStopPercentage.hint_text = f"Депозит на данный момент: {self.ids.smartStopPercentage.text}%"
            self.data["smartStopPercentage"] = int(self.ids.smartStopPercentage.text)


        json.dump(self.data, file)

        result = file.truncate()

        if result:
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

        else:
            if not self.okDialog:
                self.okDialog = MDDialog(
                    title="Pretty Neat, Right?!",
                    text="Что то пошло не так! Попробуйте зайти чуть позже.",
                    buttons=[

                        MDRectangleFlatButton(
                            text="Ok", on_release=self.closeOkDialog
                        ),
                    ],
                )
        self.okDialog.open()

    def closeOkDialog(self, obj):
        self.okDialog.dismiss()
