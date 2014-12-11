import sys

with open("train.crfsuite.txt") as f:
    content = f.readlines()

dic = {}

for line in content: 
    list = line.split()
    features = list[1:-1]
    #print " ".join(features)
    for feature in features:
        if feature in dic:
            dic[feature] = dic[feature] + 1
	else:
            dic[feature] = 1

#print len(dic.keys())

keys = dic.keys()
#print keys
#for line in content:
#    stream = ""
#    features = line.split()[1:-1]
#    for key in keys:
#        if key in features:
#            stream = stream + "1"
#        else:
#            stream = stream + "0"
#    print stream


with open("test.crfsuite.txt") as g:
    content_test = g.readlines()
    
for line in content_test:
    stream = ""
    features = line.split()[1:-1]
    for key in keys:
        if key in features:
            stream = stream + "1"
        else:
            stream = stream + "0"
    print stream
      #sys.stderr.write(stream+'\n')

