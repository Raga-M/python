w="mon tues wednes thurs fri satur sun"
words=w.split()
words2=[]
for word in words:
     words2.append(word+"day")
o=" ".join (words2)
print(o)