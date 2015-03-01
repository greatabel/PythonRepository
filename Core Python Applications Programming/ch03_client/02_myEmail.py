#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = '172.24.0.11'
POP3SVR = '172.24.0.11'

who = 'awan@movoto.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg

Hello World! from python
''' % {'who': who}

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)    # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('awan')
recvSvr.pass_('42Murloc')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
print 'recvBody=',recvBody
#assert origBody == recvBody # assert identical
