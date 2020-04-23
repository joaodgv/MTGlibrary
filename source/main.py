#python and kivy application
from kivy.app import App
from kivy.uix.widget import Widget

class Window(Widget):
    pass

class MagicApp(App):
    def build(self):
        return Window()

if __name__ == '__main__':
    MagicApp().run()