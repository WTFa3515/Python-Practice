from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 1, 0.5)  #set the color (R, G, B, transparency)
            Rectangle( pos= (10, 10), size= (50, 50) )
            Color(1, 1, 1)
            d = 30 #diameter(直徑) = 30 position
            Ellipse( pos = (touch.x - d/2, touch.y - d/2), size = (d, d) )
            #Ellipse 是用外切正方形來畫圓，所以要給的值是：左下角的位置，外切正方形的寬高
            #Ellipse ( pos= 左下角的(x,y), size= (寬, 高) )，為了要讓圓心在鼠標，所已減了 d/2
            touch.ud['line'] = Line( points= (touch.x, touch.y) )
            #將鼠標點下去的x,y值保存到touch.ud字典的'line'(line是key值??)中去做為起點，"可是這邊確實產生了一條起點到起點的線"
    def on_touch_move(self, touch):#拖動鼠標時，會連續處發"on_touch_move"，所以能像微分的dx一樣一直畫一小段直線
        touch.ud['line'].points += [touch.x, touch.y]
        
        #從上面touch_down的起點開始往move過後的地方一直++，進而畫出線

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

if __name__ == '__main__':
    MyPaintApp().run()