from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Cop from %s to %s " %(from_file,to_file)

# We could do these two on one line too, how?
input=open(from_file)
indata=input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready , hit return to continue ,ctrl+C to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "Alright,all done."
out_file.close()
input.close()		
