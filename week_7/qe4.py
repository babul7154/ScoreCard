# -*-coding:utf-8 -*-
"""
@File    :   qe4.py
@Time    :   2024/03/13 23:06:40
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   You are given certain details of the trains that stop at a station. Your task is to store these details in a nested dictionary.

The first line of input is n, the number of trains that stop at the station. n blocks of input follow. The first line in each block corresponds to the train name. The second line in each block corresponds to m, the number of compartments in the train.
m lines of input follow. Each of these m lines has two values separated by a comma: name of the compartment and number of passengers in it.

Your task is to create a nested dictionary named station_dict. The keys of the dictionary are train names, the value corresponding to a key is another dictionary. The keys of the inner dictionary are the compartment names in this train, the values are the number of passengers in each compartment. For example:
Your task is to create a nested dictionary named station_dict. The keys of the dictionary are train names, the value corresponding to a key is another dictionary. The keys of the inner dictionary are the compartment names in this train, the values are the number of passengers in each compartment. For example:

{
    'Mumbai Express': {
        'S1': 10,
        'S2': 20,
        'S3': 30
    },
    'Chennai Express': {
        'S1': 10,
        'S2': 20,
        'S3': 30
    }
  }
=================================================
  Input    :   2                   | Output : None
  Input    :   Mumbai Express      | Output : None
  Input    :   2                   | Output : None
  Input    :   S1,10               | Output : None
  Input    :   S2,20               | Output : None
  Input    :   Chennai Express     | Output : None
  Input    :   3                   | Output : None
  Input    :   S1,5                | Output : None
  Input    :   S2,10               | Output : None
  Input    :   S3,15               | Output : None
=================================================
(1) The values of the compartments should be represented as integers and not as strings.
(2) You do not have to print the output to the console. Do not try to print the output that you observe in the "Expected Output". You just have to process the input and create the dictionary station_dict.
"""
n = int(input())
station_dict = dict()
for i in range(n):
    dict_temp = dict()
    train_name = input()
    wagon_no = int(input())
    for i in range(wagon_no):
        wagon_detail = input().split(",")
        dict_temp.update({wagon_detail[0]: int(wagon_detail[1])})
    station_dict.update({train_name: dict_temp})
print(station_dict)
