from datetime import datetime
import pygame
from pygame.mixer import Sound
import vlc
import audio
from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse

# Two aspects:
# Init sprites / UI stuff/
# Init logical objects - handlers, behind UI stuff

# 1. Init everything, default to set of "main" sprites
# 2. On menu button press, hide all sprites, show specific ones. - Button handler does this
# 2.1On sub item press, perform logic. - specific button logic does this
# 3. How know when specific button is pressed - handler is defined for a widget. Button is subtype of widget


class ScreenMain(LcarsScreen):
    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_1.png"),
                        layer=0)
        
        # panel text
        all_sprites.add(LcarsText(colours.BLACK, (15, 44), "LCARS 105"),
                        layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "HOME AUTOMATION", 2),
                        layer=1)
        # ----------- Main Menu Buttons - move when more than one screen, move to parent class
        all_sprites.add(LcarsBlockMedium(colours.RED_BROWN, (145, 16), "MAIN"),
                        layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (211, 16), "SETTINGS"),
                        layer=1)
        all_sprites.add(LcarsBlockLarge(colours.BEIGE, (249, 16), "ENERGY"),
                        layer=1)

        # ----------- Main Menu Buttons End
        all_sprites.add(LcarsText(colours.BLACK, (444, 612), "192 168 0 3"),
                        layer=1)

        # date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "STAR DATE 2711.05 17:54:32", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # sub buttons - layer 2
        # Distance of 135 on y axis seems good
        # Move to super class
        all_sprites.add(LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT", self.logoutHandler),
                        layer=2)
        # -----------------------------------------------------------------------------------------
        all_sprites.add(LcarsButton(colours.BEIGE, (107, 127), "LIGHTS", self.lights_handler),
                        layer=2)
        all_sprites.add(LcarsButton(colours.PURPLE, (107, 262), "AUDIO", self.audio_handler),
                        layer=2)
        all_sprites.add(LcarsButton(colours.PEACH, (107, 398), "SENSORS", self.sensors_handler),
                        layer=2)
        all_sprites.add(LcarsButton(colours.ORANGE, (107, 533), "PENDING", self.sensors_handler),
                        layer=2)

        # Audio -------------------------------------------------------------------------------
        # Move to own section
        # Audio Buttons - layer 4
        audio.initialize(self, all_sprites)
        # all_sprites.add(LcarsButton(colours.PEACH, (200, 127), "VAL", self.audio_handler_play_val),
        # layer=4)

        # self.section_audio_sprites = all_sprites.get_sprites_from_layer(4)

        # Audio Logic
        # self.section_audio_sources_val = vlc.MediaPlayer("http://radio.doubleclic.fr/radiovaldisere.mp3")
        # self.section_audio_radio_image = LcarsImage("assets/make_it_snow.jpg", (150, 122))
        # self.section_audio_radio_image.visible = False
        # all_sprites.add(self.section_audio_radio_image, layer=4)

        # -------------------------------------------------------------------------------------

        # gadgets

        self.weather = LcarsImage("assets/weather.jpg", (188, 122))
        self.weather.visible = False
        all_sprites.add(self.weather, layer=2) 

        # all_sprites.add(LcarsMoveToMouse(colours.WHITE), layer=1)
        self.beep1 = Sound("assets/audio/panel/201.wav")
        Sound("assets/audio/panel/220.wav").play()

    def hideAll(self):
        audio.hide_audio_section(self)

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("STAR DATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)
        
    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False


    def weatherHandler(self, item, event, clock):
        self.hideAll()
        self.weather.visible = True

    def audio_handler(self, item, event, clock):
        self.hideAll()
        audio.show_audio_section(self)
        self.weather.visible = False

    def audio_handler_play_val(self, item, event, clock):
        audio.play_val(self)

    def audio_handler_play_97(self, item, event, clock):
        audio.play_97(self)

    def audio_handler_play_nova(self, item, event, clock):
        audio.play_nova(self)

    def lights_handler(self, item, event, clock):
        print "Not implemented."

    def sensors_handler(self, item, event, clock):
        print "Not implemented."
    
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())
    
    
