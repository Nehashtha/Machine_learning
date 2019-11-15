import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def open_file(dataset_list):

        files=[]
        for data in dataset_list:
            # for nature in nature_list:
            folder_path_neg = r"aclImdb\\"+data+"\\neg"
            folder_path_pos=r"aclImdb\\"+data+"\\pos"

            fileNames_neg= os.listdir(folder_path_neg)
            fileNames_pos=os.listdir(folder_path_pos)
            count=0
            for i in fileNames_neg:
                neg = open("C:\\Users\\Neha\\Downloads\\python project\\aclImdb\\"+data+"\\neg\\" + i, 'r')
                neg_read=neg.read()
                count=count+1
                files.append(neg_read)
                if count<100:
                    print(neg_read)
                else:
                    break
            count_pos=0
            for j in fileNames_pos:
                pos = open("C:\\Users\\Neha\\Downloads\\python project\\aclImdb\\"+data+"\\pos\\" + j, 'r')
                pos_read=pos.read()
                count_pos=count_pos+1
                files.append(pos_read)
                if count_pos<100:
                    print(pos_read)
                else:
                    break
        # print(len(files))
        count_vector=countvectorizer(files)
        return count_vector

def countvectorizer(files_list):
    cv = CountVectorizer()
    X = cv.fit_transform(files_list)
    lst = cv.get_feature_names()
    vector_array = X.toarray()
    print(vector_array.shape)
    print(len(files_list))
    print(vector_array)
    logistic_alg=algorithm(vector_array)
    print(logistic_alg)


def algorithm(vector_array):

    x = vector_array
    print(x)
    # print(x_train)
    y = []
    for i in range(0,2):
        y1= np.zeros((100, 1))
        y2 = np.ones((100, 1))
        y.extend(y1)
        y.extend(y2)
    print(y[200:])
    # print(x.size)
    # print(x.shape)
    # print(y)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                             multi_class='multinomial').fit(x[:200, :], np.ravel(y[:200]))

    pred = clf.predict(x[200:, :])
    print(pred)
    print(type(pred))
    # clf.score(x,y)
    from sklearn.metrics import accuracy_score
    acc = accuracy_score(pred, np.ravel(y[200:]))
    a = int(acc * 100)
    print(a,'%')

    # clf_svm = SVC(gamma='auto')
    # clf_svm.fit(x[:200, :], y[:200])
    #
    # pred_svm = clf_svm.predict(x[200:, :])
    # acc = accuracy_score(pred_svm, y[200:])
    # a = int(acc * 100)
    # print(a, '%')

def main():
    data_list=['test','train']
    # character_list=['neg','pos']
    to_open_file=open_file(data_list)
    print(to_open_file)


main()
