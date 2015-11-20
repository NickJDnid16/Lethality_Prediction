'''
Created on 25 Oct 2015

@author: nid16
'''


import re
import codecs

GraphInput = open('./GO_Children&Parents.txt', mode='r')

outputfile = open('./GO_Nodes.txt', mode='w')

GO_Seen = set()

outputfile.truncate ()
for line in GraphInput:
    if "GO" in line:
        if line not in GO_Seen:           
            GO = line.split('""')
            matches = re.findall(r'\"(.+?)\"',GO[0])
            join = '\n'.join(matches)
            
            print(join)
            outputfile.write(join+'\n')
            
            GO_Seen.add(join+'\n')
outputfile.close()


NodesInput = open('./GO_Nodes.txt', mode='r')

NodesOutput = open('./Refined_GO_Nodes.txt', mode='w')

Nodes_Seen = set()

NodesOutput.truncate()

for line in NodesInput:
    if line not in Nodes_Seen:
        NodesOutput.write(line)
        
        Nodes_Seen.add(line)
        
NodesOutput.close()














