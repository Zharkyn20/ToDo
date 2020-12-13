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

import MySQLdb

class MainView(ScrollView):
  desc_id = False
  desc_name = False
  desc_date = False

  q = '''
    SELECT * FROM todo.list_of_things
    ORDER BY list_of_things.id
  '''

  con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='aruna2010', db='todo')
  cur = con.cursor()
  cur.execute('SET NAMES utf8')

  def add_record(self, vals):
    alert = 0
    for val in vals:
      if len(val) == 0:
        alert = 1
        break

    if alert == 0:
      q = self.query("INSERT INTO todo.list_of_things (id, checklist, date%time, status) VALUES ('%d', '%s', '%d', '%s')"
        %(int(vals[0]), str(vals[1]), int(vals[2]), str(vals[3])))
      self.fill(self.db_data(q))
      self.qchange()
    else:  
      pass

  def del_record(self, vals):
    date_validation = False
    i = 0
    for val in vals:
      if len(val) > 0:
        break
      i += 1
    if i == 0:
      q = self.query("DELETE FROM todo.list_of_things WHERE checklist = '%s'" %str(vals[i]))
      self.fill(self.db_data(q))
      self.qchange()
    elif i == 1:
      try:
        parts = str(vals[i]).split("-")
        string = ''
        for item in parts:
          string += item
        if len(string) == 8:
          date_validation = True
        else:
          pass  
      except:
        pass
      if date_validation is True:
        q = self.query("DELETE FROM todo.list_of_things WHERE founded = '%s'" %str(vals[i]))
        self.fill(self.db_data(q))
        self.qchange()
      else:  
        pass
    else:
      pass
      
  def qcahnge(self):
    if self.desc_id is False:
      q = self.query('''
      SELECT * FROM todo.list_of_things
      ORDER BY todo.list_of_tjings.id'''          
              )
      self.desc_id = True
    else:
      q = self.query('''
        SELECT * FROM todo.list_of_things
        ORDER BY id'''
              )
      self.desc_id = False

    self.fill(self.db_data(q))

  def qchange2(self):
    if self.desc_name = False:
      pass
