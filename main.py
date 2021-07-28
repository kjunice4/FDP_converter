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
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Fractions, Decimals, and Percentage Converters"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
""")

Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
        
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
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "Fractions, Decimals, Percentages Converters"  
                font_size: 60
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "List_of_Converters"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Other apps from KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')   
                
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Donate to KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/about-ksquared')
            
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
                height: 300
                background_color: 0, 0 , 0 , 1
                text: "Fractions Converter"
                on_release:
                    app.root.current = "Fractions_converter"
                    root.manager.transition.direction = "left" 
            
            Button:
                font_size: 75
                size_hint_y: None
                height: 300
                background_color: 0, 0 , 0 , 1
                text: "Decimals converter"
                on_release:
                    app.root.current = "Decimals_converter"
                    root.manager.transition.direction = "left" 
        
            Button:
                font_size: 75
                size_hint_y: None
                height: 300
                background_color: 0, 0 , 0 , 1
                text: "Percentages converter"
                on_release:
                    app.root.current = "Percentages_converter"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                size_hint_y: None
                height: 300
                background_color: 0, 0 , 1 , 1
                text: "Back to Menu"
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
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
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "List_of_Converters"
                        root.manager.transition.direction = "right" 
                        
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
                    hint_text: "Percentage:"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:4 - len(input.text)] 
                    
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
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "List_of_Converters"
                        root.manager.transition.direction = "right" 
                        
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
                
                TextInput:
                    id: Whole
                    text: Whole.text
                    hint_text: "Whole:"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Whole.text)] 
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Numerator
                    text: Numerator.text
                    hint_text: "Numerator"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Numerator.text)] 
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Denomenator
                    text: Denomenator.text
                    hint_text: "Denomenator"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Denomenator.text)] 
                    
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
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "List_of_Converters"
                        root.manager.transition.direction = "right" 
                        
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
                    hint_text: "Decimal:"
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

class Menu(Screen):
    pass

class List_of_Converters(Screen):
    pass

class Decimals_converter(Screen):
            
    layouts = []
    def convert_dec_to_frac(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if entry.count(".") == 1:
                decimal_index = entry.find(".")
                print("decimal_index",decimal_index)
                whole = str(entry[:decimal_index])
                print("whole",whole)
                if whole == "0":
                    whole = ""
                print("whole",whole)
                dec_for_frac = entry[decimal_index+1:]
                print("dec_for_frac",dec_for_frac)
                if len(dec_for_frac) == 1:
                    dec_for_frac = dec_for_frac + "0"
                numerator = dec_for_frac
                print("numerator = ",numerator)
                
                denomenator = "1" + "0" * len(numerator)
                print("denomenator = ",denomenator)
                
                numerator = int(numerator)
                print("numerator = ",numerator)
                
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
                        
                if int(numerator) == 0:
                    numerator = ""
                    denomenator = ""
                    
                self.ids.list_of_steps.add_widget(Label(text= str(entry) + " to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(str(denomenator)) + "  " * len(whole), font_size = 75, size_hint_y= None, height=100))
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
            if numerator == "" and denomenator == "":
                numerator = 1
                denomenator = 1
            if int(numerator) < int(denomenator):
                self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0","") , font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(denomenator) + "  " * len(str(whole)), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= " to Percentage = ", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                last_digits = str(int(numerator) / int(denomenator))
                print("last_digits",last_digits)
                if str(whole) != "":
                    percentage = str((float(whole) + float(last_digits)) * 100) + "%"
                    print("percentage",percentage)
                    self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    percentage = str((float(last_digits)) * 100) + "%"
                    print("percentage",percentage)
                    self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            elif int(numerator) == int(denomenator) or str(numerator) == str(denomenator):
                whole = str(int(whole) * 100) + "%"
                print("whole",whole)
                self.ids.list_of_steps.add_widget(Label(text= whole, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text="Numerator exceeds Denomenator", font_size = 60, size_hint_y= None, height=100))
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
                self.ids.list_of_steps.add_widget(Label(text= str(whole)+ " " + "---" * len(numerator) + "  " * len(str(whole)), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= " to Decimal = ", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                last_digits = str(int(numerator) / int(denomenator))
                print("last_digits",last_digits)
                if str(whole) == "":
                    decimal = last_digits
                else:
                    decimal = str(float(whole) + float(last_digits))
                print("decimal",decimal)
                if decimal.count(".") > 1:
                    index = decimal.find(".")
                    decimal = decimal[:index] + decimal[index+1:]
                self.ids.list_of_steps.add_widget(Label(text= decimal, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
            elif int(numerator) >= int(denomenator):
                self.ids.list_of_steps.add_widget(Label(text= str(numerator), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(whole)+ " " + "---" * len(denomenator) + "  " * len(str(whole)), font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(denomenator), font_size = 75, size_hint_y= None, height=100))

                if whole == "":
                    whole = 0
                print("Numerator exceeds denomenator")
                remainder = int(numerator) % int(denomenator)
                print("remainder",remainder)
                whole = str(int(whole) + remainder).replace(".0","")
                print("whole",whole)
                numerator = int(numerator) - (int(denomenator) * int(remainder))
                print("numerator",numerator)
                
                if whole == "0":
                    whole = ""
                
                self.ids.list_of_steps.add_widget(Label(text= " to Decimal = ", font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if whole == "":
                    whole = 0
                
                last_digits = str(int(numerator) / int(denomenator))
                print("last_digits",last_digits)
                decimal = str(float(whole) + float(last_digits))
                print("decimal",decimal)
                
                if decimal.count(".") > 1:
                    index = decimal.find(".")
                    decimal = decimal[:index] + decimal[index+1:]
                self.ids.list_of_steps.add_widget(Label(text= decimal, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
              self.ids.list_of_steps.add_widget(Label(text="Numerator exceeds\n Denomenator", font_size = 75, size_hint_y= None, height=100))
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
            print("Its working ESC = 27 LENGTH at Perc")
            self.set_previous_screen()
            return True
    
    def set_previous_screen(self):
        print("Length is almost working")   
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Current Page:",sm.current)
        if sm.current != "Homepage" and sm.current != "Menu" and sm.current != "List_of_Converters":
            sm.transition.direction = 'right'
            sm.current = "List_of_Converters"
            print("To list from Calc")
        elif sm.current == "List_of_Converters":
            sm.transition.direction = 'right'
            sm.current = "Menu"
            print("To Menu from List")
    
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
sm.add_widget(Menu(name="Menu"))
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
    
