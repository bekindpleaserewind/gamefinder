from PySide6.QtCore import QObject, Signal

class AppSignals(QObject):
    notify = Signal(tuple)
    data = Signal(list)
    error = Signal(str)

class WorkerSignals(QObject):
    notify = Signal(tuple)
    data = Signal(list)
    error = Signal(str)

class GameFinderSignals(QObject):
    notify = Signal(tuple)
    data = Signal(list)
    error = Signal(str)

class SettingsSignals(QObject):
    reload = Signal(bool)