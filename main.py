from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.animation import Animation

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LENOVO\CHIKI;'
                      'Database=forApp;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM forApp.dbo.listOfThings')

for row in cursor:
    print(row)

class MainView(ScrollView):

	desc_id = False
	desc_name = False
	desc_date = False

	q = '''
		SELECT 
		'''