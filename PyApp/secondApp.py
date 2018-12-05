#Site Of Mouse Click
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

if __name__ == '__main__':
    MyPaintApp().run()

'''
when you click mouse (left button) will print 
"<MouseMotionEvent spos=(0.99, 0.013333333333333308) pos=(792.0, 7.999999999999985)>"
and the initial (0,0) is at "lower left corner"
pos is position, and the spos is "current position / screen width"
'''