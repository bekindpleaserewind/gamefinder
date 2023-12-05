import os
import sys

from appinfo import Info

class Logo:
    small = False
    normal = False

class Music:
    games = False

class Icon:
    online = False
    offline = False
    start = False
    stop = False
    tally = False
    trash = False
    platform = False
    credentials = False
    settings = False

class Pathinfo:
    # file paths
    app = os.path.join(os.environ['APPDATA'], Info.APPNAME)
    state = os.path.join(app, 'state.yaml')
    settings = os.path.join(app, 'settings.yaml')
    platforms = os.path.join(app, 'platforms.yaml')
    aspectfilters = os.path.join(app, 'aspectfilters.yaml')
    itemfilters = os.path.join(app, 'itemfilters.yaml')
    ebay = os.path.join(app, 'ebay.yaml')

    logo = Logo
    icon = Icon
    music = Music

    def __init__(self):
        if Info.FROZEN:
            self.icondir = sys._MEIPASS
            self.musicdir = os.path.join(sys._MEIPASS, 'alerts')
        else:
            self.musicdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'alerts')
            self.icondir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')

        self.logo.small = os.path.join(self.icondir, 'gamefinder_logo_whitebackground_small.png')
        self.logo.normal = os.path.join(self.icondir, 'gamefinder_logo_whitebackground.png')
        self.icon.online = os.path.join(self.icondir, 'online.png')
        self.icon.offline = os.path.join(self.icondir, 'offline.png')
        self.icon.start = os.path.join(self.icondir, 'start.png')
        self.icon.stop = os.path.join(self.icondir, 'stop.png')
        self.icon.tally = os.path.join(self.icondir, 'tally.png')
        self.icon.trash = os.path.join(self.icondir, 'trash.png')
        self.icon.platform = os.path.join(self.icondir, 'platforms.png')
        self.icon.credentials = os.path.join(self.icondir, 'credentials.png')
        self.icon.settings = os.path.join(self.icondir, 'settings.png')
        self.music.games = os.path.join(self.musicdir, 'games.mp3')