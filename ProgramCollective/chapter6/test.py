from ProgramCollective.chapter6 import docclass
cl=docclass.classifier(docclass.getwords)
cl.train('the quick brown fox jumps over the lazy dog','good')
cl.train('make quick money in the online casino','bad')
print(cl.fcount('quick','good'))
print(cl.fcount('quick','bad'))