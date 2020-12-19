from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import re
from pymongo import MongoClient

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        client = MongoClient()
        self.db = client.silverpos
        self.stocks = self.db.stocks

    def update_purchases(self):
    	subject = self.ids.subj_inp.text
    	hw_list_cont = self.ids.hw_list
    	if subject == 'Philosophy':
    		details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top':1})
    		subject = Label(text=subject)
    		number = Label(text=self.ids.no_inp.text)
    		hw = Label(text=self.ids.hw_inp.text)
    		status = Label(text=self.ids.status_inp.text)
    		details.add_widget(subject)
    		details.add_widget(number)
    		details.add_widget(hw)
    		details.add_widget(status)
            




class OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__=="__main__":
    oa = OperatorApp()
    oa.run()
