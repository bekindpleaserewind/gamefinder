from PySide6.QtCore import QObject, Signal

class AppSignals(QObject):
    notify = Signal(tuple)
    data = Signal(list)

class WorkerSignals(QObject):
    notify = Signal(tuple)
    data = Signal(list)

class GameFinderSignals(QObject):
    notify = Signal(tuple)
    data = Signal(list)

class SettingsSignals(QObject):
    reload = Signal(bool)