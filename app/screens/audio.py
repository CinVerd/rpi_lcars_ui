# Handles logic related to generating audio buttons, and them being pressed
import vlc
from ui.widgets.lcars_widgets import *

# 0 - val
# 1 - 97
# 2 - Nova
valColour = colours.PEACH
nineSevenColour = colours.PEACH
novaColour = colours.PEACH

activeColour = colours.GREY_BLUE


def initialize(self, all_sprites):
    all_sprites.add(LcarsButton(colours.PEACH, (200, 127), "VAL", self.audio_handler_play_val),
                    layer=4)
    self.section_audio_sources_val = vlc.MediaPlayer("http://radio.doubleclic.fr/radiovaldisere.mp3")

    all_sprites.add(LcarsButton(colours.PEACH, (258, 127), "97", self.audio_handler_play_97),
                    layer=4)
    self.section_audio_sources_97 = vlc.MediaPlayer("http://19763.live.streamtheworld.com/977_80.mp3")

    all_sprites.add(LcarsButton(colours.PEACH, (316, 127), "NOVA", self.audio_handler_play_nova),
                    layer=4)
    self.section_audio_sources_nova = vlc.MediaPlayer("https://stream.audioxi.com/NOVA")

    self.section_audio_sprites = all_sprites.get_sprites_from_layer(4)
    hideAudioSection(self)


def show_audio_section(self):
    if not self.section_audio_sprites[0].visible:
        for sprite in self.section_audio_sprites:
            sprite.visible = True


def hideAudioSection(self):
    if self.section_audio_sprites[0].visible:
        for sprite in self.section_audio_sprites:
            sprite.visible = False


def play_val(self):
    if not self.section_audio_sources_val.is_playing():
        self.section_audio_sources_val.play()
        # set button colour
        set_active_button(self, 0)
    else:
        self.section_audio_sources_val.stop()
        # set button color
        self.section_audio_sprites[0].changeColour(valColour)


def play_97(self):
    if not self.section_audio_sources_97.is_playing():
        self.section_audio_sources_97.play()
        # set button colour
        set_active_button(self, 1)
    else:
        self.section_audio_sources_97.stop()
        # set button color
        self.section_audio_sprites[1].changeColour(nineSevenColour)


def play_nova(self):
    if not self.section_audio_sources_nova.is_playing():
        self.section_audio_sources_nova.play()
        # set button colour
        set_active_button(self, 2)
    else:
        self.section_audio_sources_nova.stop()
        # set button color
        self.section_audio_sprites[2].changeColour(novaColour)


def set_active_button(self, number):
    self.section_audio_sprites[0].changeColour(valColour)
    self.section_audio_sprites[1].changeColour(nineSevenColour)
    self.section_audio_sprites[2].changeColour(novaColour)

    self.section_audio_sprites[number].changeColour(activeColour)
