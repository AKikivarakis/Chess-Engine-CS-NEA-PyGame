class Move():

    def __init__(self, oPos, nPos):
        
        self.oPos = oPos
        self.nPos = nPos

    def getOPos(self):
        # Get start position
        return self.oPos

    def getNPos(self):
        # Get end position
        return self.nPos
