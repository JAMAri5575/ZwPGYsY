# 代码生成时间: 2025-09-23 11:54:45
import os
from kivy.app import App
# 优化算法效率
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# TODO: 优化性能
from kivy.uix.button import Button
from kivy.core.window import Window
from functools import partial
import subprocess
import psutil

"""
进程管理器应用
"""

class ProcessManagerApp(App):
    def build(self):
        # 初始化主布局
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='进程管理器'))
# 改进用户体验

        # 添加结束进程按钮
        self.stop_button = Button(text='结束选中进程')
        self.stop_button.bind(on_press=self.stop_process)
# NOTE: 重要实现细节
        self.layout.add_widget(self.stop_button)

        # 添加进程列表
        self.process_list = []
        self.process_info = []
        self.process_list_widget = BoxLayout(orientation='vertical', size_hint_y=None)
        self.layout.add_widget(self.process_list_widget)

        # 更新进程列表
        self.update_process_list()

        return self.layout

    def update_process_list(self):
        """更新进程列表"""
# 添加错误处理
        self.process_list_widget.clear_widgets()
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                self.process_info.append(proc.info)
                pid_label = Label(text=f'PID: {proc.info["pid"]}')
                name_label = Label(text=f'Name: {proc.info["name"]}')
                button = Button(text='结束进程', size_hint_y=None)
# 优化算法效率
                button.bind(on_press=partial(self.stop_process, proc.info["pid"]))
# TODO: 优化性能

                process_box = BoxLayout(orientation='horizontal', size_hint_y=None)
                process_box.add_widget(pid_label)
                process_box.add_widget(name_label)
                process_box.add_widget(button)

                self.process_list_widget.add_widget(process_box)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # 忽略无法访问的进程
                pass

    def stop_process(self, instance, value=None):
        """结束进程"""
        pid = value if value is not None else instance.text
        try:
            proc = psutil.Process(int(pid))
            proc.terminate()  # 结束进程
# 优化算法效率
            proc.wait()  # 等待进程结束
            self.update_process_list()  # 更新进程列表
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # 忽略无法结束的进程
            pass
        except Exception as e:
            # 显示错误信息
            error_msg = f'结束进程时发生错误: {str(e)}'
# 增强安全性
            self.layout.add_widget(Label(text=error_msg))

    def on_stop(self):
        """退出应用时清理资源"""
        self.process_list_widget.clear_widgets()
# 添加错误处理
        self.process_list = []
        self.process_info = []

if __name__ == '__main__':
    Window.size = (600, 400)  # 设置窗口大小
# NOTE: 重要实现细节
    ProcessManagerApp().run()
# TODO: 优化性能