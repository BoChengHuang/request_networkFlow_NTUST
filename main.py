from modules.requestFlow import RequestFlow
import sys
import socket
import time

if __name__ == '__main__':
	argvList = sys.argv
	if len(argvList) == 1:
		IP = socket.gethostbyname(socket.gethostname())
		rf = RequestFlow()
		textToSend = "Today flow(s): "+str(rf._requestFlow(IP, rf._getFields()))
		print textToSend
	else:
		if "140.118" in argvList[1]:
			rf = RequestFlow()
			textToSend = "Today flow(s): "+str(rf._requestFlow(argvList[1], rf._getFields()))
			print textToSend
		elif argvList[1] == "loop":
			rf = RequestFlow()
			IP = socket.gethostbyname(socket.gethostname())
			while(1):
			    total = rf._requestFlow(IP, rf._getFields())
			    textToSend = "Today flow(s): "+str(total)
			    print textToSend
			    if float(total[:-3].replace(',','')) > 4500:
			        print 'Warining!!'
			    time.sleep(600)
		else:
			print "This is just for NTUST request..."