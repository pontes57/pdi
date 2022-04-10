from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.image import CoreImage
from kivy.lang import Builder

from PIL import Image

kv = Builder.load_string('''
#:kivy 2.0.0

<RootWidget>:
    img: img
    img3: img3
    img4: img4
    do_default_tab: False

    TabbedPanelItem:
        text: 'PIL Image'

        Screen:
            RelativeLayout:
                Image:
                    id: img
                    pos_hint: {"left": 1, 'bottom': 1}
                    size_hint: 0.5, 1
                    allow_stretch: True

            RelativeLayout:
                Image:
                    id: img3
                    pos_hint: {"right": 1, 'bottom': 1}
                    size_hint: 0.5, 1
                    allow_stretch: True

    TabbedPanelItem:
        text: 'canvas'

        Screen:
            FloatLayout:
                Image:
                    id: img4
                    keep_data: True
                    allow_stretch: True
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  # Black
                        Rectangle:
                            pos: self.pos
                            size: self.size


''')


class RootWidget(TabbedPanel):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        iw = Image.open(r"C:\Users\gabri\Documents\pdi\pratica 1\Prática01\praiaOrig.png")   # Use PIL.Image
        iw.save('./phase.png')
        gray = iw.convert('1')
        gray.save('./gray_im.png')
        self.img.source = './phase.png'
        self.img3.texture = CoreImage('./gray_im.png').texture
        self.img4.source = './gray_im.png'


class KivyPILApp(App):
    title = "Kivy & PIL Demo"

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    KivyPILApp().run()