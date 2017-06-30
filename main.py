import kivy


from kivy.app import App


class JSONApp(App):
    kv_directory = 'templates'


if __name__ == '__main__':
    JSONApp().run()
