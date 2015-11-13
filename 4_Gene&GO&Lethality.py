__author__ = 'nid16'


data = {}

outputfile = open('./Temp_Gene&GO_F.txt', mode='w')

for line in open('./gene_association.WS250.wb.c_elegans'):

    if("WB" in line):
        split_string = line.split("\t")
        genome = split_string [2]
        GO = split_string [4]
        dataMarker = split_string [6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","

lines_seen = []

singleLethality = open('./Single_Lethality_Genes.txt', mode='w')

#lines_seen.append(line)

#SPLIT LINES AND CHECK WHETHER THE GENE IS THE SAME FROM BOTH FILES

for line in open('./Gene_With_Lethal_Only_Finished.txt', mode='r'):
    print line
    split_lines = line.split(',')
    lines_seen.append(line[0])
    if split_lines[0] not in lines_seen:
        singleLethality.write(line)

for line in open('./Gene_With_Viable_Only_Finished.txt', mode='r'):
    split_lines = line.split(',')
    lines_seen.append(line[0])
    if split_lines[0] not in lines_seen:
        singleLethality.write(line)

for line in open('./Single_Lethality_Genes.txt', mode='r'):
    print line
    line = line.rstrip()
    split_line = line.split(",")
    try:
        gene = split_line[0]
        data[gene] = data.get(gene,"")+str(split_line[1])
    except IndexError:
        Null = "Null"

count = 0
for x in data:
    count = count +1
    print count
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")

outputfile.close()

#inputfile.close()

inputfile = open('./Temp_Gene&GO_F.txt', mode='r')
outputfile = open('./Gene&GO_F.txt', mode='w')
fOutputfile = open('./Filtered.txt', mode='w')

#viable = raw_input("viable")
#lethal = raw_input("lethal")
#GO = "GO"

for line in inputfile:
    if "GO" not in line:# or "lethal" not in line:
        fOutputfile.write(line)
    elif "viable" not in line and "lethal" not in line:
        fOutputfile.write(line)
    else:
        outputfile.write(line)
outputfile.close()
inputfile.close()
fOutputfile.close()


