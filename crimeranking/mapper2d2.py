import dstk
dstk = dstk.DSTK()

coord=[]
typecrime=[]
location=[]
path = [
    "2016-08-gloucestershire-street"
    ]
for i in range(0,len(path)):
    f = open(path[i]+".csv", "r")
    for line in f:
        entry = line.rsplit(',')
        if entry[4]=='' or entry[4]=="Longitude" or entry[4]=="longitude":
            continue
        else:
            coord.append([float(entry[5]),float(entry[4])])
            typecrime.append(entry[9])
            location.append(entry[6])
    f.close()
#extract coordinates
###

f = open("output2d2.txt","w")
for i in range(0,len(coord)):
    f.write(typecrime[i]+": ")
    address = dstk.coordinates2politics(coord[i])
    level = address[0]['politics']
    if level==None:
        f.write("\n")
        continue
    else:
        for j in range(0,len(level)):
            f.write(level[j]['name'])
            if j!=len(level)-1:
                f.write(", ")
            else:
                f.write(", "+location[i])
    f.write("\n")
f.close()
