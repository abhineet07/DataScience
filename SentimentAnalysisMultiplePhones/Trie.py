class MatchNode:
    def __init__(self):
        self.trieNode = None
        self.polarity = 'Neutral'
        self.match = False
        self.matchLen = -1
        self.matchString = ""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.polarity = 'Neutral'
        self.matchLen = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, polarity):
        current = self.root
        for i in range(len(word)):
            ch = word[i]
            if not current.children.__contains__(ch):
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.endOfWord = True
        current.polarity = polarity

    def search(self, word):
        current = self.root
        for i in range(len(word)):
            ch = word[i]
            if not current.children.__contains__(ch):
                return None
            current = current.children[ch]
        return current.endOfWord

    # predecessor suffixSearch
    def suffixSearch3(self, word, root):
        current = self.root
        matchNode = MatchNode()
        matchNode.polarity = current.polarity
        match_len = 0
        match_str = ""
        biggestMatch = ""
        # id = 0
        for i in range(len(word)):
            ch = word[i]
            match_str = match_str + ch
            # print("Match str : ", match_str, "\tBiggest Match : ", biggestMatch)
            if not current.children.__contains__(ch):
                # print("Not contain in current children")
                return matchNode
            elif current.children[ch].endOfWord:
                # print("CONTAINS in current children")
                if len(match_str) > len(biggestMatch):
                    biggestMatch = match_str
                    # print("Biggest Match : ", biggestMatch, "\ti+1 : ", (i+1), "\tlen(word) : ", len(word), "\tlen(biggestMatch) :", len(biggestMatch))
                    # if the next char to current char is not space then that word is not a match
                    # eg: 'no' in 'now'
                    if len(biggestMatch) == len(word):
                        matchNode.match = True
                    elif i+1 < len(word):
                        if word[i+1]!=" ":
                            matchNode.match = False
                        else:
                            matchNode.match = True
                    # print("Matchnode.match : ", matchNode.match)
                    matchNode.trieNode = current.children[ch]
                    matchNode.polarity = current.children[ch].polarity
                    matchNode.matchLen = match_len
                    matchNode.matchString = biggestMatch

            current = current.children[ch]
            match_len += 1
            #id = i
            # print(matchNode.match)

        if current.endOfWord:
            if i + 1 < len(word):
                if word[i + 1] != " ":
                    matchNode.match = False
                else:
                    matchNode.match = True
            matchNode.trieNode = current
            matchNode.polarity = current.polarity
            matchNode.matchLen = match_len
            matchNode.matchString = biggestMatch
            # print("Space condition : ", matchNode.match)
            return matchNode

        return matchNode


    def suffixSearch2(self, word):
        current = self.root
        for i in range(len(word)):
            ch = word[i]
            if not current.children.__contains__(ch):
                return None
            elif current.children[ch].endOfWord:
                return current.children[ch]
            current = current.children[ch]
        if current.children[ch].endOfWord:
            return current.children[ch]
        else:
            return None

    def suffixSearch(self, word):
        current = self.root
        self.matchNode = MatchNode()
        self.matchNode.polarity = current.polarity
        match_len = 1
        match_str = ""
        for i in range(len(word)):
            ch = word[i]
            match_str = match_str + ch
            if not current.children.__contains__(ch):
                return None
            elif current.children[ch].endOfWord:
                self.matchNode.trieNode = current.children[ch]
                self.matchNode.matchLen = match_len
                self.matchNode.matchString = match_str
                return self.matchNode
            current = current.children[ch]
            match_len += 1

        if current.children[ch].endOfWord:
            self.matchNode.trieNode = current.children[ch]
            self.matchNode.matchLen = match_len
            self.matchNode.matchString = match_str
            return self.matchNode
        else:
            return None

def main():
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their", "not", "good", "not good"]

    t = Trie()
    for key in keys:
        t.insert(key, "positive")

    print(t.search("the"))
    print(t.search("ther"))
    print(t.search("no"))
    print(t.suffixSearch2("ther").endOfWord)

    match = t.suffixSearch3("not good", t.root)
    if match != None:
        print(match.trieNode.endOfWord)
        print(match.polarity)
        print("MatchString : ", match.matchString)
        print(match.matchLen)
    else:
        print("word not present")

    print(t.search("notgood"))


if __name__ == '__main__':
    main()
