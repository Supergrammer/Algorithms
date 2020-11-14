#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#

import requests
import json

def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
    answer, cnt = 0, 0
    
    for i in range(1, 5):
        params = {'status':statusQuery, 'page':i}
        res = requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search', params=params)
        for data in res.json()['data']:
            if data.get('parent') and data['parent']['id'] == parentId:
                answer += data['operatingParams']['rotorSpeed']
                cnt += 1
                
    if cnt == 0: return 0
    answer //= cnt
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    parentId = int(input().strip())

    result = avgRotorSpeed(statusQuery, parentId)

    fptr.write(str(result) + '\n')

    fptr.close()