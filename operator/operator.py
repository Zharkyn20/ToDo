<FlatButton@ButtonBehavior+Label>:
    font_size: 14

<OperatorWindow>:
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (.83,.83,.83, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        id: header
        size_hint_y: None
        height: 40
        canvas.before:
            Color:
                rgba: (.30, .18, .48, 1)
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            text: 'Home Works Managing System'
            size_hint_x: 1
            bold: True
            color: (.9,.9,.9,1)

    BoxLayout:
        padding: 10
        BoxLayout:
            id: product_details
            orientation: "vertical"
            size_hint_x: .8
            spacing: 10

            BoxLayout:
                id: product_labels
                size_hint_y: None
                height: 40
                canvas.before:
                    Color:
                        rgba: (.30, .18, .42, 1)
                    Rectangle:
                        size: self.size
                        pos: self.pos
                    
                FlatButton:
                    text: 'No.'
                    size_hint_x: .05
                FlatButton:
                    text: 'Subject'
                    size_hint_x: .2
                FlatButton:
                    text: 'HW'
                    size_hint_x: .45
                FlatButton:
                    text: 'Start date'
                    size_hint_x: .1
                FlatButton:
                    text: 'Due date'
                    size_hint_x: .1
                FlatButton:
                    text: 'Status'
                    size_hint_x: .1

            BoxLayout:
                id: product_inputs
                size_hint_y: None
                height: 30
                spacing: 5
                TextInput:
                    id: no_inp
                    size_hint_x: .05
                TextInput:
                    id: subj_inp
                    size_hint_x: .2
                    multiline: False
                    on_text_validate: root.update_purchases()
                TextInput:
                    id: hw_inp
                    size_hint_x: .45
                TextInput:
                    id: sdate_inp
                    size_hint_x: .1
                TextInput:
                    id: ddate_inp
                    size_hint_x: .1
                TextInput:
                    id: status_inp
                    size_hint_x: .1
            BoxLayout:
                id: add_to_cart
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: None
                    height: 30
                    canvas.before:
                        Color:
                            rgba: (.30, .18, .42, 1)
                        Rectangle:
                            size: self.size
                            pos: self.pos
                    Label:
                        text: 'Subject'
                        size_hint_x: .2
                    Label:
                        text: 'No.'
                        size_hint_x: .3
                    Label:
                        text: 'HW'
                        size_hint_x: .1
                    Label:
                        text: 'Status'
                        size_hint_x: .1
                GridLayout:
                    id: hw_list
                    cols: 1
                


        BoxLayout:
            id: preview
            orientation: 'vertical'
            size_hint_x: .2

            TextInput:
                id: receipt_preview
                readonly: True
                text: 'Drop your files here'
    BoxLayout:
        id: footer
        size_hint_y: None
        height: 30
        canvas.before:
            Color:
                rgba: (.30, .18, .48, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'International Ala-Too University'
