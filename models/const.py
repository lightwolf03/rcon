MAPS = {
    "mp_abandon" : "Carnival",
    "mp_afghan" : "Afghan",
    "mp_boneyard" : "Scrapyard",
    "mp_brecourt" : "Wasteland",
    "mp_checkpoint" : "Karachi",
    "mp_compact" : "Salvage",
    "mp_complex" : "Bailout",
    "mp_crash" : "Crash",
    "mp_derail" : "Derail",
    "mp_estate" : "Estate",
    "mp_favela" : "Favela",
    "mp_fuel2" : "Fuel",
    "mp_highrise" : "Highrise",
    "mp_invasion" : "Invasion",
    "mp_nightshift" : "Skidrow",
    "mp_overgrown" : "Overgrown",
    "mp_quarry" : "Quarry",
    "mp_rundown" : "Rundown",
    "mp_rust" : "Rust",
    "mp_storm" : "Storm",
    "mp_strike":"Strike",
    "mp_subbase" : "Sub Base",
    "mp_terminal" : "Terminal",
    "mp_trailerpark" : "Trailer Park",
    "mp_underpass" : "Underpass",
    "mp_vacant" : "Vacant",
}

GAMETYPES = {
    "dm" : "DeathMatch",
    "tdm" : "Team DeathMatch",
    "sd" : "Search and Destroy",
    "ctf" : "Capture the Flag",
    "war" : "War",
}

class GlobalVars(object):
    def __init__(self, connection, mp, gt, players, daemon, worker, locker, queue):
        self.connection = connection
        self.map = mp
        self.gt = gt
        self.players = players
        self.daemon = daemon
        self.worker = worker
        self.window = None
        self.locker = locker
        self.queue = queue

from models.threads import DaemonWorker
from threading import RLock
from queue import Queue

CONNECTION = None; MAP = None; GT = None; PLAYERS = None
DAEMON = None; WORKER = DaemonWorker(); LOCKER = RLock(); QUEUE = Queue()
VARS = GlobalVars(CONNECTION, MAP, GT, PLAYERS, DAEMON, WORKER, LOCKER, QUEUE)