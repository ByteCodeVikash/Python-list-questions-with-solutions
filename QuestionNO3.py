#Python – Swap elements in String list

def swapString(string,pos1,pos2):

    string[pos1],string[pos2]=string[pos2],string[pos1]

    return string

string=["a","b","c","d"]

pos1,pos2=1,3

print(swapString(string,pos1,pos2))