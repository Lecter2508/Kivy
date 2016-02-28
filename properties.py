from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.event import EventDispatcher


class MyClass1(EventDispatcher):
    a = NumericProperty(1)

    def on_a(self, instance, value):
        print('Hello')


class MyClass2(EventDispatcher):
    a = NumericProperty(1)


def callback(instance, value):
    print('My callback is call from', instance)
    print('and the a value changed to', value)


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)
