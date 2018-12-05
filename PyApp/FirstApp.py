#py-m pip install --upgrade pip wheel setuptools
#py -m pip install kivy
#can't open window, so continue install
#py -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
#can open window but didn't show hello world
#py -m pip install kivy.deps.gstreamer
#py -m pip install kivy.deps.angle
#fk, I key in "buil" not "build". No wander I can't show text

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text = 'Hello world, by kivy')

TestApp().run()