# 代码生成时间: 2025-09-19 06:13:08
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserPopup
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from collections import Counter
import re

"""
Text File Analyzer App using Kivy Framework
This app allows users to analyze text files by counting word frequencies.
"""

class TextFileAnalyzerApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical')

        # Text input for file path
        self.file_path_input = TextInput(multiline=False, size_hint_y=None, height=40)
        self.file_path_input.bind(on_text_validate=self.open_file)
        layout.add_widget(self.file_path_input)

        # Button to open file chooser
        self.open_button = Button(text='Open File')
        self.open_button.bind(on_release=self.open_file)
        layout.add_widget(self.open_button)

        # Text input to display file content and word frequencies
        self.content_display = TextInput(multiline=True, size_hint_y=0.9)
        self.content_display.disabled = True  # Disable editing
        layout.add_widget(self.content_display)

        return layout

    def open_file(self, instance):
        # Open file chooser popup
        filechooser = FileChooserPopup(select=self.select_file)
        filechooser.open()

    def select_file(self, selection, *args):
        # Handle file selection
        if selection:
            try:
                # Read file content and analyze it
                with open(selection[0], 'r', encoding='utf-8') as file:
                    content = file.read()

                # Update UI with file content and word frequencies
                self.content_display.text = content
                frequency = self.analyze_text(content)
                self.content_display.text += '
' + frequency

            except Exception as e:
                # Handle errors
                error_message = f'Error: {str(e)}'
                self.content_display.text = error_message
        else:
            self.content_display.text = 'No file selected.'

    def analyze_text(self, content):
        # Analyze text content and return word frequency
        words = re.findall(r'\w+', content.lower())
        word_count = Counter(words)
        return 'Word Frequencies:' + ''.join(f'
{word}: {count}' for word, count in word_count.items())

# Run the app
if __name__ == '__main__':
    TextFileAnalyzerApp().run()