from lru import LRUCache

import os
import sys
assert len(sys.argv) > 2, f"usage: python3 {sys.argv[0]} <testcase_file> <expected_output_file>"
testcase_file = sys.argv[1]
assert os.path.isfile(testcase_file)
outputs_file = sys.argv[2]
assert os.path.isfile(outputs_file)

import logging
logger = logging.getLogger('info')
logger.setLevel(logging.INFO)
ch = logging.FileHandler('codout.txt')
ch.setLevel(logging.INFO)
f = logging.Formatter("%(message)s")
ch.setFormatter(f)
logger.addHandler(ch)

dlogger = logging.getLogger('debug')
dlogger.setLevel(logging.DEBUG)
dch = logging.StreamHandler(sys.stdout)
dch.flush = sys.stdout.flush
dch.setLevel(logging.DEBUG)
df = logging.Formatter("%(levelname)s - %(message)s")
dch.setFormatter(df)
dlogger.addHandler(dch)

def driver(instructions, args, expected_outputs):
    lc = None
    outputs = []
    for idx, (i,a) in enumerate(zip(instructions,args)):
        if i == "LRUCache":
            lc = LRUCache(*a)
            logger.info('null')
            outputs.append('null')
        elif i == "put":
            lc.put(*a)
            logger.info('null')
            outputs.append('null')
            if outputs[-1] != expected_outputs[idx]:
                dlogger.debug(f"problem at put: {outputs[-1] = } {expected_outputs[idx] = }")
                import pdb;pdb.set_trace()
                dlogger.debug(f"problem at put: {outputs[-1] = } {expected_outputs[idx] = }")
        elif i == "get":
            ret = lc.get(*a)
            logger.info(str(ret))
            outputs.append(str(ret))
            if outputs[-1] != expected_outputs[idx]:
                dlogger.debug(f"problem at get: {outputs[-1] = } {expected_outputs[idx] = }")
                import pdb;pdb.set_trace()
                dlogger.debug(f"problem at get: {outputs[-1] = } {expected_outputs[idx] = }")
        dlogger.debug(f"{i = }, {a = }, {outputs[-1] = }")
        dlogger.debug(f"{lc = }")
    return outputs

def main():
    global testcase_file
    with open(outputs_file,'r') as handle:
        expected_outputs_ = handle.readlines() # must be one line of outputs
    expected_outputs = [eo.strip('[]') for eo in expected_outputs_[0].strip().split(',')]
    with open(testcase_file,'r') as handle:
        lines = handle.readlines() # must contain two lines, one being instructions, other being args
    assert len(lines) == 2
    instructions_ = lines[0]
    args_ = lines[1]
    instructions = [i.strip('"') for i in instructions_.strip("[]\w\n ").split(',')]
    args = [[int(j) for j in k.split(',')] for k in [a.strip('[]') for a in args_.strip().split(',[')]]
    outputs = driver(instructions, args, expected_outputs)

if __name__=="__main__":
    main()
