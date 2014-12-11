#! /usr/bin/env python
# -*- coding=utf-8 -*-

import math

LocalCh='modelData/characterFile.txt'
LocalWords='modelData/wordsFile.txt'
Localcorpus='corpus/BigCorpusPre.txt'

class Bigram:
	'''
	Bigram语言模型
	'''

	#字频表
	character={}
	#词频表
	words={}

        #字计数器
        characterCount = 0
        #词计数器
        wordsCount = 0

        #平滑
        lam = 1

	#测试集
	judgeResult=file

	def __init__(self):
	    pass

        def trainModel(self, corpusPath=Localcorpus):
	    with open(corpusPath) as f:
		for line in f:
                    line = line.decode('utf-8')
		    line = line.strip()
                    for i in range(0, len(line)):
                        if not self.character.has_key(line[i]):
                            self.character[line[i]] = 1
                        else:
                            self.character[line[i]] += 1
                        if not self.words.has_key(line[i:i+2]):
                            self.words[line[i:i+2]] = 1
                        else:
                            self.words[line[i:i+2]] += 1 

	def modelOutput(self, characterPath=LocalCh, wordsPath=LocalWords):
	    characterFile = open(characterPath, 'w')
            wordsFile = open(wordsPath, 'w')
            for (ch, count) in self.character.items():
                characterFile.write(ch.encode('utf-8')+':'+repr(count)+'\n')
            for (word, count) in self.words.items():
                wordsFile.write(word.encode('utf-8')+':'+repr(count)+'\n')
            characterFile.close()
            wordsFile.close()
        

	def modelLoader(self, characterPath=LocalCh, wordsPath=LocalWords):
            characterFile = open(characterPath, 'r')
            wordsFile = open(wordsPath, 'r')
            for line in characterFile:
                if len(line.strip()) == 0:
                    continue
                parts = line.split(':')
                if len(parts[0]) == 0 or len(parts[1]) == 0:
                    continue
                self.character[parts[0]] = parts[1]
                self.characterCount += int(parts[1])
            for line in wordsFile:
                if len(line.strip()) == 0:
                    continue
                parts = line.split(':')
                if len(parts[0]) == 0 or len(parts[1]) == 0:
                    continue
                self.words[parts[0]] = parts[1]
                self.wordsCount += int(parts[1])
            characterFile.close()
            wordsFile.close()

        def getPieceCount(self, piece):
            if len(piece) == 1:
                return self.character.setdefault(piece, 0)
            elif len(piece) == 2:
                return self.words.setdefault(piece, 0)
            else:
                print 'Word piece is wrong size.\n'

        def getPiecePro(self, frontPiece, word):
            frontPro = getPiecePro(frontPiece) / characterCount
            wordPro = getPiecePro(word) / wordsCount
            return (wordPro + self.lam) / (frontPro + self.lam)


	def getSentencePro(self, sentence):
            if len(sentence.strip()) == 0:
                return 0
            retPro = math.log(getPiecePro(sentence[0]+lam)/(characterCount+lam))
            for i in range(1, len(sentence)):
                retPro += math.log(getPiecePro(sentence[i], sentence[i-1:i+1])) 
            return retPro
	
	def testSetProcess(self):
            pass
if __name__ == '__main__':
    #print 'Model is training...\n'
    bm = Bigram()
    #bm.trainModel()
    #bm.modelOutput()
    print 'Start Judging...\n'
    bm.modelLoader();
