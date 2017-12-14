import sys
sys.path.insert(0, '/home/HypothesisTest/')

from hypoclient import HypoClient
from hypothesis import given, example
from hypothesis.strategies import text

sock = HypoClient.SockConnect()

@given(s=text())
@example(s='')
def test1(s):
    HypoClient.SockSendAll(s.encode('utf-8'))
    print("test1:" + s)

if __name__ == '__main__':
    test1()


'''HypoClient.SockSendAll(b"Hello\n")'''

receivedData=HypoClient.SockReceive(sock)

'''Print("test:" + receivedData.decode('utf-8'))'''

HypoClient.SockClose()



