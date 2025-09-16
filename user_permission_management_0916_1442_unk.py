# 代码生成时间: 2025-09-16 14:42:48
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, StringProperty


class UserPermissionManagementApp(App):
    def build(self):
        sm = ScreenManager()
        
        # Define the screens
        main_screen = MainScreen()
        user_management_screen = UserManagementScreen()
        
        # Add screens to the screen manager
        sm.add_widget(main_screen)
        sm.add_widget(user_management_screen)
        
        return sm


class MainScreen(Screen):
    def on_enter(self):
        # Add a button to navigate to user management screen
        self.add_widget(Button(text='Manage Users', on_press=self.goto_user_management))
    
    def goto_user_management(self, instance):
        self.manager.current = 'user_management'


class UserManagementScreen(Screen):
    # Define properties
    user_permissions = ListProperty()
    username_input = StringProperty()
    permission_input = StringProperty()
    
    def on_enter(self):
        # Create the layout
        layout = BoxLayout(orientation='vertical')
        
        # Add the username input field
        layout.add_widget(Label(text='Username:'))
        layout.add_widget(TextInput(text=self.username_input, multiline=False,
                                 on_text=self.update_username))
                                 
        # Add the permission input field
        layout.add_widget(Label(text='Permission:'))
        layout.add_widget(TextInput(text=self.permission_input, multiline=False,
                                  on_text=self.update_permission))
        
        # Add the add user button
        layout.add_widget(Button(text='Add User', on_press=self.add_user))
        
        # Add the permissions list
        self.permissions_list = BoxLayout(orientation='vertical')
        for permission in self.user_permissions:
            self.permissions_list.add_widget(Label(text=permission))
        layout.add_widget(self.permissions_list)
        
        # Add the layout to the screen
        self.add_widget(layout)
    
    def update_username(self, instance, value):
        self.username_input = value
    
    def update_permission(self, instance, value):
        self.permission_input = value
    
    def add_user(self, instance):
        try:
            # Add the user with the specified permissions
            self.user_permissions.append(f"{self.username_input}: {self.permission_input}")
            
            # Clear the input fields
            self.username_input = ''
            self.permission_input = ''
            
            # Update the permissions list
            self.permissions_list.clear_widgets()
            for permission in self.user_permissions:
                self.permissions_list.add_widget(Label(text=permission))
        except Exception as e:
            print(f'Error adding user: {e}')


if __name__ == '__main__':
    UserPermissionManagementApp().run()