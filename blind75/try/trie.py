class TrieNode:
    def __init__(this, val, word_end = False):
        this.val = val
        this.children = {}
        this.word_end = word_end
    def iswordend(this):
        return this.word_end
    def setwordend(this, we):
        assert type(we) == bool, "What type this {}".format(type(we))
        this.word_end = we
    def add_child(this, key, child):
        if key not in this.children:
            this.children[key] = child
            print("Success added child {}->{}".format(this.val,key))
            return True
        else:
            print("Child already exists {}->{}".format(this.val,key))
            return False
    def __repr__(this):
        return "{val} - nchildren: {nc} -- word end? {we}\n".format(val=this.val, nc=len(this.children),we= this.word_end)
class Trie:
    def __init__(this):
        this.root = TrieNode("root")
        print("Root node created")
    def insert(this, word):
        # root - a - n - y
        #        |       |
        #        |       -- w - h - e - r - e
        #        \-- r - t
        curr = this.root
        idx = 0
        aflag = False
        while not aflag:
            if word[idx] in curr.children:
                curr = curr.children[word[idx]]
                idx += 1
                if idx == len(word):
                    curr.setwordend(True)
                    aflag = True
            else:
                aflag = True
        while idx < len(word):
            if idx != len(word)-1:
                curr.add_child(word[idx], TrieNode(word[idx]))
            else:
                curr.add_child(word[idx], TrieNode(word[idx], word_end=True))
            curr = curr.children[word[idx]]
            idx += 1
    def search(this, word):
        curr = this.root
        for idx in range(len(word)):
            if word[idx] in curr.children:
                curr = curr.children[word[idx]]
            else:
                return False
        if curr.iswordend():
            return True
        return False
    def startsWith(this, prefix):
        curr = this.root
        for idx in range(len(prefix)):
            if prefix[idx] in curr.children:
                curr = curr.children[prefix[idx]]
            else:
                return False
        return True
    def __repr__(this):
        rep = ""
        Q = [this.root]
        while Q:
            top = Q.pop(0)
            rep += repr(top)
            for c in top.children:
                Q.append(top.children[c])
        return rep

a = Trie()
a.insert("fake")
a.insert("fluke")
a.insert("fast")
a.insert("art")
a.insert("fart")
a.insert("fart")
a.insert("anywhere")
a.insert("any")
print('startsWith("an")',a.startsWith("an"))
print('search("an")',a.search("an"))
print('search("any")',a.search("any"))
print('search("fart")',a.search("fart"))
print('search("fartsy")',a.search("fartsy"))
print('startsWith("ar")',a.startsWith("ar"))
print(a)
