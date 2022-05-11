
from kivy.uix.screenmanager import Screen
import os
from findervideos.finderphrases import FinderPhrases
import json
from kivy.uix.screenmanager import ScreenManager

from kivy.app import App

os.environ['KIVY_VIDEO'] = 'ffpyplayer'


class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()
        sc1 = ScreenOne(name='screen_one')
        sc2 = ScreenTwo(name='screen_two')
        screen_manager.add_widget(sc1)
        screen_manager.add_widget(sc2)

        return screen_manager


class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search_video(self):
        text = self.text_input.text
        list_videos = FinderPhrases().get_phrases(text, 3)
        with open('links_videos.json', 'w') as fp:
            json.dump(list_videos, fp)


class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_videos(self):
        with open('./links_videos.json', 'r') as f:
            list_of_videos = json.load(f)
        list_caption = [elem['caption'] for elem in list_of_videos]
        list_links = [elem['link'] for elem in list_of_videos]
        return list_links


def printlog(message):
    with open('./log.txt', 'a') as f: f.write(message + "\n")


if __name__ == '__main__':
    TestApp().run()
