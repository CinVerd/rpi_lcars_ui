from ui.widgets.lcars_widgets import *
import requests

def initialize(self, all_sprites):
    all_sprites.add(LcarsButton(colours.PEACH, (200, 127), "LIGHTS ON", self.lights_handler_main_on),
                    layer=5)

    all_sprites.add(LcarsButton(colours.BLUE, (280, 127), "LIGHTS OFF", self.lights_handler_main_off),
                    layer=5)

    self.section_lights_sprites = all_sprites.get_sprites_from_layer(5)
    hide_lights_section(self)


def show_lights_section(self):
    if not self.section_lights_sprites[0].visible:
        for sprite in self.section_lights_sprites:
            sprite.visible = True


def hide_lights_section(self):
    if self.section_lights_sprites[0].visible:
        for sprite in self.section_lights_sprites:
            sprite.visible = False


def main_light_on(self):
    print("on")
    # Python is cool sometimes.
    r = requests.get('http://localhost:1138/1251/mainlight/on')


def main_light_off(self):
    print("off")
    r = requests.get('http://localhost:1138/1251/mainlight/off')