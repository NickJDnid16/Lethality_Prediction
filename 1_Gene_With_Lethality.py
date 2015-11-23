'''
Created on 23 Oct 2015

@author: nid16
'''
import sys
import codecs
inputfile = open('./phenotype_association.WS250.wb', mode='r')
outputfile = open('./Genes.txt', mode='w')


Lethality = ("WBPhenotype:0000050", "WBPhenotype:0000060", "WBPhenotype:0000054", "WBPhenotype:0000057", "WBPhenotype:0000117", "WBPhenotype:0000118", "WBPhenotype:0000058", \
             "WBPhenotype:0000419", "WBPhenotype:0001003", "WBPhenotype:0000116", "WBPhenotype:0000411", "WBPhenotype:0000052", "WBPhenotype:0000053", "WBPhenotype:0000351", \
             "WBPhenotype:0001018", "WBPhenotype:0001078", "WBPhenotype:0000772", "WBPhenotype:0001130", "WBPhenotype:0001129", "WBPhenotype:0000152", "WBPhenotype:0000160", \
             "WBPhenotype:0001132", "WBPhenotype:0001131", "WBPhenotype:0001885", "WBPhenotype:0001886", "WBPhenotype:0002007", "WBPhenotype:0001642", "WBPhenotype:0002004", \
             "WBPhenotype:0001020", "WBPhenotype:0001536", "WBPhenotype:0000040", "WBPhenotype:0000044", "WBPhenotype:0000748", "WBPhenotype:0000759", "WBPhenotype:0001343", \
             "WBPhenotype:0001959", "WBPhenotype:0001960", "WBPhenotype:0002068", "WBPhenotype:0000628", "WBPhenotype:0001867", "WBPhenotype:0001107", "WBPhenotype:0001108", \
             "WBPhenotype:0001109", "WBPhenotype:0001103", "WBPhenotype:0001104", "WBPhenotype:0000765", "WBPhenotype:0000761", "WBPhenotype:0000760", "WBPhenotype:0001106", \
             "WBPhenotype:0000762", "WBPhenotype:0001105", "WBPhenotype:0000767", "WBPhenotype:0000769", "WBPhenotype:0001081", "WBPhenotype:0001082", "WBPhenotype:0001083", \
             "WBPhenotype:0000768", "WBPhenotype:0001079", "WBPhenotype:0001080", "WBPhenotype:0000771", "WBPhenotype:0001007", "WBPhenotype:0001011", "WBPhenotype:0000270", \
             "WBPhenotype:0001034", "WBPhenotype:0001138", "WBPhenotype:0001027", "WBPhenotype:0001141", "WBPhenotype:0001035", "WBPhenotype:0001026", "WBPhenotype:0001142", \
             "WBPhenotype:0001143", "WBPhenotype:0001139", "WBPhenotype:0001580", "WBPhenotype:0001832", "WBPhenotype:0001895", "WBPhenotype:0001151", "WBPhenotype:0001030", \
             "WBPhenotype:0001152", "WBPhenotype:0001031", "WBPhenotype:0001153", "WBPhenotype:0001154", "WBPhenotype:0001155", "WBPhenotype:0001353", "WBPhenotype:0001157", \
             "WBPhenotype:0001158", "WBPhenotype:0001159", "WBPhenotype:0001156", "WBPhenotype:0001161", "WBPhenotype:0001162", "WBPhenotype:0001164", "WBPhenotype:0001166", \
             "WBPhenotype:0001165", "WBPhenotype:0001163", "WBPhenotype:0001041", "WBPhenotype:0001043", "WBPhenotype:0000776", "WBPhenotype:0001216", "WBPhenotype:0001044", \
             "WBPhenotype:0001077", "WBPhenotype:0001078", "WBPhenotype:0000772", "WBPhenotype:0001130", "WBPhenotype:0001129", "WBPhenotype:0000152", "WBPhenotype:0000160", \
             "WBPhenotype:0001132", "WBPhenotype:0001131", "WBPhenotype:0001885", "WBPhenotype:0001886", "WBPhenotype:0002007", "WBPhenotype:0001118", "WBPhenotype:0001127", \
             "WBPhenotype:0001128", "WBPhenotype:0001110", "WBPhenotype:0001867", "WBPhenotype:0001111", "WBPhenotype:0001112", "WBPhenotype:0001113", "WBPhenotype:0001114", \
             "WBPhenotype:0001115", "WBPhenotype:0001116", "WBPhenotype:0001119", "WBPhenotype:0001120", "WBPhenotype:0001122", "WBPhenotype:0001121", "WBPhenotype:0001124", \
             "WBPhenotype:0001123", "WBPhenotype:0001125", "WBPhenotype:0001187", "WBPhenotype:0001117", "WBPhenotype:0001126", "WBPhenotype:0001133", "WBPhenotype:0001134", \
             "WBPhenotype:0001135", "WBPhenotype:0001176", "WBPhenotype:0001137", "WBPhenotype:0001147", "WBPhenotype:0000777", "WBPhenotype:0001148", "WBPhenotype:0001150", \
             "WBPhenotype:0001144", "WBPhenotype:0001145", "WBPhenotype:0001146", "WBPhenotype:0001167", "WBPhenotype:0001169", "WBPhenotype:0001168", "WBPhenotype:0001178", \
             "WBPhenotype:0001177", "WBPhenotype:0000365", "WBPhenotype:0001185", "WBPhenotype:0001186", "WBPhenotype:0000062")

geneseen = []
genes = []
data = {}
for line in inputfile:

    if "WB" not in line:
        Null = "Null"
    elif "WB" in line:

        split_string = line.split("\t")
        gene = split_string[2]
        negation = split_string[3]
        phenotype = split_string[4]

        data[gene] = data.get(gene,"")+negation+","+phenotype+","

for x in data:
    outputfile.write(x+","+data[x]+"\n")


outputfile.close()
inputfile.close()


inputfile = open('./Genes.txt', mode='r')
vOutputfile = open('./Gene_With_Viable_Only.txt', mode='w')
lOutputfile = open('./Gene_With_Lethal_Only.txt', mode='w')
oOutputfile = open('./Gene_With_Both_L&V.txt', mode='w')

NOT = "NOT"
WB = "WB"

for line in inputfile:
    split_string = line.split(",")
    print split_string[0]
    if NOT in line:
        if any(l in line for l in Lethality):

            oOutputfile.write(line)
        else:
            vOutputfile.write(line)
    elif NOT not in line:
        lOutputfile.write(line)
#sys.exit("Stopped")

vOutputfile.close()
lOutputfile.close()
oOutputfile.close()
inputfile.close()

#########################################################################################

inputfile = open('./Gene_With_Both_L&V.txt', mode='r')
vinputfile = open('./Gene_With_Lethal_Only.txt', mode='r')
linputfile = open('./Gene_With_Viable_Only.txt', mode='r')

lethal = []
viable = []

#sys.exit("Stopped")
out = open('./Stuff.txt', mode='w')
for line in inputfile:
    N = line.count("NOT")
    Leth = 0
    Phenotype = line.count("WB")
    split_string = line.split(",")
    for element in split_string:
        if element in Lethality:
            Leth = Leth+1
    print N
    print Leth
    if N == Leth: 
        with open('./Gene_With_Viable_Only.txt', 'a') as file:
            file.write(line)
        print "Turned Into Viable"

    elif N < Leth:
        with open('./Gene_With_Lethal_Only.txt', 'a') as file:
            file.write(line)
        print "Turned Into Lethal"
    elif N == Phenotype and N != Leth:
        with open('./Gene_With_Viable_Only.txt', 'a') as file:
            file.write(line)
        print "Turned Into Viable"
    elif Leth > 1 and N == 0:
        with open('./Gene_With_Lethal_Only.txt', 'a') as file:
            file.write(line)
        print "Turned Into Lethal"
    elif N > Leth:
        with open('./Gene_With_Viable_Only.txt', 'a') as file:
            file.write(line)
        print "Turned Into Viable"
    else:
        out.write(line)

inputfile.close()

voutputfile = open('./Gene_With_Viable_Only_Finished.txt', mode='w')
loutputfile = open('./Gene_With_Lethal_Only_Finished.txt', mode='w')


for line in vinputfile:
    line_split = line.split(",")
    gene = line_split[0]
    voutputfile.write(gene+","+"viable"+"\n")
for line in linputfile:
    line_split = line.split(",")
    gene = line_split[0]
    loutputfile.write(gene+","+"lethal"+"\n")


vinputfile.close()
linputfile.close()
voutputfile.close()
loutputfile.close()


vinputfile = open('./Gene_With_Viable_Only_Finished.txt', mode='r')
linputfile = open('./Gene_With_Lethal_Only_Finished.txt', mode='r')
goutputfile = open('./Single_Lethality_Genes.txt', mode='w')

for line in vinputfile:
    goutputfile.write(line)
for line in linputfile:
    goutputfile.write(line)

vinputfile.close()
linputfile.close()
goutputfile.close()



