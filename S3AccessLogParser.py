# coding:utf-8

from __future__ import print_function
import os
import sys
import locale
import codecs
import traceback

def SimpleCharDet(b_str):
    def TryDecode(b_str, c_code):
        try:
            b_str.decode(c_code)
            return c_code
        except UnicodeDecodeError:
            return 'UDError'
    c_code_list = ['us-ascii', 'utf-8', 'cp932', 'eucjp']
    for c_code in c_code_list:
        if TryDecode(b_str, c_code) != c_code_list: return c_code
    return 'unknown'

def GetCoding(filepath):
    locale.setlocale(locale.LC_ALL, '')
    maxsize = 1 * 1024 * 1024
    def SysExit(e, errorMsg):
        sys.exit("Error: {4} '{0}' [{1}]: {2}".format(filepath, e.errno, e.strerror, errorMsg))
    def TryRead(f_in):
        try:
            return f_in.read(maxsize)
        except IOError as e:
            SysExit(e, 'cannot read from file')
    def TryOpen():
        try:
            with open(filepath, 'rb') as f_in: return TryRead(f_in)
        except IOError as e:
            SysExit(e, 'cannot open file')
    return SimpleCharDet(TryOpen())

def FileInput(filepath):
    with codecs.open(filepath, mode = 'r', encoding = GetCoding(filepath)) as file: return(file.read())

def LogSplit(logfile):
    log_list = []
    for one_str in logfile.splitlines():
        log_split, log_elem, paren_flag, quote_flag = [], "", False, False
        for one_char in list(one_str):
            if one_char == ' ':
                if not paren_flag and not quote_flag:
                    log_split.append(log_elem)
                    log_elem = ""
                else: log_elem += one_char
            elif one_char == '[': paren_flag = True
            elif one_char == ']': paren_flag = False
            elif one_char == '"': quote_flag = not quote_flag
            else: log_elem += one_char
        log_list.append(log_split)
    return log_list

def LogOutput(dirpath):
    for filename in os.listdir(dirpath):
        try:
            logfile = FileInput(dirpath + filename)
            for log in LogSplit(logfile): print(log)
        except KeyboardInterrupt:
            sys.exit()
        except:
            traceback.print_exc()

LogOutput(sys.argv[1])
