file = open("pokemonlist.txt","r")
readfile = file.read()
filelist = readfile.split()
filedict = {}

for i in filelist:
    if i[0] not in filedict:
        filedict[i[0]] = [i]
    else:
        filedict[i[0]].append(i)

def pokemonlist(x):
    global longest

    longest = []
    if len(x) > len(longest):
        longest = x

    if x[-1][-1] in filedict:
        for name in filedict[x[-1][-1]]:
            if name not in x:
                x.append(name)
                pokemonlist(x) 

for x in filelist:
    pokemonlist([x])

print(longest)