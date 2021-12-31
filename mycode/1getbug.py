
# Run this at first, this programme will get bugs and put them in a file named "file". Then this file could be used in the following programmes.

import bugzilla
import pickle
import threading

URL = "bugzilla.stage.redhat.com"
start_id = 695000
end_id = 710000

def getbug_thread(i, URL, bug_list_thread):
    bzapi = bugzilla.Bugzilla(URL)
    for id in range(start_id + i, end_id, 10):
        try:
            print(id)
            bug = bzapi.getbug(id)
            bug_list_thread.append(bug)
        except:
            print("Exception occurred. Try next id for thread %d." % i)

ts = []
bug_lists = [[], [], [], [], [], [], [], [], [], []]
for i in range(0, 10):
    try:
        th = threading.Thread(target=getbug_thread, args=(i, URL, bug_lists[i]))
        ts.append(th)
    except:
        print("unable to create thread %d" % i)

for i in range(0, 10):
    try:
        ts[i].start()
    except:
        print("unable to start thread %d" % i)

for i in range(0, 10):
    try:
        ts[i].join()
    except:
        print("unable to join thread %d" % i)

bug_list = []
for l in bug_lists:
    bug_list.extend(l)

f = open("file", "wb")
pickle.dump(bug_list, f)
f.close()

f = open("file", "rb")
bug_list = pickle.load(f)
print(len(bug_list))
