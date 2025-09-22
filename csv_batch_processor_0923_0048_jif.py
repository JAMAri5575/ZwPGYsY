# 代码生成时间: 2025-09-23 00:48:09
import os
import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserPopup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.clock import Clock

"""
CSV文件批量处理器
"""

class CSVBatchProcessorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='CSV文件批量处理器'))
        self.layout.add_widget(Button(text='选择文件夹', on_release=self.open_folder_picker))
        self.layout.add_widget(Label(text=self.current_folder))
        self.layout.add_widget(Button(text='开始处理', on_release=self.process_csv_files))
        return self.layout

    def open_folder_picker(self, instance):
        "