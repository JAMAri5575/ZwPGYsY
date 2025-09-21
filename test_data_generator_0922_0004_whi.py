# 代码生成时间: 2025-09-22 00:04:40
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class TestDataGeneratorApp(App):
    """
    Kivy application to generate test data.
    This application allows users to specify the number of test data entries
    and the range for each field, and then generates random data within the specified range.
    """
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create a label to display instructions
        self.instructions_label = Label(text=
            "This application generates test data based on user-defined criteria."
        )
        layout.add_widget(self.instructions_label)

        # Create a text input for the user to specify the number of entries
        self.entries_input = TextInput(hint_text='Enter number of entries')
        layout.add_widget(self.entries_input)

        # Create a text input for the user to specify the range for field 1
        self.range_input_1 = TextInput(hint_text='Enter range for field 1 (e.g., 1-100)')
        layout.add_widget(self.range_input_1)

        # Create a text input for the user to specify the range for field 2
        self.range_input_2 = TextInput(hint_text='Enter range for field 2 (e.g., 1-100)')
        layout.add_widget(self.range_input_2)

        # Create a button to generate the test data
        self.generate_button = Button(text='Generate Test Data')
        self.generate_button.bind(on_press=self.generate_test_data)
        layout.add_widget(self.generate_button)

        # Create a label to display the generated test data
        self.test_data_label = Label(text='')
        layout.add_widget(self.test_data_label)

        return layout

    def generate_test_data(self, instance):
        # Get the number of entries from the user input
        try:
            num_entries = int(self.entries_input.text)
        except ValueError:
            self.test_data_label.text = 'Invalid number of entries. Please enter a positive integer.'
            return

        # Get the ranges for each field from the user input
        try:
            range_1 = self.parse_range(self.range_input_1.text)
            range_2 = self.parse_range(self.range_input_2.text)
        except ValueError:
            self.test_data_label.text = 'Invalid range format. Please use the format 