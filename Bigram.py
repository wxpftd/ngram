#! /usr/bin/env python
# -*- coding=utf-8 -*-

import math

LocalCh='modelData/characterFile.txt'
LocalWords='modelData/wordsFile.txt'
Localcorpus='corpus/corpus.txt'

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
		    line = line.strip()
                for i in range(0, len(line)):
                    if not character.has_key(line[i]):
                        character[line[i]] = 1
                    else:
                        character[line[i]] += 1
                    if not words.has_key(line[i:i+2]):
                        words[line[i:i+2]] = 1
                    else:
                        words[line[i:i+2]] += 1 

	def modelOutput(self, characterPath=LocalCh, wordsPath=LocalWords):
	    characterFile = open(characterPath, 'w')
            wordsFile = open(wordsPath, 'w')
            for ch, count in character:
                characterFile.write(ch+':'+count)
            for word, count in words:
                wordsFile.write(word+':'+count)
            characterFile.close()
            wordsFile.close()
        

	def modelLoader(self, characterPath=LocalCh, wordsPath=LocalWords):
            characterFile = open(characterPath, 'r')
            wordsFile = open(wordsPath, 'r')
            for line in characterFile:
                parts = line.split(':')
                character[parts[0]] = parts[1]
                characterCount += parts[1]
            for line in wordsFile:
                parts = line.split(':')
                words[parts[0]] = parts[1]
                wordsCount += parts[1]
            characterFile.close()
            wordsFile.close()

        def getPieceCount(self, piece):
            if len(piece) == 1:
                return character.setdefault(piece, 0)
            elif len(piece) == 2:
                return words.setdefault(piece, 0)
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
if __name__ == __main__:
    print 'Model is training...\n'
    bm = Bigram()
    bm.trainModel()
    tm.modelOutput()
