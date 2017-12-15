import random
import sys
sys.path.insert(0, '/home/HypothesisTest/')

from hypoclient import HypoClient
from hypothesis import given, example
from hypothesis.strategies import text

sock = HypoClient.SockConnect()

@given(s=text())
@example(s='')
def test1(s):
    '''HypoClient.SockSendAll(s.encode('utf-8'))'''
    print("test1:" + s)

def sendCommand():
    selectCommand = ['create and commit once', 'create and commit twice', 'create and commit thrice']
    randomChoice = random.choice(selectCommand)
    print(randomChoice)
    HypoClient.SockSendAll(randomChoice.encode('utf-8'))
    
if __name__ == '__main__':
    '''test1()'''
    sendCommand()




'''HypoClient.SockSendAll(b"Hello\n")'''

receivedData=HypoClient.SockReceive(sock)

'''Print("test:" + receivedData.decode('utf-8'))'''

HypoClient.SockClose()



