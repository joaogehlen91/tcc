# Load libraries

import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.utils import shuffle
from sklearn.svm import OneClassSVM

out = open('resultados_classifier.csv', 'w')


# data = 'author_and_outlier.csv'
data = 'cenario4/supervised/positivos_negativos_FAVE.csv'
dataset = pandas.read_csv(data, header=None)

models = []
f = 0

X = dataset.values[:, f:24]
Y = dataset.values[:, 24]

print(len(X[0]))

acum_acc_g = 0
acum_r_g = 0
acum_p_g = 0

acum_acc_knn = 0
acum_r_knn = 0
acum_p_knn = 0

if f == 0:
    out.write('FAVE\n')
if f == 12:
    out.write('MAVE\n')

for i in range(10):
    l = []
    # l.append(str(i))
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.9)
    print(len(X_train))

    g = GaussianNB()
    # k = KMeans(n_clusters=1)
    knn = KNeighborsClassifier()
    # svm = OneClassSVM()

    g.fit(X_train, y_train)
    # k.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    # svm.fit(X)

    prediction_g = g.predict(X_test)
    # prediction_k = k.predict(X_test)
    prediction_knn = knn.predict(X_test)
    # prediction_svm = svm.predict(X)

    acc_g = accuracy_score(y_test, prediction_g)
    p_g = precision_score(y_test, prediction_g)
    r_g = recall_score(y_test, prediction_g)
    f1_g = f1_score(y_test, prediction_g)

    print('\nGaussianNB:')
    print('accuracy:  {:5.4} %'.format(acc_g * 100))
    print('precision: {:5.4} %'.format(p_g * 100))
    print('recall:    {:5.4} %'.format(r_g * 100))
    print('f-measure: {:5.4} %'.format(f1_g * 100))
    out.write('G')
    out.write(';')
    out.write(str(acc_g).replace('.', ','))
    out.write(';')
    out.write(str(p_g).replace('.', ','))
    out.write(';')
    out.write(str(r_g).replace('.', ','))
    out.write(';')
    out.write(str(f1_g).replace('.', ','))
    out.write(';')



    acc_knn = accuracy_score(y_test, prediction_knn)
    p_knn = precision_score(y_test, prediction_knn)
    r_knn = recall_score(y_test, prediction_knn)
    f1_knn = f1_score(y_test, prediction_knn)

    print('\nKNN:')
    print('accuracy:  {:5.4} %'.format(acc_knn * 100))
    print('precision: {:5.4} %'.format(p_knn * 100))
    print('recall:    {:5.4} %'.format(r_knn * 100))
    print('f-measure: {:5.4} %'.format(f1_knn * 100))
    out.write('KNN')
    out.write(';')
    out.write(str(acc_knn).replace('.', ','))
    out.write(';')
    out.write(str(p_knn).replace('.', ','))
    out.write(';')
    out.write(str(r_knn).replace('.', ','))
    out.write(';')
    out.write(str(f1_knn).replace('.', ','))


    acum_acc_g += accuracy_score(y_test, prediction_g)
    acum_r_g += precision_score(y_test, prediction_g)
    acum_p_g += recall_score(y_test, prediction_g)

    acum_acc_knn += accuracy_score(y_test, prediction_knn)
    acum_r_knn += precision_score(y_test, prediction_knn)
    acum_p_knn += recall_score(y_test, prediction_knn)

    out.write('\n')

out.close()

print('\nMedias:')
print('GaussianNB:')
print('accuracy:  {:5.4} %'.format((acum_acc_g / 10) * 100))
print('precision: {:5.4} %'.format((acum_r_g / 10) * 100))
print('recall:    {:5.4} %'.format((acum_p_g / 10) * 100))

print('\nKNN:')
print('accuracy:  {:5.4} %'.format((acum_acc_knn / 10) * 100))
print('precision: {:5.4} %'.format((acum_p_knn / 10) * 100))
print('recall:    {:5.4} %'.format((acum_r_knn / 10) * 100))
