#! /usr/share/env python
# -*- coding=utf-8 -*-

resultFile = open('corpus/BigCorpusPre.txt', 'w')
with open('corpus/BigCorpus.txt', 'r') as f:
    for line in f:
        line = line[line.find(':')+1:]
        resultFile.write(line.strip()+'\n')
resultFile.close()

