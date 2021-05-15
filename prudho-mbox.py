#!/usr/bin/env python3

import email
from email.policy import default

class MboxReader:
    def __init__(self, filename):
        self.handle = open(filename, 'rb')
        assert self.handle.readline().startswith(b'From ')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle.close()

    def __iter__(self):
        return iter(self.__next__())

    def __next__(self):
        lines = []
        while True:
            line = self.handle.readline()
            if line == b'' or line.startswith(b'From '):
                yield email.message_from_bytes(b''.join(lines), policy=default)
                if line == b'':
                    break
                lines = []
                continue
            lines.append(line)

with MboxReader("test.mbox") as mbox:
    for message in mbox:

        dateList = message.get_all("Date")
        toList = message.get_all("To")
        ccList = message.get_all("CC")
        fromList = message.get_all("From")
        subjectList = message.get_all("Subject")

        if(dateList is None):
           dateList=[]

        if(toList is None):
           toList=[]

        if(fromList is None):
           fromList=[]

        if(subjectList is None):
           subjectList=[]
        if(ccList is None):
           ccList=[]

        #print(fromList)
        #print(subjectList)
        #print(dateList)
        #print(toList)
        #print(ccList)
        #print("--------------------\n")
        
        separator = ', '
        print(separator.join(dateList)+"£"+separator.join(fromList)+"£"+separator.join(subjectList)+"£"+separator.join(toList)+"£"+separator.join(ccList))
