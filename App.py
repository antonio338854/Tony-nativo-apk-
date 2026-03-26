from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        return Button(text='Ola! Eu sou um APK!', 
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

if __name__ == '__main__':
    MeuApp().run()
