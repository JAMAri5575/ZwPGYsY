# 代码生成时间: 2025-09-22 11:25:22
# sorting_algorithm_kivy_app.py
"""
Kivy application to demonstrate various sorting algorithms.
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# Define a Kivy widget for the sorting algorithm app
class SortingAlgorithmWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(SortingAlgorithmWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Enter numbers separated by commas"))
        self.text_input = TextInput(multiline=False)
        self.add_widget(self.text_input)
        self.add_widget(Label(text="Choose a sorting algorithm"))
        self.algorithm_spinner = Spinner(text='Algorithm', values=('Bubble Sort', 'Insertion Sort', 'Merge Sort'), size_hint_y=None, height=40)
        self.add_widget(self.algorithm_spinner)
        self.add_widget(Button(text='Sort', on_release=self.sort_numbers))
        self.add_widget(Label(text="Sorted Numbers"))
        self.result_label = Label()
        self.add_widget(self.result_label)

    def sort_numbers(self, instance):
        # Get the numbers from the text input, split by comma and convert to integers
        try:
            numbers = [int(num.strip()) for num in self.text_input.text.split(',')]
        except ValueError:
            self.result_label.text = 'Please enter valid numbers separated by commas'
            return

        # Sort the numbers according to the selected algorithm
        self.result_label.text = 'Sorting...'
        if self.algorithm_spinner.text == 'Bubble Sort':
            sorted_numbers = self.bubble_sort(numbers)
        elif self.algorithm_spinner.text == 'Insertion Sort':
            sorted_numbers = self.insertion_sort(numbers)
        elif self.algorithm_spinner.text == 'Merge Sort':
            sorted_numbers = self.merge_sort(numbers)
        else:
            self.result_label.text = 'Please select a valid sorting algorithm'
            return

        self.result_label.text = ', '.join(map(str, sorted_numbers))

    def bubble_sort(self, arr):
        # Bubble Sort algorithm
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def insertion_sort(self, arr):
        # Insertion Sort algorithm
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def merge_sort(self, arr):
        # Merge Sort algorithm
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

# Define the Kivy app
class SortingApp(App):
    def build(self):
        return SortingAlgorithmWidget()

if __name__ == '__main__':
    SortingApp().run()