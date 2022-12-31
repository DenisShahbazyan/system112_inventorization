from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy_garden.zbarcam import ZBarCam
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField

from kivy.network.urlrequest import UrlRequest
import json
from http import HTTPStatus
from kivy.config import Config


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class LoginScreen(MDScreen):
    input_login: MDTextField = ObjectProperty()
    input_password: MDTextField = ObjectProperty()
    label_error: MDLabel = ObjectProperty()
    input_password_field: ClickableTextFieldRound = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = None

    def got_success(self, req, token):
        self.token = token['auth_token']

    def got_error(self, req, *args):
        self.label_error.text = (
            'Ошибка ' + str(req.resp_status) + ' ' + str(req.error)
        )

    def got_fail(self, req, *args):
        self.label_error.text = 'Ошибка ' + str(req.resp_status)

    def sign_in(self):
        URL = 'http://127.0.0.1:8000/api/auth/token/login/'
        values = {
            'password': str(self.input_password.text.strip()),
            'email': str(self.input_login.text.strip()),
        }
        params = json.dumps(values)
        headers = {
            'Content-type': 'application/json',
            'Accept': '*/*'
        }

        req = UrlRequest(
            URL,
            req_body=params,
            req_headers=headers,
            on_failure=self.got_fail,
            on_error=self.got_error,
            on_success=self.got_success,
        )
        req.wait()

        if req.resp_status == HTTPStatus.OK and self.token is not None:
            self.manager.current = 'menu'

    def on_touch_down(self, touch):
        if self.input_login.collide_point(*touch.pos):
            self.label_error.text = ''
        if self.input_password_field.collide_point(*touch.pos):
            self.label_error.text = ''
        return super().on_touch_down(touch)


class MenuScreen(MDScreen):
    zbarcam: ZBarCam = ObjectProperty()
    qrfield: MDTextField = ObjectProperty()

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


if __name__ == '__main__':
    Window.size = (375, 750)
    Builder.load_file('../ui/main.kv')
    InventorizationApp().run()
