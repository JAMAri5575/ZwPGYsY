# 代码生成时间: 2025-09-17 08:27:30
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserPopup
import pandas as pd
import numpy as np

"""
数据统计分析器程序
"""

class DataAnalysisApp(App):
    def build(self):
        # 创建主布局
        self.layout = BoxLayout(orientation='vertical')

        # 添加标题
        self.layout.add_widget(Label(text='数据统计分析器', size_hint_y=None, height=50))

        # 添加文件选择按钮
        btn_load_data = Button(text='加载数据文件')
        btn_load_data.bind(on_release=self.load_data)
        self.layout.add_widget(btn_load_data)

        # 添加结果显示区域
        self.result_label = Label(text='', size_hint_y=None, height=30)
        self.layout.add_widget(self.result_label)

        return self.layout

    def load_data(self, instance):
        # 弹出文件选择对话框
        filechooser = FileChooserPopup(select=self.load_file)
        filechooser.open()

    def load_file(self, selection, selection_causes):
        if selection:
            try:
                # 使用Pandas加载数据
                self.data = pd.read_csv(selection[0])
                self.result_label.text = '数据加载成功'
            except Exception as e:
                self.result_label.text = '加载数据失败: {}'.format(str(e))
        else:
            self.result_label.text = '未选择任何文件'

    def on_start(self):
        # 应用启动时执行的操作
        pass

# 运行程序
if __name__ == '__main__':
    DataAnalysisApp().run()