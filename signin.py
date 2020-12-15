from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
	
class SigninWindow(BoxLayout):
	pass 

class FullImage(Image):
    pass

class SigninApp(App):
	def build(self):
		return SigninWindow()
		return FullImage()

if __name__=="__main__":
	sa = SigninApp()
	sa.run()

		
