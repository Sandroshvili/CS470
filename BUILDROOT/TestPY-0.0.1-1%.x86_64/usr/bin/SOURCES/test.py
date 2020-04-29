#!/usr/bin/python2.7
import sys
if len(sys.argv)>1:
	print "We read only one argument, though you might have provided many more of them %s"%(str(sys.argv[1]))
else:
	print "Hello There You can pass 1 argument from command line to me"
	print "The script has the name %s" %(sys.argv[0])

