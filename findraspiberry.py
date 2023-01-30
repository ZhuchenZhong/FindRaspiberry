import os

lines = [line.split() for line in os.popen('arp -a').readlines() if line]
for line in lines:
    try:
        if line[1].startswith('28:cd:c1') or \
           line[1].startswith('b8:27:eb') or \
           line[1].startswith('e4:5f:01'):
            print(line[0])
        #else:
            #print("Found OTHER: ", line[0], ' : ', line[1])
    except IndexError:pass

