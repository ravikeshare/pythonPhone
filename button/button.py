from abc import ABCMeta, abstractmethod
from screen.screen import LedScreen


class PhoneButton(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def button_pressed(self, value):
        return NotImplementedError


class NumericButton(PhoneButton):

    def button_pressed(self, value):
        # print " Numeric button pressed"
        screen_obj = LedScreen()
        screen_obj.display_input("Numeric Button", value)


class FunctionButton(PhoneButton):

    def button_pressed(self, value):
        # print "Function Button pressed"
        screen_obj = LedScreen()
        screen_obj.display_input("Function Button", value)

