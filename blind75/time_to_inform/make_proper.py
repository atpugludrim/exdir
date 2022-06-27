import sys
def stripper(token):
    return str(token).strip().strip('[]').strip()
with open(sys.argv[1],"r") as f:
    lines = f.readlines()

with open(sys.argv[2],"w") as f:
    lins = []
    lins.append(' '.join(stripper(token) for token in lines[2].split(','))+'\n')
    lins.append(' '.join(stripper(token) for token in lines[3].split(',')))
    f.writelines(lins)
