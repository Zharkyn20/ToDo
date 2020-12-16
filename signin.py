from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image
from kivy.core.window import Window

Window.size=(360,640)

class SigninWindow(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def validate_user(self):
		user = self.ids.username_field
		pwd = self.ids.pwd_field
		info = self.ids.info

		uname = user.text
		passw = pwd.text

		if uname == "" or passw == '':
			info.text ='[color=#FF0000]username and/ or password required'
		else:
			if uname == 'admin' and passw == 'admin':
				print ('Logged In successfully!!!')

class FullImage(Image):
	def build(self):
		return Image(source='img.jpg')

class SigninApp(App):
	def build(self):
		return SigninWindow()
		return FullImage()

if __name__=="__main__":
	sa = SigninApp()
	sa.run()
