from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class FloatLayout(FloatLayout):
    Window.clearcolor = (255, 255, 255, 255)
    pass


class Start(App):
    NAME = "default player"

    def build(self):
        return FloatLayout()


start = Start()
start.run()
