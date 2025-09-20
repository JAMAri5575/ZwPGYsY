# 代码生成时间: 2025-09-21 05:13:31
Interactive Chart Generator using Kivy framework.
This application allows users to interactively generate charts and graphs.
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.chart import Chart, LinePlot
from kivy.core.window import Window
import random

class InteractiveChartApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Create the chart
        chart = Chart()
        chart.size_hint = (1, 1)
        chart.bind(minimum_height=chart.setter('height'))
        chart.bind(minimum_width=chart.setter('width'))
        main_layout.add_widget(chart)

        # Create the input fields
        self.input_x = TextInput(text='Enter X values separated by comma:', multiline=True)
        main_layout.add_widget(self.input_x)

        self.input_y = TextInput(text='Enter Y values separated by comma:', multiline=True)
        main_layout.add_widget(self.input_y)

        # Create the generate button
        self.generate_button = Button(text='Generate Chart')
        self.generate_button.bind(on_press=self.generate_chart)
        main_layout.add_widget(self.generate_button)

        return main_layout

    def generate_chart(self, instance):
        # Clear the chart
        chart = self.root.get_widget_class(Chart)
        chart.clear()

        # Get the input values
        x_values = [float(i) for i in self.input_x.text.split(',') if i.strip().isdigit()]
        y_values = [float(i) for i in self.input_y.text.split(',') if i.strip().isdigit()]

        # Check if both lists have the same length
        if len(x_values) != len(y_values):
            raise ValueError('X and Y values must have the same length')

        # Create a LinePlot
        with chart.plot(ctx=chart.ctx) as plot:
            plot.line(x_values=x_values, y_values=y_values, color=[1, 0, 0, 1])

class MainApp(App):
    def build(self):
        # Set up the window size
        Window.size = (800, 600)
        return InteractiveChartApp().build()

if __name__ == '__main__':
    MainApp().run()
