from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivy.properties import ObjectProperty

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '760')

Builder.load_file('../ui/inventorization.kv')


class LoginScreen(Screen):
    input_login = ObjectProperty(None)
    input_password = ObjectProperty(None)
    label_error = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def sign_in(self):
        LOGIN = ''
        PASSWORD = ''
        if (self.input_login.text == LOGIN and
                self.input_password.text == PASSWORD):
            self.manager.current = 'second'
        else:
            self.label_error.text = 'Ошибка входа!'

    def on_touch_down(self, touch):
        if self.input_login.collide_point(*touch.pos):
            self.label_error.text = ''
        if self.input_password.collide_point(*touch.pos):
            self.label_error.text = ''
        return super().on_touch_down(touch)


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class InventorizationApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='second'))
        return sm


if __name__ == "__main__":
    InventorizationApp().run()
