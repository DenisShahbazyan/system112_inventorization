from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import ObjectProperty

from kivymd.uix.tab.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivy_garden.zbarcam import ZBarCam


class Tab(MDFloatLayout, MDTabsBase):
    pass


class LoginScreen(MDScreen):
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
            self.manager.current = 'menu'
        else:
            self.label_error.text = 'Ошибка входа!'

    def on_touch_down(self, touch):
        if self.input_login.collide_point(*touch.pos):
            self.label_error.text = ''
        if self.input_password.collide_point(*touch.pos):
            self.label_error.text = ''
        return super().on_touch_down(touch)


class MenuScreen(MDScreen):
    zbarcam: ZBarCam
    qrfield: ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__cam_release()

    def scan(self, instance):
        self.__cam_release()

    def on_touch_down(self, touch):
        if self.zbarcam.collide_point(*touch.pos):
            self.__cam_open()
        return super().on_touch_down(touch)

    def __cam_release(self):
        if self.zbarcam.xcamera._camera._device.isOpened():
            self.zbarcam.stop()
            self.zbarcam.xcamera._camera._device.release()

    def __cam_open(self):
        if not self.zbarcam.xcamera._camera._device.isOpened():
            self.zbarcam.xcamera._camera._device.open(0)
            self.zbarcam.start()


class InventorizationApp(MDApp):
    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.theme_style = 'Light'

    def build(self):
        sm = MDScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        return sm


if __name__ == "__main__":
    Window.size = (375, 750)
    Builder.load_file('../ui/inventorization.kv')
    InventorizationApp().run()
