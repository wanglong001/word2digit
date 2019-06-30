#! /usr/local/env python
from pypinyin import pinyin
import Levenshtein
import sys
import os

"""
汉字转数字
依赖：
    pip install python-Levenshtein
    pip install pypinyin
"""

digitMap = {
        "0" : pinyin('零洞') ,
        "1" : pinyin('幺一') ,
        "2" : pinyin('二') ,
        "3" : pinyin('三') ,
        "4" : pinyin('四实') ,
        "5" : pinyin('五') ,
        "6" : pinyin('六') ,
        "7" : pinyin('七') ,
        "8" : pinyin('八') ,
        "9" : pinyin('九') ,
        }

class Word2Digit:
    def __init__(self):
        self.digitMap = digitMap

    def transform(self, word):
        resDigit = ""
        minDistance = 100
        for digit, pinyinList in self.digitMap.items():
            for p in pinyinList:
                for w in pinyin(word):
                    distance = Levenshtein.distance(w[0], p[0])
                    if minDistance > distance:
                        minDistance = distance
                        resDigit = digit
        return resDigit 

if __name__ == '__main__':
    #print(digitMap)
    
    if len(sys.argv) < 2:
        print("Usages: {} <输入文件> <输出文件>".format(sys.argv[0]))
        exit(0)

    inputFlp = os.path.realpath(sys.argv[1])
    outputFlp = os.path.realpath(sys.argv[2])
    outputDir = os.path.dirname(outputFlp)
    os.makedirs(outputDir, exist_ok=True)
    model = Word2Digit()
    
    resList = []
    with open(inputFlp, "r") as fin:
        lines = fin.readlines()
        for line in lines:
            outputLine = ""
            for word in line.strip():
                digit = model.transform(word)
                outputLine += digit
            outputLine += "\n"
            resList.append(outputLine)

    with open(outputFlp, "w") as fout:
        fout.writelines(resList)

    #a = model.transform('实')
    #print(a)

     
