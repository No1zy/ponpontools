# -*- coding: utf-8 -*-:q

import argparse
import re
import sys

OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
PURPLE= "\033[95m"
CYAN= "\033[96m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Log file to analyze')
parser.add_argument("--command",'-c', help='host-list | grep')
parser.add_argument('--all', '-a', help='grep option all grep. please regexp')
parser.add_argument('--time', '-t', help='grep option time')
parser.add_argument('--ip', '-i', help='grep option IP Address')
parser.add_argument('--status', '-s', help='grep option status code')

args = parser.parse_args()

f = open(args.file, 'r')

def isKey(text):
    reg = "host|time|forwardedfor|req|status|size|referer|ua|reqtime|vhost"
    key = re.compile(reg)
    return True if key.match(text) else False

def exp_status(reg,target):
    reg_status = re.compile(reg)
    result = reg_status.search(target)
    return result.group() if result else False

def print_log(logs, match_text=None, match_key=None):
    reg_status_ok = '^2[0-9][0-9]$'
    reg_status_ng = '^4[0-9][0-9]$|^5[0-9][0-9]$'
    status_ok = re.compile(reg_status_ok)
    status_ng = re.compile(reg_status_ng)
    for key,value in logs.items():
        #if match_text != None and match_key != None:
        if match_key == key:
            split_str = value.split(match_text)
            if key == "time":
                print(key + ': ' + split_str[0] + FAIL + match_text + ENDC + split_str[1])
            elif key == "req":
                print('\t' + key + ': ' + split_str[0] + FAIL + match_text + ENDC + split_str[1])
            else:
                print('\t' + key + ': ' + split_str[0] + FAIL + match_text + ENDC + split_str[1])
        elif key == "time":
            print(WARNING + key + ': ' + value + ENDC)
        elif key == "host":
            print(OKGREEN + '\t' + key + ': ' + value + ENDC)
        elif key == "req":
            print(PURPLE +'\t'+ 'URI: ' + value + ENDC)
        elif key == "reqtime":
            continue
        elif key == "referer":
            print(OKBLUE +'\t' + key + ': ' + value + ENDC)
        elif key == "status":
            if status_ok.match(value):
                print(OKGREEN + '\tstatus: ' + value + ENDC)
            elif status_ng.match(value):
                print(FAIL + '\tstatus: ' + value + ENDC)
            else:
                print('\tstatus: ' + value)
        else:
            print('\t'+ key +': ' + value)
    

def tag_search(logs,tag):
    return [log[tag] for log in logs]

def host_list(logs):
    lis = tag_search(logs,'host')
    print('     Host              access count      ')
    for host in list(set(lis)):
        print('{0:15s}          {1}'.format(host,str(lis.count(host))))

def all_grep(logs,text):
    for key, value in logs.items():
        group = exp_status(text,value)
        if group:
            return group, key
    return False
            

def grep_search(logs,elm=None,reg=None,status=None):
    for line in logs:
        if elm == 'all' and reg != None:
             result = all_grep(line,reg)
             if result:
                 print_log(line,result[0], result[1])
        elif reg == None and elm == 'all':
             if status != None:
                 exp_status(status,line['status']) and print_log(line)
        elif line[elm].find(reg) >= 0:
             if status == None:
                 print_log(line)
             elif status != None:
                 if exp_status(status,line['status']):
                     print_log(line)
logs = []
line = f.readline()
while line: 
    line = f.readline()
    if len(line) is 0:
        break
    dic = dict()
    for element in line.split('\t'):
        parts = element.split(':')
        req_dict = {parts[0]: ':'.join(parts[i].replace('\n','') for i in range(1,len(parts)))}
        if len(req_dict) > 0: 
            dic.update(req_dict)
    logs.append(dic)
f.close()

if args.command is not None:
    if args.command == "host-list":
        host_list(logs)
    elif args.command == "grep":
        if args.all != None:
            grep_search(logs, 'all', args.all)
        elif args.time != None:
            grep_search(logs,'time',args.time, args.status)
        elif args.ip != None:
            grep_search(logs,'host', args.ip, args.status)
        elif args.status != None:
            grep_search(logs, 'all', None,args.status)
else:
    print(logs)
