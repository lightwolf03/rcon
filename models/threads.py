import threading, time, datetime
from models.log import log
from models.const import MAPS, GAMETYPES
from queue import Queue
from PySide import QtGui

class Daemon(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stoped = True
        log("Daemon initialiazed")

    def run(self):
        from models.const import VARS
        self._stoped = False
        while self._stoped != True:
            VARS.worker.do(self.updateSTATUS)
            time.sleep(8)

    def stop(self):
        self._stoped = True
        log("Daemon stopped")

    def update(self):
        self.updateSTATUS()

    def updateSTATUS(self):
        from models.const import VARS
        try:
            recv = VARS.connection.response(128)
            print("Last string", recv)
            PLAYERS, MAP = VARS.connection.getStatus()
            print("status OK", datetime.datetime.now())
        except TypeError:
            MAP = None;
        if MAP != None:
            VARS.window.labelMAP.setText(MAPS[MAP])
            VARS.window.tablePLAYERS.clearContents()
            for player in PLAYERS:
                num = QtGui.QTableWidgetItem(player.num)
                name = QtGui.QTableWidgetItem(player.name)
                score = QtGui.QTableWidgetItem(player.score)
                guid = QtGui.QTableWidgetItem(player.guid)
                ping = QtGui.QTableWidgetItem(player.ping)
                VARS.window.tablePLAYERS.setItem(int(player.num),0, num)
                VARS.window.tablePLAYERS.setItem(int(player.num), 1, name)
                VARS.window.tablePLAYERS.setItem(int(player.num), 2, score)
                VARS.window.tablePLAYERS.setItem(int(player.num), 3, guid)
                VARS.window.tablePLAYERS.setItem(int(player.num), 4, ping)
        try:
            recv = VARS.connection.response(128)
            print("Recv", recv)
            GT = VARS.connection.getServerInfo()
            if GT != None:
                VARS.window.labelGT.setText(GAMETYPES[GT])
                print("serverinfo OK")
        except Exception:
            pass
        VARS.window.listWidget.clear()
        for player in VARS.players:
            VARS.window.listWidget.addItem(player.name)



class DaemonWorker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stoped = False
        self.queue = Queue()

    def do(self, task):
        self.queue.put(task)

    def run(self):
        while self._stoped != True:
            self.work()

    def work(self):
        from models.const import VARS
        VARS.locker.acquire()
        if self.queue.empty() != True:
            working = self.queue.get()
            try:
                log("work start")
                working()
                self.queue.task_done()
                log("work end")
            except TypeError:
                log("work end without work")
        VARS.locker.release()