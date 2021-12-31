# This programme can calculate mean, median, min, and max bug lifetimes. These bugs could have any different features
import pickle
import numpy as np
f = open("../mycode/file", "rb")
bug_list = pickle.load(f)
list=[]
for bug in bug_list:
    if bug.status == 'CLOSED' and bug.resolution != 'DUPLICATE' and bug.resolution != 'WORKSFORME' and bug.resolution != 'NOTABUG' and bug.resolution != 'INSUFFICIENT_DATA'and bug.resolution != 'WONTFIX'and bug.resolution != 'CANTFIX':
       #if len(bug.comments)>18:
       #if bug.priority=='urgent':
       #if bug.severity=='unspecified':
           try:
            tt1=bug.cf_last_closed.timetuple()     # The last time the bug was turned to "CLOSED"
            tt2=bug.creation_time.timetuple()      # The creation time of the bug
            list.append((tt1.tm_year-tt2.tm_year)*365+(tt1.tm_mon-tt2.tm_mon)*30+tt1.tm_mday-tt2.tm_mday)     # Calculate the number of days between them, and put them in one list
           except:
             continue

print(np.mean(list))
print(np.median(list))
print(min(list))
print(max(list))





