# Variables used: priority, severity, and product.
# This programme serves section 7.1

import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn import preprocessing

f = open("file", "rb")
bug_list = pickle.load(f)


X2 = []
X3 = []
X4 = []
y = []

for idx, bug in enumerate(bug_list):
    if bug.status == 'CLOSED' and bug.resolution != 'DUPLICATE' and bug.resolution != 'WORKSFORME' and bug.resolution != 'NOTABUG' and bug.resolution != 'INSUFFICIENT_DATA' and bug.resolution != 'WONTFIX' and bug.resolution != 'CANTFIX':
        if   'comments' in dir(bug) and'cf_last_closed' in dir(bug) and 'creation_time' in dir(bug) and bug.classification and bug.priority and bug.severity:
            if bug.product =='Fedora' or bug.product =='Red Hat Enterprise Linux 6' or  bug.product =='Red Hat Enterprise Linux 5':
               X2.append(bug.priority)
               X3.append(bug.severity)
               X4.append(bug.product)
               tt1 = bug.cf_last_closed.timetuple()
               tt2 = bug.creation_time.timetuple()
               y.append((tt1.tm_year - tt2.tm_year) * 365 + (tt1.tm_mon - tt2.tm_mon) * 30 + tt1.tm_mday - tt2.tm_mday)


le = preprocessing.LabelEncoder()
le.fit(X2)
X2 = le.transform(X2)
X2 = np.array(X2).reshape(-1, 1)

le = preprocessing.LabelEncoder()
le.fit(X3)
X3 = le.transform(X3)
X3 = np.array(X3).reshape(-1, 1)

le = preprocessing.LabelEncoder()
le.fit(X4)
X4 = le.transform(X4)
X4 = np.array(X4).reshape(-1, 1)




print(X2.shape)
print(X3.shape)
print(X4.shape)

X = np.hstack([X2,X3,X4])
print(X.shape)
y = np.array(y)

X_train = X[0:int(len(X) * 0.9)]
X_test = X[int(len(X) * 0.9): len(X)]
y_train = y[0:int(len(y) * 0.9)]
y_test = y[int(len(y) * 0.9): len(y)]

regr_1 = DecisionTreeRegressor(max_depth=10)
regr_1.fit(X_train, y_train)

y_test_1 = regr_1.predict(X_test)


result=np.abs(y_test - y_test_1)
print(result)
n = len(result)
print(n)
print(np.mean(result))
print(np.median(result))
print(min(result))
print(max(result))

