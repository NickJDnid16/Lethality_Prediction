
import codecs

output = codecs.open('./GO_Terms_Used.txt.txt', encoding='utf-8', mode='w')



for line in  in codecs.open('./Lethality&Vector.txt', encoding='utf-8', mode='r'):
    line = line+1
    print(line)
    csv = BinLine.split(",")
    Gene = csv[0]
    Gene = '"'+Gene+'"'

    output.write(Gene)
    output.write(',')
    sl = 1
    sli = 0
    sliced = csv[1]

    for each in csv[1]:
        output.write(sliced[int(sli):int(sl)])
        if "1" not in csv[1]:
            print "Boooooo"
        sl =sl+1
        sli = sli+1
        output.write(',')

    output.write(csv[2])

output.close()


