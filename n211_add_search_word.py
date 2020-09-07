
"""
Add and Search Word - Data structure design
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = {}
        self.ds['.'] = []
        self.maxLength = float("-inf")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        if len(word) > self.maxLength:
            self.maxLength = len(word)
        
        if len(self.ds['.']) < self.maxLength:
            
        wordList = list(word)
        
        for i in range(len(wordList)):
            
            if wordList[i] in self.ds:
                self.ds[wordList[i]].append(i)
            else:
                self.ds[wordList[i]] = []
                self.ds[wordList[i]].append(i)
                
        
        print(self.ds)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        wordList = list(word)
        
        for i in range(len(wordList)):

            if i not in self.ds[wordList[i]]:
                return False
            
            
                

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
# param_2 = obj.search("bad")