class TimeMap:

    def __repr__(this):
        return repr(this.internal_dict)

    def __init__(self):
        self.internal_dict = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.internal_dict.get(key,"")
        if val == "":
            self.internal_dict.update({key:{timestamp:value}})
        else:
            self.internal_dict[key].update({timestamp:value})
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.internal_dict.get(key,"")
        if val == "":
            return val
        val_t = val.get(timestamp,"")
        if val_t != "":
            return val_t
        closest = None
        min_diff = float('inf')
        for k, v in sorted(val.items()):
            if k < timestamp:
                diff = timestamp - k
                if diff < min_diff:
                    min_diff = diff
                    closest = v
            else:
                break
        if closest is not None:
            return closest
        else:
            return ""

def instruction_reader(instructions, args):
    tobj = None
    for idx,(i, a) in enumerate(zip(instructions, args)):
        print("Instruction #{} ".format(idx),end='')
        if i == "TimeMap":
            tobj = TimeMap()
            print(tobj)
        elif i == "set":
            tobj.set(*a)
            print("{}".format(tobj))
        elif i == "get":
            print("{} = {}".format('get('+','.join(str(k) for k in a)+')',tobj.get(*a)))

# ins = ["TimeMap","set","get","get","set","get","get"]
# arg = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]

ins = ["TimeMap","set","set","get","get","get","get","get"]
arg = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]


instruction_reader(ins, arg)
