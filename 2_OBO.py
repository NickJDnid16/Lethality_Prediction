import codecs

def getDescendents(goid):
  recursiveArray = [goid]
  if terms.has_key(goid):
    children = terms[goid]['c']
    if len(children) > 0:
      for child in children:
        recursiveArray.extend(getDescendents(child))

  return set(recursiveArray)

def getAncestors(goid):
  recursiveArray = [goid]
  if terms.has_key(goid):
    parents = terms[goid]['p']
    if len(parents) > 0:
      for parent in parents:
        recursiveArray.extend(getAncestors(parent))

  return set(recursiveArray)


def getTerm(stream):
  block = []
  for line in stream:
    if line.strip() == "[Term]" or line.strip() == "[Typedef]":
      break
    else:
      if line.strip() != "":
        block.append(line.strip())

  return block



def parseTagValue(term):
  data = {}
  for line in term:
    tag = line.split(': ',1)[0]
    value = line.split(': ',1)[1]
    if not data.has_key(tag):
      data[tag] = []

    data[tag].append(value)

  return data



oboFile = open('./gene_ontology.WS250.obo','r')

#declare a blank dictionary
#keys are the goids
terms = {}

#skip the file header lines
getTerm(oboFile)

#infinite loop to go through the obo file.
#Breaks when the term returned is empty, indicating end of file
count = 0
while 1:

  #get the term using the two parsing functions
  term = parseTagValue(getTerm(oboFile))
  count = count +1
  print count
  if len(term) != 0:
    termID = term['id'][0]

    #only add to the structure if the term has a is_a tag
    #the is_a value contain GOID and term definition
    #we only want the GOID
    if term.has_key('is_a'):
      termParents = [p.split()[0] for p in term['is_a']]

      if not terms.has_key(termID):
        #each goid will have two arrays of parents and children
        terms[termID] = {'p':[],'c':[]}

      #append parents of the current term
      terms[termID]['p'] = termParents

      #for every parent term, add this current term as children
      for termParent in termParents:
        if not terms.has_key(termParent):
          terms[termParent] = {'p':[],'c':[]}
        terms[termParent]['c'].append(termID)
  else:
    break


import json


# ^ugly
outputfile = codecs.open('./GO_Children&Parents.txt', encoding='utf-8', mode='w')

outputfile.write(json.dumps(terms, indent=4))
# ^nice


#######################################################



import re


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
print len(Nodes_Seen)













