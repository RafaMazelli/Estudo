from pygame import mixer

mixer.init()
mixer.music.load('testesick.mp3')
mixer.music.play()
input('\33[31mAgora voce escuta?')