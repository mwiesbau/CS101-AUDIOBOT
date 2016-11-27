"""
Created on 12 October 2016
@author: Mathias Wiesbauer
"""

import requests
import json
from datetime import datetime
import time
import globalz
import mod


hostname = "10.0.75.2"
port = "7272"
api_key = "audiobot"


def update_big_value(tile, description, maintitle, mainvalue, title1, value1, \
                     title3, value3):
    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"
        
    ######  THE TEXT TO BE PUBLISHED ####
    text_data = {'title': maintitle, 'description': description, 'big-value': mainvalue, \
                 'upper-left-label': title1, 'upper-left-value': value1, \
                 'upper-right-label': title3, 'upper-right-value': value3}
    json_text = json.dumps(text_data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "big_value", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}
   

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text

def update_big_value_config(tile, color="", background="False"):
    url = "http://" + hostname + ":" + port + "/api/v0.1/" + api_key + "/tileconfig/" + tile

    value_data = {'big_value_color': color,                  
                  'fading_background': background}

    json_value_data = json.dumps(value_data)  # CONVERT TO JSON
    payload = {'value': json_value_data}
    r = requests.post(url, data=payload)
   #print r.text
    
def update_just_value(tile, title, description, value):
    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"
    if tile == 'orangeavg' and globalz.state == 0:
        globalz.orangeDecibelSum += float(value)
        globalz.orangeAvgCount += 1
        value = globalz.orangeDecibelSum / globalz.orangeAvgCount
        print globalz.state
        
    if tile == 'blueavg' and globalz.state == 2:
        globalz.blueDecibelSum += float(value)
        globalz.blueAvgCount += 1
        value = globalz.blueDecibelSum / globalz.blueAvgCount
        
    ######  THE TEXT TO BE PUBLISHED ####
    text_data = {'title': title, 'description': description, 'just-value': value}
    json_text = json.dumps(text_data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "just_value", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}
   

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text

def update_just_value_config(tile, color="", background="False"):
    url = "http://" + hostname + ":" + port + "/api/v0.1/" + api_key + "/tileconfig/" + tile

    value_data = {'just-value-color': color,                  
                  'fading_background': background}

    json_value_data = json.dumps(value_data)  # CONVERT TO JSON
    payload = {'value': json_value_data}
    r = requests.post(url, data=payload)
   #print r.text

def update_state():
    if globalz.state == 0:
        globalz.state = 1
        return
    if globalz.state == 1:
        globalz.state = 2
        return
    if globalz.state == 2:
        globalz.state = 0

def update_text(tile, string=""):
    """
    :param tile:test
    :param string:
    :return:
    """
    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"

    ######  THE TEXT TO BE PUBLISHED ####
    text_data = {'text': string}
    json_text = json.dumps(text_data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "text", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text

def update_text_config(tile, color="", size="", weight=""):
    url = "http://" + hostname + ":" + port + "/api/v0.1/" + api_key + "/tileconfig/" + tile

    value_data = {'font_color': color,
                  'font_size': size,
                  'font_weight': weight}

    json_value_data = json.dumps(value_data)  # CONVERT TO JSON
    payload = {'value': json_value_data}
    r = requests.post(url, data=payload)
   #print r.text

def update_pie_chart(tile, maintitle, redtitle, bluetitle, reddata, bluedata):

    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"


    ######  THE TEXT TO BE PUBLISHED ####
    text_data = {'title': maintitle, 'pie_data': [[redtitle, reddata], [bluetitle, bluedata]]}
    json_text = json.dumps(text_data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "pie_chart", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text

def update_bar_chart(tile, maintitle, subtitle, label, redvalue, bluevalue):

    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"


    ######  THE TEXT TO BE PUBLISHED ####
    text_data = {'title': maintitle, 'subtitle': subtitle, 'ticks': [label], \
                 'series_list': [[redvalue], [bluevalue]]}
    json_text = json.dumps(text_data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "bar_chart", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text

def update_fancy_listing(tile, data):

    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"

    ######  THE TEXT TO BE PUBLISHED ####
    json_text = json.dumps(data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "fancy_listing", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text


def update_advanced_plot(tile, data):

    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"

    ######  THE TEXT TO BE PUBLISHED ####
    json_text = json.dumps(data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "advanced_plot", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)
    #print r.text



def update_fancy_listing_config(tile):
    url = "http://" + hostname + ":" + port + "/api/v0.1/" + api_key + "/tileconfig/" + tile

    value_data = {'vertical_center': False,
                  "3": {"label_color": "red"}}


    json_value_data = json.dumps(value_data)  # CONVERT TO JSON
    payload = {'value': json_value_data}
    r = requests.post(url, data=payload)
    #print r.text


def update_date_time(tile):
    """
    Publishes current date time to a tile
    :param tile:
    :return:
    """
    '''
    :param tile: Tile ID in tipboard to publish results to
    :return:
    '''
    #### THE CONNECTION INFO TO THE TIPBOARD APP
    url = "http://"+ hostname + ":" + port + "/api/v0.1/" + api_key + "/push"


    date_time = datetime.now()

    weekdaystring = date_time.strftime("%A")
    timestring = date_time.strftime("%H:%M:%S")
    datestring = date_time.strftime("%Y-%m-%d")


    ######  THE TEXT TO BE PUBLISHED ####
    text_data = {'title': weekdaystring, "description": datestring, "just-value": timestring}
    json_text = json.dumps(text_data)  # CONVERT TO JSON

    ###### THE PAYLOAD
    payload = {'tile': "just_value", 'key': tile, 'data': json_text}
    #headers = {'content-type': 'application/json'}

    ##### SEND DATA TO TILE IN TIPBOARD
    r = requests.post(url, data=payload)

    #print r.text
class Solution:
    # @return an integer
    def atoi(self, str):
        pointer = 0
        isNegative = False
        while pointer<len(str) and str[pointer]==' ':
            pointer += 1
        if pointer==len(str):
            return 0
        if str[pointer] == '-':
            isNegative = True
            pointer += 1
        elif str[pointer] == '+':
            isNegative = False
            pointer += 1
        solution = 0
        for pointer in range(pointer, len(str)):
            if not str[pointer].isdigit():
                break
            else:
                solution *= 10
                solution += int(str[pointer])
                
        #This is because leetcode question is not prepared to Python but to Java/C so we truncate it
        if not isNegative and solution > 2147483647:
            return 2147483647
        elif isNegative and solution > 2147483648:
            return -2147483648
            
        if isNegative:
            return -1 * solution;
        else:
            return solution;
### PUBLISH FANCY LISTING
#data = [
#    {"label": "Barbecue",
#     "text":  "2 Days",
#     "description": "too much meat"}
#]

#update_fancy_listing('listing_unproductive', data)


###### PUBLISH PIE CHART #####
#data1 = {"title": "East Portal",
#        "pie_data": [["Productive", 60], ["Unproductive", 40]]}

#data2 = {"title": "West Portal",
#        "pie_data": [["Productive", 80], ["Unproductive", 20]]}

#update_pie_chart('productivity1', data1)
#update_pie_chart('productivity2', data2)


## PUBLISH LINE CHART
#data = {
#    "title": "Productivity 2014",
#    "description": "",
#    "plot_data": [[[1, 20], [2, 25], [3, 30], [4, 40]],
#                    [[1, 300], [2, 50], [3, 70], [4, 80]]]
#
#}
#update_advanced_plot("productivityTime", data)
