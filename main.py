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
                app.root.current = "FDP_Converter_page"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 50
            text: "KSquared"
            on_release:
                app.root.current = "FDP_Converter_page"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Fractions, Decimals, and Percentage Converter"
            on_release:
                app.root.current = "FDP_Converter_page"
                root.manager.transition.direction = "left" 

""")

#Length 
Builder.load_string("""
<FDP_Converter_page>
    id: FDP_Converter_page
    name:"FDP_Converter_page"
    
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
                    background_color: 1, 0 , 0 , 1
                    on_release:
                        input.text = ""
                        
                Button:
                    id: steps
                    text: "Clear Answers"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        
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
                fullscreen: True
                __safe_id: [dropdown.__self__]
                
                TextInput:
                    id: input
                    text: input.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:10 - len(input.text)] 
                    
                Button:
                    id: btn
                    text: "V"
                    on_release: dropdown.open(self)
                    size_hint_y: None
                    height: 200
                    
                DropDown:
                    id: dropdown
                    on_parent: self.dismiss()
                    on_select: btn.text = "{}".format(args[1])
                        
                    Button:
                        text: "Inches"
                        size_hint_y: None
                        height: 200
                        on_release: dropdown.select("Inches")
                        
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
                
                Button:
                    id: btn
                    text: "Inches"
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 1 , 0 , 1
                    on_release:
                        Length.inches(input.text)
                                            
                Button:
                    id: btn
                    text: "Feet"
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        Length.feet(input.text)

            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
                
                Button:
                    id: btn
                    text: "Yard"
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        Length.yard(input.text)
                                            
                Button:
                    id: btn
                    text: "Mile"
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 1 , 0 , 1
                    on_release:
                        Length.mile(input.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
""")
class Homepage(Screen):
    pass
           
class FDP_Converter_page(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(FDP_Converter_page, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = sm.previous()
            
    layouts = []
    def inches(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if float(entry) > 0:
                self.ids.list_of_steps.add_widget(Label(text="Entered Inches : " + str(format(float(entry),",") + " in"), font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Feet : " + str(format(float(entry)/12,",")) + " ft", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Yards : " + str(format(float(entry)/36,",")) + " yd", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Miles : " + str(format(float(entry)/63360,",")) + " mi", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Positive Numbers Only!" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)

        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def feet(self,entry):
        print("inches ",entry)
        
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if float(entry) > 0:
                self.ids.list_of_steps.add_widget(Label(text="Entered Feet : " + str(format(float(entry),",")) + " ft", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Inches : " + str(format(float(entry)*12,",") + " in"), font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Yards : " + str(format(float(entry)/3,",")) + " yd", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Miles : " + str(format(float(entry)/5280,",")) + " mi", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Positive Numbers Only!" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)

        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def yard(self,entry):
        print("inches ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if float(entry) > 0:
                self.ids.list_of_steps.add_widget(Label(text="Entered Yards : " + str(format(float(entry),",")) + " yd", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Inches : " + str(format(float(entry)*36,",") + " in"), font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Feet : " + str(format(float(entry)*3,",")) + " ft", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Miles : " + str(format(float(entry)/1760,",")) + " mi", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Positive Numbers Only!" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)

        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def mile(self,entry):
        print("inches ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            if float(entry) > 0:
                self.ids.list_of_steps.add_widget(Label(text="Entered Miles : " + str(format(float(entry),",")) + " mi", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Inches : " + str(format(float(entry)*63360,",") + " in"), font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Feet : " + str(format(float(entry)*5280,",")) + " ft", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Yards : " + str(format(float(entry)*1760,",")) + " yd", font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Positive Numbers Only!" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)

        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)


sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(FDP_Converter_page(name="FDP_Converter_page"))     
sm.current = "Homepage"   



class Units(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Units().run()
    

