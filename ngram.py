import codecs
corpus = codecs.open('./corpus.txt', 'r', 'gb2312')
line = corpus.readline()
target = open('./target.txt', 'w')
target.write(line[0])
