# -*- coding: utf-8 -*-
# http://aiweeklynews.com/archives/50653819.html
# sklearnの重要度はgini係数
# RandomForestClassifier
# シャッフルとかしないタイプ


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
    inputF   = args[1] # 1行目はタイトル行、1列目は目的変数のデータセット（tsv）
    #predItem = args[2] # 目的変数のタイトル
    saveName = args[2] # 保存ファイル名
else:
    print ("\n[Exec] python plotImportance_forweb.py [inputFile(tsv)] [savefilename(png)]")
    print ("[Exec] python plotImportance_forweb.py wine.txt important_wine")
    exit()


X = pd.read_table(inputF) # デフォルトでheader1行目
predItem = list(X.columns)[0]
yItem = X.pop(predItem) # 目的変数を除く ～pop:xからpredItemを除いてyに格納
yItem = yItem.astype('int') # ←整数にする
#print (yItem, type(yItem))
#exit()


x = X.to_numpy()
y = yItem.to_numpy()
#print(type(X), type(y))


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# 学習
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(x_train, y_train)

#予測データ作成
y_predict = clf.predict(x_train)

# 評価レポート
#print(classification_report(y_train, y_predict))


#特徴量の重要度
feature = clf.feature_importances_

#特徴量の重要度を上から順に出力する
f = pd.DataFrame({'number': range(0, len(feature)),
             'feature': feature[:]})
f2 = f.sort_values('feature',ascending=False)

#特徴量群
label = X.columns[0:]
#print (label,"####")


#特徴量の重要度順（降順）
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


