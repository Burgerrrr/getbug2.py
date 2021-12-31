#!/usr/bin/env python
#
# This work is licensed under the GNU GPLv2 or later.
# See the COPYING file in the top-level directory.

# getbug.py: Simple demonstration of connecting to bugzilla, fetching
#            a bug, and printing some details.

import bugzilla
import pickle
# public test instance of bugzilla.redhat.com. It's okay to make changes
URL = "bugzilla.stage.redhat.com"

bzapi = bugzilla.Bugzilla(URL)

# getbug() is just a simple wrapper around getbugs(), which takes a list
# IDs, if you need to fetch multiple
#
# Example bug: https://bugzilla.stage.redhat.com/show_bug.cgi?id=427301
bug_list = []
f = open("../mycode/file", "wb")
for id in range(1000,1010):
    try:
        print(id)
        bug = bzapi.getbug(id)
        bug_list.append(bug)
    except:
        print("Exception occurred. Try next id.")
pickle.dump(bug_list, f)
f.close()

f = open("../mycode/file", "rb")
bug_list = pickle.load(f)
print(len(bug_list))

bug = bzapi.getbug(9930)
print("'Id'        :%s," % bug.id)
print("'Product'   :'%s'," % bug.product)
print("'Component' :'%s'," % bug.component)
print("'Status'    :'%s'," % bug.status)
print("'Resolution':'%s'," % bug.resolution)
print("'Summary'   :'%s'," % bug.summary)

print("'Priority'  :'%s'," % bug.priority)
print("'Severity'  :'%s'," % bug.severity)
print("'Version'   :'%s'," % bug.version)
print("'Alias'     :'%s'," % bug.alias)
print("'Assigned_to':'%s'," % bug.assigned_to)
print("'Is_confirmed':'%s'," % bug.is_confirmed)
print("'Creation_time':'%s'," % bug.creation_time)
print("'Last_change_time' :'%s'," % bug.last_change_time)
print("'Platform'  :'%s'," % bug.platform)
print("'Classification':'%s'," % bug.classification)
print("'Op_sys'    :'%s'," % bug.op_sys)
print("'Whiteboard':'%s'," % bug.whiteboard)
print("'Cf_last_closed':'%s'," % bug.cf_last_closed)

# Just check dir(bug) for other attributes, or check upstream bugzilla
# Bug.get docs for field names:
# https://bugzilla.readthedocs.io/en/latest/api/core/v1/bug.html#get-bug

# comments must be fetched separately on stock bugzilla. this just returns
# a raw dict with all the info.
comments = bug.getcomments()
print("'Number_of_comments':%s," % comments[-1]["count"])
print("'Creation_time_of_comment':'%s'," % comments[-1]["creation_time"])
print("'Creator'   :'%s'," % comments[-1]["creator"])
print("'Creator_id':'%s'," % comments[-1]["creator_id"])
print("'id'        :'%s'," % comments[-1]["id"])
print("'Is_private':'%s'," % comments[-1]["is_private"])
print("'Tags'      :'%s'," % comments[-1]["tags"])
print("'Text'      :'%s'," % comments[-1]["text"])
print("'Time'      :'%s'," % comments[-1]["time"])

tt1 = bug.cf_last_closed.timetuple()
tt2 = bug.creation_time.timetuple()
print("'Duration'  :%s" % ((tt1.tm_year-tt2.tm_year)*365+(tt1.tm_mon-tt2.tm_mon)*30+tt1.tm_mday-tt2.tm_mday))






# getcomments is just a wrapper around bzapi.get_comments(), which can be
# used for bulk comments fetching
