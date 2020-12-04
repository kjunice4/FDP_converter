from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "List_of_Converters"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 50
            text: "KSquared"
            on_release:
                app.root.current = "List_of_Converters"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Fractions, Decimals, and Percentage Converters"
            on_release:
                app.root.current = "List_of_Converters"
                root.manager.transition.direction = "left" 

""")

#List of converters
Builder.load_string("""
<List_of_Converters>:
    id: List_of_Converters
    name: "List_of_Converters"
        
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Button:
                font_size: 75
                size_hint_y: None
                height: 600
                text: "Fractions Converter"
                on_release:
                    app.root.current = "Fractions_converter"
                    root.manager.transition.direction = "left" 
            
            Button:
                font_size: 75
                size_hint_y: None
                height: 600
                background_color: 0, 0 , 1 , 1
                text: "Decimals converter"
                on_release:
                    app.root.current = "Decimals_converter"
                    root.manager.transition.direction = "left" 
        
            Button:
                font_size: 75
                size_hint_y: None
                height: 600
                text: "Percentages converter"
                on_release:
                    app.root.current = "Percentages_converter"
                    root.manager.transition.direction = "left" 

""")

Builder.load_string("""
<Percentages_converter>
    id: Percentages_converter
    name:"Percentages_converter"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                text: "Percentages Converter"   
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        input.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: input
                    text: input.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:4 - len(input.text)] 
                    
                Label:
                    font_size: 75
                    text: "%"
                    size: self.texture_size
                                
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: 75
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Fraction"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentages_converter.convert_perc_to_frac(input.text)
                        
                Button:
                    id: steps
                    text: "Decimal"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentages_converter.convert_perc_to_dec(input.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
""")

Builder.load_string("""
<Fractions_converter>
    id: Fractions_converter
    name:"Fractions_converter"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                text: "Fractions Converter"   
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        Whole.text = ""
                        Numerator.text = ""
                        Denomenator.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        Whole.text = ""
                        Numerator.text = ""
                        Denomenator.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                Label:
                    font_size: 75
                    text: "Whole"
                    size: self.texture_size
                
                TextInput:
                    id: Whole
                    text: Whole.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(Whole.text)] 
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                Label:
                    font_size: 75
                    text: "Numerator"
                    size: self.texture_size
                
                TextInput:
                    id: Numerator
                    text: Numerator.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(Numerator.text)] 
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                Label:
                    font_size: 75
                    text: "Denomenator"
                    size: self.texture_size
                
                TextInput:
                    id: Denomenator
                    text: Denomenator.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(Denomenator.text)] 
                    
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: 75
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Percent"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions_converter.convert_frac_to_perc(Whole.text + "(" + Numerator.text + "/" + Denomenator.text + ")")
                        
                Button:
                    id: steps
                    text: "Decimal"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions_converter.convert_frac_to_dec(Whole.text + "(" + Numerator.text + "/" + Denomenator.text + ")")
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height            
    
""")

Builder.load_string("""
<Decimals_converter>
    id: Decimals_converter
    name:"Decimals_converter"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                text: "Decimals Converter"   
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        input.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: input
                    text: input.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(input.text)] 
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: 75
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Fraction"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Decimals_converter.convert_dec_to_frac(input.text)
                        
                Button:
                    id: steps
                    text: "Percent"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Decimals_converter.convert_dec_to_perc(input.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height            
    
""")

class Homepage(Screen):
    pass

class List_of_Converters(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(List_of_Converters, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = sm.previous()  

class Decimals_converter(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Decimals_converter, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "List_of_Converters"  

    layouts = []
    def convert_dec_to_frac(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if entry.count(".") == 1:
                decimal_index = entry.find(".")
                whole = str(entry[:decimal_index])
                print("whole",whole)
                dec_for_frac = entry[decimal_index+1:]
                print("dec_for_frac",dec_for_frac)
                numerator = dec_for_frac[:2]
                print("numerator",numerator)
                
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50 ",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                    
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break
                
                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                            
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]
                    
                self.ids.list_of_steps.add_widget(Label(text= str(entry) + " to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(str(denomenator)) + "  ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout) 
            else:
                self.ids.list_of_steps.add_widget(Label(text="Enter a decimal number", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout) 
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_dec_to_perc(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if entry.count(".") == 1:
                percent = str(float(entry)*100) + "%"
                print("percent ",percent)
                self.ids.list_of_steps.add_widget(Label(text=percent, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text="Enter a decimal number", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout) 
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)      
            
class Fractions_converter(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Fractions_converter, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "List_of_Converters"     

    layouts = []
    def convert_frac_to_perc(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            left_par_index = entry.find("(") 
            whole = entry[:left_par_index] 
            print("whole",whole)
            frac_sign = entry.find("/")
            numerator = entry[left_par_index+1:frac_sign]
            print("numerator",numerator)
            right_par_index = entry.find(")")
            denomenator = entry[frac_sign+1:right_par_index]
            print("denomenator",denomenator)
            if int(numerator) < int(denomenator):
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0","") , font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(denomenator) + "  " * len(str(whole)), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= " to Percentage = ", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                last_digits = str(100 / int(denomenator) * int(numerator))
                print("last_digits",last_digits)
                if last_digits[-2:] == '.0':
                    last_digits = last_digits[:-2]
                percentage = str(str(whole) + str(last_digits)) + "%"
                print("percentage",percentage)
                self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_frac_to_dec(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            left_par_index = entry.find("(") 
            whole = entry[:left_par_index] 
            print("whole",whole)
            frac_sign = entry.find("/")
            numerator = entry[left_par_index+1:frac_sign]
            print("numerator",numerator)
            right_par_index = entry.find(")")
            denomenator = entry[frac_sign+1:right_par_index]
            print("denomenator",denomenator)
            if int(numerator) < int(denomenator):
                self.ids.list_of_steps.add_widget(Label(text= str(numerator), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole)+ " " + "---" * len(denomenator) + "  " * len(str(whole)), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= " to Decimal = ", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                last_digits = str(100 / int(denomenator) * int(numerator))
                print("last_digits",last_digits)
                if last_digits[-2:] == '.0':
                    last_digits = last_digits[:-2]
                decimal = str(str(whole) + "." + str(last_digits))
                print("decimal",decimal)
                if decimal.count(".") > 1:
                    index = decimal.find(".")
                    decimal = decimal[:index] + decimal[index+1:]
                self.ids.list_of_steps.add_widget(Label(text= decimal, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)  
            
class Percentages_converter(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Percentages_converter, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "List_of_Converters"
            
    layouts = []
    def convert_perc_to_frac(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            # 2, 4, 5, 10, 25, 50
            if len(entry) > 2:
                numerator = entry[-2:]
                whole = entry[:-2]
                print("whole",whole)
                print("numerator",numerator)
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50 ",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break

                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator) == "00":
                    numerator = "1" + str(numerator)
                    
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]    
                
                self.ids.list_of_steps.add_widget(Label(text= str(entry) + "% to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(str(denomenator)) + "  ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)     
                
            if len(entry) <= 2:
                numerator = entry
                print("numerator",numerator)
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50 ",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                    
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break
                
                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                            
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]
                    
                self.ids.list_of_steps.add_widget(Label(text= entry + "% to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0","") , font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "-----", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_perc_to_dec(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            dec = entry + "/100"
            evaled = str(eval(dec))
            print("evaled",evaled)
            self.ids.list_of_steps.add_widget(Label(text= entry + "% to Decimal = ", font_size = 75, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= evaled, font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))   
            self.layouts.append(layout)
            
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage")) 
sm.add_widget(List_of_Converters(name="List_of_Converters")) 
sm.add_widget(Fractions_converter(name="Fractions_converter"))
sm.add_widget(Decimals_converter(name="Decimals_converter"))     
sm.add_widget(Percentages_converter(name="Percentages_converter")) 
sm.current = "Homepage"   

class FDP_Converter(App):
    def build(app):
        return sm

if __name__ == '__main__':
    FDP_Converter().run()
    

