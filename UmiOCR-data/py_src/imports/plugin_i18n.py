# =========================================================
# =============== 为插件提供简易的i18n翻译API ===============
# =========================================================

import os
import csv

TrDict = {}
LangCode = ""


# 设置语言
def setLangCode(langCode):
    global LangCode
    LangCode = langCode


# 载入翻译。每个模块调用tr前，必须载入翻译。
# file: 与翻译文件同目录的任意文件的路径
# name: 翻译文件名
def trLoad(file="", name=""):
    global TrDict
    TrDict = {}
    if not file or not name:
        return
    path = os.path.dirname(os.path.abspath(file)) + "/" + name
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)
                index = -1
                for i, h in enumerate(headers):  # 搜索语言
                    if h == LangCode:
                        index = i
                if index == -1:  # 找不到对应语言
                    if LangCode.startswith("zh_"):  # 中文
                        index = 0
                    else:
                        index = 1  # 找不到对应语言，默认英文
                for row in csv_reader:
                    TrDict[row[0]] = row[index]
    except Exception as e:
        print("[Error] 加载插件翻译失败：", file, name, e)


# 进行翻译。输入原文，返回译文
def tr(original):
    if original in TrDict:
        return TrDict[original]
    return original
