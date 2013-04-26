class Player(object):
    def __init__(self, num, score, ping, guid, name, lastmsg, address, qport, rate):
        self.num     = num
        self.score   = score
        self.ping    = ping
        self.guid    = guid
        self.name    = name
        self.lastmsg = lastmsg
        self.address = address
        self.qport   = qport
        self.rate    = rate

    def __repr__(self):
        return "<Player: name %s, GUID %s, address %s" % (self.name, self.guid, self.address)