#-*- coding: utf-8 -*-
import socket, time
from models.parsers import parseStatus, parseServerInfo
from models.log import log
start = b"\xFF\xFF\xFF\xFF"
end   = b"\x00"

def encode(command):
    bytestring = start + command.encode() + end
    return bytestring
    

class RconConnection(object):
    def __init__(self, ip, port, password):
        self.ip       = ip
        self.port     = port
        self.password = password
        self.socket   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(3)

    def connect(self):
        try:
            self.socket.connect(("%s" % (self.ip), int(self.port)))
            log("Socket connected")
        except:
            log("Could not connect")
            log("%s %s" % (self.ip, self.port))

    def auth(self):
        string = "login %s" % (self.password)
        command = encode(string)
        self.socket.send(command)

    def send(self, command):
        time.sleep(1)
        string = "rcon %s %s" % (self.password, command)
        string = encode(string)
        log("%s : %s" % ("Sended string", string))
        self.socket.send(string)
        
    def response(self, size):
        try:
            string = self.socket.recv(size)
            log("%s %s" % ("Raw response", string[10:20]))
            string = string[10:]
            string = string.decode()
            if "The server must set 'rcon_password' for clients to use 'rcon'" in string:
                log("rcon_password is not set")
                return None
            else:
                return string
        except:
            print("No response")
            return None
            

    def closeConnect(self):
        self.socket.close()
        log("Socket disconnected")

    def sendRaw(self, command):
        self.socket.send(command)

    def getStatus(self):
        self.send("status")
        log("status started")
        response = self.response(1024)
        if response != None:
            players, mp_map = parseStatus(response)
            if players and mp_map:
                log("%s %s" % (players, mp_map))
            else:
                log("Failed getStatus")
            return players, mp_map

    def getServerInfo(self):
        self.send("serverinfo")
        log("serverinfo started")
        response = self.response(1024)
        response = response[22:]
        if response != None:
            result = parseServerInfo(response)
            return result

    def changeGameType(self, string):
        log("start changing gt")
        self.send("g_gametype %s" % (string))
        response = self.response(256)
        log("changing gt: response OK")
        if "g_gametype will be changed upon restarting" in response:
            self.send("fast_restart")
            log("fast restarted")


# class Connection(threading.Thread):
#     def __init__(self, connection):
#         threading.Thread.__init__(self)
#         self.connection = connection
#         self.queue = queue.Queue()

#     def working(self):
#         from models.const import VARS
#         while self._stopped != True:
#             VARS.locker.acquire()
#             work = self.queue.get()
#             work()
#             self.queue.task_done()
#             VARS.locker.release()

#     def do(self, work):
#         self.queue.put(work)

#     def getStatus(self):
#         ret = self.connection.getStatus()
#         return ret

#     def getServerInfo(self):
#         ret = self.connection.getServerInfo()
#         return ret