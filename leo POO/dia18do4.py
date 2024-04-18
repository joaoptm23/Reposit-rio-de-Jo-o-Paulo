from kivy.app import app
from kivy.uix.button import button
from kivy.uix.boxlayout import boxlayout
from kivy.uix.label import label

class test (app)
    def build (self)
        box = boxlayout (orientations =  'vertical')
        button = button (text = 'botão 1')
        label = label (text = 'texto 1')
        box.add_widget (button)
        box.add_widget (label)

        box2 = boxlayout ()
        button2 = button (text = 'botão 2')
        label2 = label (text = 'texto 2')
        box2.add_widget (button2)
        box2.add_widget (label2)

        box.add_widget(box2)
        return box

test().run()
