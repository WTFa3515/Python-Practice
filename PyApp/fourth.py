from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        #color = (random(), random(), random())
        with self.canvas:
            Color(random(), random(), random())
            #Color(*color)
            #怕太暗可以用Color(random(),1,1, mode='hsv') 把RGB改成HSV(色調,飽和度,明度)
            d = 10
            Ellipse( pos= (touch.x -d/2, touch.y -d/2), size= (d,d))
            touch.ud['line'] = Line( points =[touch.x, touch.y] )
    
    def on_touch_up(self, touch):
        with self.canvas:
            Color = (random(), random(), random())
            d = 10
            Ellipse( pos= (touch.x -d/2, touch.y -d/2), size= (d,d))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()#開新窗口，給MyPaintWidget和Button用(但沒有設定按鈕大小)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'Clear')#等號右邊其實就是按鈕了，只是這邊給clearbtn儲存方便調用
        clearbtn.bind(on_release = self.clear_canvase)#將清除紐bind(綁定)下面的清除畫布。當clear紐被按下時就去呼叫clear_canvase
        parent.add_widget(self.painter)#在窗口中新增一個自己()然後在第二行已經將panter定義成可以呼叫MyPaintWidget類別了
        parent.add_widget(clearbtn)#在窗口中增加清除鈕
        return parent
    def clear_canvase(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()
