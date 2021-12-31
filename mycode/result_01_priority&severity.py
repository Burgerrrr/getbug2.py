# Variables used: priority and severity.
# This programme serves section 7.1

import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn import preprocessing

f = open("file", "rb")
bug_list = pickle.load(f)

# X1 and X2 correspond to two features, and more features can be expanded as needed. y is the target variable.
X1 = []
X2 = []
y = []

for idx, bug in enumerate(bug_list):
    if bug.status == 'CLOSED' and bug.resolution != 'DUPLICATE' and bug.resolution != 'WORKSFORME' and bug.resolution != 'NOTABUG' and bug.resolution != 'INSUFFICIENT_DATA' and bug.resolution != 'WONTFIX' and bug.resolution != 'CANTFIX':
        if   'comments' in dir(bug) and'cf_last_closed' in dir(bug) and 'creation_time' in dir(bug) and bug.classification and bug.priority and bug.severity:
               X1.append(bug.priority)
               X2.append(bug.severity)
               tt1 = bug.cf_last_closed.timetuple()
               tt2 = bug.creation_time.timetuple()
               y.append((tt1.tm_year - tt2.tm_year) * 365 + (tt1.tm_mon - tt2.tm_mon) * 30 + tt1.tm_mday - tt2.tm_mday)

# Convert X1 from a discrete value to an integer value.
le = preprocessing.LabelEncoder()
le.fit(X1)
X1 = le.transform(X1)
# Convert a row into a column.
X1 = np.array(X1).reshape(-1, 1)

le = preprocessing.LabelEncoder()
le.fit(X2)
X2 = le.transform(X2)
X2 = np.array(X2).reshape(-1, 1)

print(X1.shape)
print(X2.shape)
X = np.hstack([X1,X2])
print(X.shape)
y = np.array(y)

# Use 90% of data to train, and use 10% of data to test
X_train = X[0:int(len(X) * 0.9)]
X_test = X[int(len(X) * 0.9): len(X)]
y_train = y[0:int(len(y) * 0.9)]
y_test = y[int(len(y) * 0.9): len(y)]


# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=10)
regr_1.fit(X_train, y_train)

# Predict
y_test_1 = regr_1.predict(X_test)


# Output results
result=np.abs(y_test - y_test_1)
print(result)
n = len(result)
print(n)             # Output the number of predicted results.
print(np.mean(result))
print(np.median(result))
print(min(result))
print(max(result))



