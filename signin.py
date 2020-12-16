<FlatButton@ButtonBehavior+Label>:
	font_size: 16

<SigninWindow>:
	id: main_win
	orientation: "vertical"
	spacing: 10
	space_x: self.size[0]/2.5
	
	BoxLayout:
		size_hint_y: None
		height: 50
		canvas:
			Color:
				rgba: (.06, .45, .45, 1)
			Rectangle:
				size: self.size
				pos: self.pos 	 
		Label:
			text: "Access Control"
			bold: True 
			size_hint_x: .9	
		FlatButton:
			text: "x"
			size_hint_x: .1
	BoxLayout:
		orientation: 'vertical'
		padding: main_win.space_x, 10 
		# spacing: 20
		BoxLayout:
			orientation: "vertical"
			spacing: 10
			size_hint_y: None
			height: 80
			Label:
				id: info
				text: ''
				markup: True
			TextInput:
				id: username_field
				hint_text: "Username"
				multiline: False 
				focus: True
				on_text_validate: pwd_field.focus = True
			TextInput:
				id: pwd_field
				hint_text: "Password"
				multiline: False
				password: True
				on_text_validate: root.validate_user()
		Label:
			id: sp
			size_hint_y: None
			height: 40
		Button:
			text: "Sign In"
			size_hint_y: None
			height: 40
			background_color: (.06,.45,.45, 1)
			background_normal: ''
			on_release: root.validate_user()
		Label:
			id: sp2
