import pickle

f = open("../mycode/file", "rb")
bug_list = pickle.load(f)

list=[]
for bug in bug_list:
    if bug.status == 'CLOSED' and bug.resolution != 'DUPLICATE' and bug.resolution != 'WORKSFORME' and bug.resolution != 'NOTABUG' and bug.resolution != 'INSUFFICIENT_DATA'and bug.resolution != 'WONTFIX'and bug.resolution != 'CANTFIX':
       try:
          list.append(bug.product)          # Put the products of bugs in a list. The variable could also be "bug.component", "bug.classification" etc.
       except: continue


# Calculate the number of bugs from different products
d = {}
for i in list:
    if list.count(i) >= 1:
        d[i] = list.count(i)
print(d)

f.close()

