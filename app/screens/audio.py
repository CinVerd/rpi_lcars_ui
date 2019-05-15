# Handles logic related to audio buttons being pressed


def play_val(self):
    print "what"
    if not self.section_audio_sources_val.is_playing():
        # Sound("http://radio.doubleclic.fr/radiovaldisere.mp3").play()
        # p = vlc.MediaPlayer("http://radio.doubleclic.fr/radiovaldisere.mp3")
        self.section_audio_sources_val.play()
        #self.section_audio_radio_image.visible = True
    else:
        self.section_audio_sources_val.stop()
        #self.section_audio_radio_image.visible = False
