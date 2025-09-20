# 代码生成时间: 2025-09-20 10:55:41
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty

# Define a custom FloatLayout to handle responsiveness
class ResponsiveFloatLayout(FloatLayout):
    width = NumericProperty(Window.width)
    def __init__(self, **kwargs):
        super(ResponsiveFloatLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_dimensions, 1 / 60.0)  # Update layout dimensions every frame

    def update_dimensions(self, dt):
        self.width = Window.width
        self.height = Window.height

# Define the App class
class ResponsiveLayoutApp(App):
    def build(self):
        # Load the kv file
        self.load_kv('responsive_layout.kv')
        return Builder.load_file('responsive_layout.kv')

    def on_config_change(self, config):
        # Rebuild the app when the configuration changes
        return ResponsiveLayoutApp().build()

# Define the ScreenManager with a default screen
sm = ScreenManager()
sm.add_widget(Screen(name='main', manager=sm))

# Define the layout in kv file
Builder.load_string('''
<ResponsiveFloatLayout>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(10)
    Label:
        text: 'Hello, Kivy!'
        font_size: sp(24)
    Button:
        text: 'Click me'
        size_hint: None, None
        size: dp(200), dp(50)
        font_size: sp(18)
        on_release: app.root.current = 'second'

<SecondScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Second Screen'
            font_size: sp(24)
        Button:
            text: 'Go back'
            size_hint: None, None
            size: dp(200), dp(50)
            font_size: sp(18)
            on_release: app.root.current = 'main'
''')

if __name__ == '__main__':
    ResponsiveLayoutApp().run()