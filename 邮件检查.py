#!/usr/bin/python

#-*- encoding: utf-8 -*-

import imaplib
import re


def gmail_checker(mailhost, username, password, flag = 0):
	i=imaplib.IMAP4_SSL(mailhost)
	try:
		i.login(username, password)
		x, y=i.status('INBOX', '(MESSAGES UNSEEN)')
		messages=int(re.search('MESSAGES\s+(\d+)', y[0]).group(1))
		unseen=int(re.search('UNSEEN\s+(\d+)', y[0]).group(1))
		print "-------------------------------------------------"
		print "%s : total %i messages, %i unseen." % (username, messages, unseen)

				
	finally:
		i.logout()

if __name__ == '__main__':
	gmail_checker('imap.163.com', '--------------', '---------', 1)
	gmail_checker('imap.qq.com','----------','-------------',1)
	gmail_checker('imap.gmail.com', '------------', '---------',1)
	gmail_checker('imap-mail.outlook.com', '----------','----------', 1)