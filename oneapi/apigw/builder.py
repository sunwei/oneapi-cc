# -*- coding: utf-8 -*-
import json


def start_build():

    with open('api-conf-example.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    return data

