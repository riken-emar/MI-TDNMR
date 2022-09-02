# -*- coding: utf-8 -*-
# http://aiweeklynews.com/archives/50653819.html
# sklearn�̏d�v�x��gini�W��
# RandomForestClassifier
# �V���b�t���Ƃ����Ȃ��^�C�v


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


argLen = 3
args = sys.argv
if (len(args)==argLen):
    inputF   = args[1] # 1�s�ڂ̓^�C�g���s�A1��ڂ͖ړI�ϐ��̃f�[�^�Z�b�g�itsv�j
    #predItem = args[2] # �ړI�ϐ��̃^�C�g��
    saveName = args[2] # �ۑ��t�@�C����
else:
    print ("\n[Exec] python plotImportance_forweb.py [inputFile(tsv)] [savefilename(png)]")
    print ("[Exec] python plotImportance_forweb.py wine.txt important_wine")
    exit()


X = pd.read_table(inputF) # �f�t�H���g��header1�s��
predItem = list(X.columns)[0]
yItem = X.pop(predItem) # �ړI�ϐ������� �`pop:x����predItem��������y�Ɋi�[
yItem = yItem.astype('int') # �������ɂ���
#print (yItem, type(yItem))
#exit()


x = X.to_numpy()
y = yItem.to_numpy()
#print(type(X), type(y))


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# �w�K
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(x_train, y_train)

#�\���f�[�^�쐬
y_predict = clf.predict(x_train)

# �]�����|�[�g
#print(classification_report(y_train, y_predict))


#�����ʂ̏d�v�x
feature = clf.feature_importances_

#�����ʂ̏d�v�x���ォ�珇�ɏo�͂���
f = pd.DataFrame({'number': range(0, len(feature)),
             'feature': feature[:]})
f2 = f.sort_values('feature',ascending=False)

#�����ʌQ
label = X.columns[0:]
#print (label,"####")


#�����ʂ̏d�v�x���i�~���j
indices = np.argsort(feature)[::-1]

print("No\tItem\tImportanceScore")
for i in range(len(feature)):
    print(str(i + 1) + "\t" + str(label[indices[i]]) + "\t" + str(feature[indices[i]]))

fig = plt.figure()
plt.title('Feature Importance')
plt.bar(range(len(feature)),feature[indices], color='lightblue', align='center')
plt.xticks(range(len(feature)), label[indices], rotation=90)
plt.xlim([-1, len(feature)])
plt.subplots_adjust(left=0.6)
plt.tight_layout()
plt.ylabel("Importance")
#plt.show()

outfileName = saveName
fig.savefig(outfileName)

#print("\nSaved graph file: "+outfileName)


