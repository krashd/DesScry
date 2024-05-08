class Node:
    nodeID = ""
    nodeType = "rag"
    signalType = "001"
    serialNumber = ""
    poleNumber = 0
    cabinetNumber = 0
    cicNumber = 0
    ctbCommsChannel = "R1"
    spurredFrom = ""
    orderID = 0
    text = ""
    nodeSpecificData = []



class RAGData:
    phase = ""
    ledPlateList = []
    solarCell = "not_fitted"
    detectorInputList = []



class NearSideData:
    nearsideType = ""
    phase = ""



class WaitPDUData:
    def __init__(self, phase, audible, tactile, pushButtonInputName):
        self.phase = phase
        self.audible = audible
        self.tactile = tactile
        self.pushButtonInputName = pushButtonInputName



class Detector:
    inputName = ""
    inputIndex = 0



class SmartLoopData:
    phase = ""
    loopInputList = []



p1e1 = Node()
p1e1.signalType = "HD80F"
p1e1.nodeType = "pdu"
p1e1.cabinetNumber = 1
p1e1.cicNumber = 1
p1e1.ctbCommsChannel = "R1"
p1e1.orderID = 1
p1e1.text = "PB"
#p1e1.nodeSpecificData.append(WaitPDUData("E", "not_fitted", "not_fitted", "EPBU1"))
#p1e1.nodeSpecificData.append(WaitPDUData("E", "not_fitted", "not_fitted", "EPBU2"))

if (len(p1e1.nodeSpecificData) > 0):
    for obj in p1e1.nodeSpecificData:
        print(obj.pushButtonInputName)
else:
    print("No node data present")