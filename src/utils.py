"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
import re

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class StitchCalculator():
    def __init__(self):
        pass

# arguments: string userIn, string mode
#            mode should be either "int" or "float" depending on which should be checked
# return: boolean, True means string is valid

    def isValid(self, userIn, mode):
        isValid = True

        if (mode == "int"):
            if (not userIn.isdigit()):
                isValid = False
                print("Number must be a positive integer!")

        elif (mode == "float"):
            try:
                float(userIn)
            except ValueError:
                print("Number must be a valid float!")
                isValid = False

            if (re.search("-", userIn) != None):
                print("Number must be positive!")
                isValid = False


        else:
            print("Mode must be int or float")
            isValid = False

        return isValid

    def rectangle_calculator(self, width, length, gauge_l, gauge_w, s_multiple, s_remainder, r_multiple, r_remainder ):
        stitches = self.one_dim_calculator(width, gauge_w, s_multiple, s_remainder)
        rows = self.one_dim_calculator(length, gauge_l, r_multiple, r_remainder)
        return (stitches, rows)

    def one_dim_calculator(self, x, gauge, multiple , remainder):
        estimate = int(x * gauge)
        difference = (estimate -  remainder)% multiple
        if difference == 0:
            return estimate
        elif difference  == 1:
            return estimate + 1
        else:
            option1 = estimate - difference + multiple
            option2 = estimate - difference
            if difference > abs(multiple - difference):
                return option1
            else:
                return option2

class Styles:
    def __init__(self, label_color, header_color, size_hint, height, background_color, padding, spacing):
        self.label_color = label_color
        self.header_color = header_color
        self.size_hint = size_hint
        self.height = height
        self.background_color = background_color
        self.padding = padding
        self.spacing = spacing


class GenerateWidgets:
    def __init__(self):
        pass

    # Create a form
    # labels is a dictionary like {"input1" : 0.0}, first being the label, second being the type
    def generate_number_form(self, cols, labels, styles, layout, submit_handler):
        scroll_view = ScrollView(size_hint=(1, 6))
        form_layout = GridLayout(cols=cols, padding=styles.padding, spacing=styles.spacing, size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))  # Adjust the height to fit content dynamically

        text_inputs = {}
        for key, value in labels.items():
            form_layout.add_widget(Label(text=key, color=styles.header_color))
            form_layout.add_widget(Label())
            for name in value:
                form_layout.add_widget(Label(text=name, color=styles.label_color))
                text_inputs[name] = TextInput(size_hint=styles.size_hint, height=styles.height,
                                              background_color=styles.background_color)
                form_layout.add_widget(text_inputs[name])

        scroll_view.add_widget(form_layout)
        layout.add_widget(scroll_view)
        result = Label(text="Result", color=styles.header_color)
        layout.add_widget(result)
        submit_button = Button(text="Submit", size_hint=styles.size_hint, height=styles.height,
                               background_color=styles.background_color)
        submit_button.bind(on_press=submit_handler)
        layout.add_widget(submit_button)

        return layout, text_inputs, result