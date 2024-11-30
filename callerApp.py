from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.uix.button import MDIconButton
from kivy.properties import BooleanProperty
from time import sleep
kv = """
<RecieverButton>:
    
MDScreen:
    MDBoxLayout:
        orientation:'vertical'
        size_hint:(1,0.3)
        pos_hint:{'top':1}
        md_bg_color:app.theme_cls.primary_light
        FitImage:
            source:app.path
            size_hint:(None,None)
            height:dp(120)
            width:dp(120)
            radius:dp(self.width)
            pos_hint:{'center_x':0.5, 'top':0.5}
        MDLabel:
            text: 'Zendaya'
            font_style:'Body1'
            font_size:dp(24)
            size_hint_y:None
            height: self.texture_size[1]+dp(10)
            halign:'center'
        MDLabel:
            text:'Model & Actor'
            font_style:'Body2'
            font_size:dp(16)
            size_hint_y:None
            height:self.texture_size[1]+dp(8)
            halign:'center'
           
    MDFloatLayout:
        size_hint:(1,0.7)
        pos_hint:{'top':0.7}
        MDLabel:
            text:'(+258)12345678'
            font_style:'H4'
            halign:'center'
            pos_hint:{'center_x':0.5,'top':1.4}
        MDLabel:
            text:'INCOMING CALL'
            font_style:'Caption'
            font_size:dp(12)
            halign:'center'
            pos_hint:{'center_x':0.5,'top':1.35}
        MDIcon:
            icon:'chevron-up'
            font_size:dp(28)
            pos_hint:{'center_x':0.5, 'top':0.64}
            theme_text_color:'Custom'
            text_color:'green'
        MDIcon:
            icon:'chevron-up'
            font_size:dp(34)
            pos_hint:{'center_x':0.5, 'top':0.60}
            theme_text_color:'Custom'
            text_color:'green'
        MDIcon:
            icon:'chevron-up'
            font_size:dp(40)
            pos_hint:{'center_x':0.5, 'top':0.56}
            theme_text_color:'Custom'
            text_color:'green'
        RecieverButton:
            id:receive_button
            icon:'phone'
            elevation:5
            icon_size:dp(36)
            theme_text_color:'Custom'
            text_color:'green'
            md_bg_color:'white'if app.theme_cls.theme_style == 'Dark' else app.theme_cls.primary_light
            pos_hint:{'center_x':0.5, 'top':0.5}
        MDIcon:
            icon:'chevron-down'
            font_size:dp(40)
            pos_hint:{'center_x':0.5, 'top':0.4}
            theme_text_color:'Custom'
            text_color:'red'
        MDIcon:
            icon:'chevron-down'
            font_size:dp(34)
            pos_hint:{'center_x':0.5, 'top':0.36}
            theme_text_color:'Custom'
            text_color:'red'
        MDIcon:
            icon:'chevron-down'
            font_size:dp(28)
            pos_hint:{'center_x':0.5, 'top':0.32}
            theme_text_color:'Custom'
            text_color:'red'
        MDIcon:
            icon:'clock'
            font_size:dp(28)
            pos_hint:{'right':0.1, 'top':0.1}
            theme_text_color:'Custom'
            text_color:app.theme_cls.primary_dark
        MDIcon:
            icon:'message'
            font_size:dp(28)
            pos_hint:{'right':0.9, 'top':0.1}
            theme_text_color:'Custom'
            text_color:app.theme_cls.primary_dark
           
           
        
        
       
"""
class RecieverButton(MDIconButton):
    moved_state = BooleanProperty()
   
    def on_touch_up(self, touch):
        app = App.get_running_app()
        if self.collide_point(*touch.pos):
            if self.moved_state:
                 app.stop_animation()
            else:
                app.animate_call()
            
        
    def on_touch_move(self, touch):
        
        if self.collide_point(*touch.pos):
            self.moved_state = True
            pos_y = self.pos[1]
            touch_y = touch.pos[1]
            
            diff = abs(pos_y - touch_y)
            print('Difference', diff)
            if diff >= 50 :
                # move up
                anim = Animation(pos_hint = {'top':0.6}).start(self)
                print('call received', self.moved_state)
            else:
                # move down
                anim = Animation(pos_hint = {'top':0.4}).start(self)
                print('call disconnected', self.moved_state)
        else:
                self.moved_state = False
                
                
            
            
            
class CallerApp(MDApp):
    @property
    def path(self):
        import os
        img_path = os.path.join(os.path.dirname(__file__), 'girl.jpeg')
        return img_path
    def build(self):
        return Builder.load_string(kv)
    def animate_call(self):
        
        print('animating', self.call_btn.x)
        
        self.anim.repeat = True
        self.anim.start(self.call_btn)
        
    def stop_animation(self):
        self.anim.stop(self.call_btn)
       
        
        
    def on_start(self):
       self.theme_cls.theme_style= 'Dark'
       self.anim = Animation(pos_hint={'top':0.48}, duration=0.3)+Animation(pos_hint={'top':0.52}, duration=0.3)
       self.call_btn = self.root.ids.receive_button
       self.animate_call()
        
        
if __name__ == '__main__':
    CallerApp().run()