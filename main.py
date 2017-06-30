import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        search_template = "http://0.0.0.0:8000/get"
        search_url = search_template.format(self.search_input.text)
        print('asdasdas')
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['id'], d['email']) for d in data['objects']]
        self.search_results.item_strings = cities
        print("\n".join(cities))

#    pass


class JSONApp(App):
    kv_directory = 'templates'


if __name__ == '__main__':
    JSONApp().run()
