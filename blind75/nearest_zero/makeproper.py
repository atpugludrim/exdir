import sys
with open(sys.argv[1],'r') as f:
    lines = f.readlines()

with open(sys.argv[2],'w') as f:
    f.write(F'{len(lines)} ')
    for i, l in enumerate(lines):
        tokens = l.strip().split(',')
        if i == 0:
            f.write(F'{len(tokens)}\n')
        stripped = (t.strip('[] ') for t in tokens)
        f.write(' '.join(stripped)+'\n')
