from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
# <Button>
#     background_color: (155/255, 173/255, 212/255,1)
#     canvas.before:
#         Color:
#             rgba: 159/255, 119/255, 186/255,1
#         RoundedRectangle: 
#             size: self.size
#             pos: self.pos
            # radius:[50]
<Label>
    font_size: 32
    background_color: 190/255, 208/255, 247/255
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
<Mylayout>
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        FloatLayout:
            size_hint: (1, 0.1)
            Label:
                text: 'Welcome to the Image Carousel'
                color: (69/255, 226/255, 237/255,1)
                bold: True
                pos_hint: {'center_x':0.5,'top':1}
                # background_color: (11,1,1,1)
                
                # canvas.before:
                #     Color:
                #         rgba: root.background_color
                #     Rectangle:
                #         size: self.size
                #         pos: self.pos
        Carousel:
            id: carousel
            direction: 'right'
            Image:
                source: 'icons/A.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/B.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/C.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/D.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/E.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/F.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/G.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/H.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/I.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/J.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/K.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/L.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/M.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/N.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/O.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/P.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/Q.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/R.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/S.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/T.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/U.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/V.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/W.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/X.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/Y.jpg'
                allow_stretch: True
                keep_ratio: False
            Image:
                source: 'icons/Z.jpg'
                allow_stretch: True
                keep_ratio: False

        FloatLayout:
            size_hint: (1, 0.1)
            Button:
                text: 'Previous'
                pos_hint: {'left':1,'bottom':1}
                on_press: carousel.load_previous()
                size_hint: (0.25, 1)
                outline_color: (0,1,1,1)
                bold: True
                outline_width: 2
                background_color: (0,0,0,0)
                # border: 10,10,10,10
                # canvas.before:
                #     Color:
                #         rgba: self.background_color
                #     RoundedRectangle: 
                #         size: self.size
                #         pos: self.pos
                #         radius: [20, 20, 20, 20]
        # # FloatLayout:
        #     size_hint: (1, 0.1)
            Button:
                # background_normal: 'icons/next_icon.jpg'
                text: 'Next'
                border: (10,10,10,10)
                background_normal: ''
                pos_hint: {'right':1,'bottom':1}
                on_press: carousel.load_next()
                background_color: (0,0,0,0)
                size_hint: (0.25, 1)
                outline_color: (0,1,1,1)
                bold: True
                outline_width: 2
            
                                ''')

class Mylayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return Mylayout()

if __name__ == '__main__':
    MyApp().run()
    