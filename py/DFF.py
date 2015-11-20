DFFList = []


def DFFTick():
    for i in DFFList:
        i.tick()


class DFF():

    def __init__(self):
        DFFList.append(self)
        
