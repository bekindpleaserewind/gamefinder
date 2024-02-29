from datetime import datetime
from signals import ConsoleSignals

LEVEL_INFO = "INFO"
LEVEL_WARN = "WARN"
LEVEL_ERR = "ERR"
LEVEL_CRIT = "CRIT"
LEVEL_DEBUG = "DEBUG"

class LogLevel:
    info = 10
    warn = warning = 20
    err = error = 30
    crit = critical = 40
    debug = 50

class Console:
    level = LogLevel()
    signals = ConsoleSignals()

    def __init__(self):
        self.logLevel = False
        self.firstMessage = False
        self.setLevel(self.level.info)
        self.output = ""

    def setLevel(self, level):
        self.logLevel = level

    def log(self, msg, level = False):
        if level:
            self.signals.message.emit((level, msg,))
            return True
        self.signals.message.emit((self.logLevel, msg,))
    
    def info(self, msg):
        self.log(msg, self.level.info)
    
    def warn(self, msg):
        self.log(msg, self.level.warn)

    def err(self, msg):
        self.log(msg, self.level.err)
    
    def crit(self, msg):
        self.log(msg, self.level.crit)
    
    def debug(self, msg):
        self.log(msg, self.level.debug)
    
    def toString(self, data):
        level, message = data

        if self.firstMessage is False:
            self.output = "{:22}{:6}{}".format('[' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ']', self.levelToString(level), message,)
            self.firstMessage = True
        else:
            self.output = "{}<br>{:22}{:6}{}".format(self.output, '[' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ']', self.levelToString(level), message,)

        return self.output
 
    def levelToString(self, level):
        if level == self.level.info:
            return LEVEL_INFO
        if level == self.level.warn:
            return LEVEL_WARN
        if level == self.level.err:
            return LEVEL_ERR
        if level == self.level.crit:
            return LEVEL_CRIT
        if level == self.level.debug:
            return LEVEL_DEBUG