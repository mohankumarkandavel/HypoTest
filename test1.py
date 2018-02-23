# -*- coding: utf-8 -*-

import random
import sys
import re
sys.path.insert(0, 'C:/Users/mkan839/Documents/new/HypothesisTest/')

from hypoclient import HypoClient
from hypothesis.strategies import characters, text, integers
from hypothesis import given, example, settings
from unicodedata import category


sock = HypoClient.SockConnect()
s_string = []
c_commit = []
c_commitByte = []
s_commitString = []
c_commitHash = []

s = text(
    characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size=1).map(lambda l: l.strip()).filter(lambda l: len(l) > 0)
c = text(
    characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size=1).map(lambda l: l.strip()).filter(lambda l: len(l) > 0)
cb = integers(min_value=1,max_value=99)
cs = integers(min_value=1,max_value=99)
	
@given(s)
@settings(max_examples=100)
def stringBase(s):
    '''s = re.sub(r'(\n+)', r" ", s)
    s = re.sub(r'(\x00-\xff)', r"", s)'''
    inputString=b'New String '+ s.encode('utf-8')
    '''print(s.encode('utf-8'))'''
    HypoClient.SockSendAll(inputString)
    ''''data = sock.recv(1024)
    data1=str(data).replace('\\r\\n','')
    data2=data1.replace("b", '')
    print(data2.replace("'", ''))'''
    '''if s == data2.replace("'", '') :
        print('pass')
    assert s == data2.replace("'", '')'''
    s_string.append(s)
    if len(s_string) ==100 :
        commitBase()

@given(c)
@settings(max_examples=100)
def commitBase(c):
    '''s = re.sub(r'(\n+)', r" ", s)
    s = re.sub(r'(\x00-\xff)', r"", s)'''
    inputCommit=b'New Commit '+ c.encode('utf-8')
    '''print(s.encode('utf-8'))'''
    HypoClient.SockSendAll(inputCommit)
    ''''data = sock.recv(1024)
    data1=str(data).replace('\\r\\n','')
    data2=data1.replace("b", '')
    print(data2.replace("'", ''))'''
    '''if s == data2.replace("'", '') :
        print('pass')
    assert s == data2.replace("'", '')'''
    c_commit.append(c)
    if len(c_commit) ==100 :
        newRepo()

def newRepo():
    inputRepo='New Repo'
    HypoClient.SockSendAll(inputRepo.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    repoCommit()

@given(cb,cs)
@settings(max_examples=10)
def repoCommit(cb,cs):
    inputRepoCommit='Repo Commit Repo/0 Byte/'+str(cb)+' String/'+str(cs)
    '''inputRepoCommit=b'Repo Commit Repo/0 Byte/0 String/0'''
    HypoClient.SockSendAll(inputRepoCommit.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    c_commitByte.append(cb)
    s_commitString.append(cs)
    c_commitHash.append(data.decode('utf-8'))
    if len(c_commitByte) == 10 :
        commitTest()
		
def commitTest():
    inputCommitTest='Repo Show Repo/0 Commit/'+str(random.randint(0,len(c_commitHash)))
    '''inputCommitTest='Repo Show Repo/0 Commit/'+str(random.randint(1,len(c_commitHash)))+' String/'+str(random.choice(s_commitString))HypoClient.SockSendAll(inputCommitTest.encode('utf-8')) '''  
    HypoClient.SockSendAll(inputCommitTest.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    inputClose='Close'
    HypoClient.SockSendAll(inputClose.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
	

'''@given(s=text(min_size=5),c=text(min_size=5))
def sendCommand(s,c):
    inputCommand = input("Enter command here: ")
    inputC='New Repo'
    print(inputC)
    HypoClient.SockSendAll(inputC.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        data1=str(data.decode('utf-8')).strip()
        if (data1.startswith('Repo')):
            inputString='New String '+ s
            print('hypo String' + s)
            HypoClient.SockSendAll(inputString.encode('utf-8'))		
        elif data1.startswith('String') :
            inputByte='New Commit '+ c
            print('hypo commit' + c)
            HypoClient.SockSendAll(inputByte.encode('utf-8'))
        elif data1.startswith('Commit') :
            inputRepoCommit='Repo Commit Repo/0 Byte/0 String/0'
            HypoClient.SockSendAll(inputRepoCommit.encode('utf-8'))
        elif data1.startswith('Hash') :
            inputByte='Repo Show Repo/0 Commit/0 String/0'
            HypoClient.SockSendAll(inputByte.encode('utf-8'))
        elif data1.startswith('Show') :
            inputClose='Close'
            HypoClient.SockSendAll(inputClose.encode('utf-8'))	
        elif data1.startswith('Close') :	
            sock.SockClose()
            break;
        elif data1.startswith('Clear') :
            inputClear='Clear'
            HypoClient.SockSendAll(inputClear.encode('utf-8'))
        else :
            print('Error Try Again')
            break;'''
    
    
    
if __name__ == '__main__':
    stringBase()
    '''sendCommand()'''


'''receivedData=HypoClient.SockReceive(sock)
Print("test:" + receivedData.decode('utf-8'))
HypoClient.SockClose()'''

'''HypoClient.SockSendAll(b"Hello\n")'''





