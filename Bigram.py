#! /usr/bin/env python
# -*- coding=utf-8 -*-

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

    def trainModel(self, corpusPath='corpus/corpus.txt'):
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

	def modelOutput(self, characterFilePath='modelData/characterFile.txt', wordsFilePath='modelData/wordsFile.txt'):
        with characterFile = open(characterFilePath, 'w')
        for ch, count in character:
            characterFile.write(ch+':'+count)
        wordsFile = open(wordsFilePath, 'w')
        for word, count in words:
            wordsFile.write(word+':'+count)
        

	def ModelLoader(self, characterFilePath='modelData/characterFile.txt', wordsFilePath='modelData/wordsFile.txt'):
        characterFile = open(characterFilePath, 'r')
        wordsFile = open(wordsFilePath, 'r')
        for line in characterFile:
            parts = line.split(':')
            character[parts[0]] = parts[1]
        for line in wordsFile:
            parts = line.split(':')
            words[parts[0]] = parts[1]

    def getPiecePro(self, piece):
        if character[piece]:


	def calculate(self, sentence):
		pass
	
	def TestSetProcess(self):
		pass

