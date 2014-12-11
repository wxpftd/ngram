#! /usr/bin/env python
# -*- coding=utf-8 -*-

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
                    if not words.has_key(line[i:i+1]):
                        words[line[i:i+1]] = 1
                    else:
                        words[line[i:i+1]] += 1 

	def modelOutput(self, characterPath=LocalCh, wordsPath=LocalWords):
	    characterFile = open(characterPath, 'w')
            for ch, count in character:
                characterFile.write(ch+':'+count)
            characterFile.close()
            wordsFile = open(wordsPath, 'w')
            for word, count in words:
                wordsFile.write(word+':'+count)
            wordsFile.close()
        

	def ModelLoader(self, characterPath=LocalCh, wordsPath=LocalWords):
            characterFile = open(characterPath, 'r')
            wordsFile = open(wordsPath, 'r')
            for line in characterFile:
                parts = line.split(':')
                character[parts[0]] = parts[1]
            for line in wordsFile:
                parts = line.split(':')
                words[parts[0]] = parts[1]
            characterFile.close()
            wordsFile.close()

        def getPiecePro(self, piece):
	   pass


	def calculate(self, sentence):
	   pass
	
	def TestSetProcess(self):
	   pass

