# 代码生成时间: 2025-09-23 22:52:46
import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

"""
Web Content Grabber App

This app allows users to input a URL and fetch the content of the webpage.
It demonstrates the use of Kivy framework for GUI and requests + beautifulsoup
for web content extraction.
"""

class WebContentGrabberApp(App):
    def build(self):
        # Create a BoxLayout to hold the widgets
        layout = BoxLayout(orientation='vertical')

        # Create a TextInput for the URL
        self.url_input = TextInput(multiline=False, hint_text='Enter URL here')

        # Create a Button to start the fetch process
        fetch_button = Button(text='Fetch Content')
        fetch_button.bind(on_press=self.fetch_content)

        # Create a Label to display the fetched content
        self.content_label = Label(text='Content will be displayed here', text_size=(600, None))

        # Add the widgets to the layout
        layout.add_widget(self.url_input)
        layout.add_widget(fetch_button)
        layout.add_widget(self.content_label)

        return layout

    def fetch_content(self, instance):
        # Get the URL from the TextInput
        url = self.url_input.text

        # Check if URL is not empty
        if not url:
            self.content_label.text = 'Please enter a URL'
            return

        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the text content from the parsed HTML
            content = soup.get_text()

            # Display the content in the Label
            self.content_label.text = content
        except requests.exceptions.HTTPError as errh:
            self.content_label.text = f'HTTP Error: {errh}'
        except requests.exceptions.ConnectionError as errc:
            self.content_label.text = f'Error Connecting: {errc}'
        except requests.exceptions.Timeout as errt:
            self.content_label.text = f'Timeout Error: {errt}'
        except requests.exceptions.RequestException as err:
            self.content_label.text = f'OOps: Something Else: {err}'
        except Exception as e:
            self.content_label.text = f'An error occurred: {e}'

if __name__ == '__main__':
    WebContentGrabberApp().run()