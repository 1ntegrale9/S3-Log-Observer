from __future__ import print_function
from django.shortcuts import render
from .models import CreateRecord
from tqdm import tqdm
import os
import codecs
import traceback


def IndexView(request):
    output('s3log/')
    return render(request, 'analyzer/index.html')


def input(filepath):
    try:
        with codecs.open(filepath, mode='r', encoding='us-ascii') as file:
            return(file.read())
    except Exception:
        traceback.print_exc()
        print(filepath)
        return ""


def parse(log, callback, constraint=None):
    if constraint and not (constraint in log):
        return
    log_split, log_elem, paren_flag, quote_flag = [], "", False, False
    for one_char in list(log):
        if one_char == ' ':
            if not paren_flag and not quote_flag:
                log_split.append(log_elem)
                log_elem = ""
            else:
                log_elem += one_char
        elif one_char == '[':
            paren_flag = True
        elif one_char == ']':
            paren_flag = False
        elif one_char == '"':
            quote_flag = not quote_flag
        else:
            log_elem += one_char
    if log_elem != "":
        log_split.append(log_elem)
    try:
        callback(log_split)
    except Exception as e:
        print(e)


def output(dirpath):
    for filename in tqdm(os.listdir(dirpath)):
        logs = input(dirpath + filename)
        for log in logs.splitlines():
            parse(log, CreateRecord)
