# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:35:34 2018

@author: A
"""

import time
import urllib
import json 
import requests
from dbhelper import DBHelper

db = DBHelper()


TOKEN = "574106209:AAFPUTE7FpC6FfoPZX7OOvds5j-8tKT0oMs"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}?".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):
    #print(json.dumps(updates, indent=4, sort_keys=True))
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text               = updates["result"][last_update]["message"]["text"]
    chat_id            = updates["result"][last_update]["message"]["chat"]["id"]
    interlocutor_name  = updates["result"][last_update]["message"]["from"]["first_name"]
    return (text, chat_id, interlocutor_name)


def send_message(text, chat_id, interlocutor_name, reply_markup=None ):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text + interlocutor_name, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text               = update["message"]["text"]
            chat               = update["message"]["chat"]["id"]
            interlocutor_name  = update["message"]["from"]["first_name"]
            send_message(text, chat, interlocutor_name)
        except Exception as e:
            print(e)

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text               = update["message"]["text"]
            chat               = update["message"]["chat"]["id"]
            interlocutor_name  = update["message"]["from"]["first_name"]
            items              = db.get_items(chat)
            if text == "/done":
                keyboard=build_keyboard(items)
                send_message("Select an item to delete", chat, interlocutor_name, keyboard)
            elif text == "/start":
                send_message("Welcome to your personal To Do list. Send any text to me and I'll store it as an item. Send /done to remove items", chat)
            elif text.startswith("/"):
                continue    
            elif text in items:
                db.delete_item(text, chat)
                items    = db.get_items(chat)
                keyboard = build_keyboard(items)        
                send_message("Select an item to delete", chat, interlocutor_name, keyboard)            
            else:
                db.add_item(text, chat)
                items = db.get_items(chat)
                message = "\n".join(items)
                send_message(message, chat, interlocutor_name)
        except KeyError:
            print("Error")
            pass

                
def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)
    
    
def main():
    db.setup()
    last_update_id = None
    while True:
        print("loop")
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0 :
            last_update_id = get_last_update_id(updates) + 1
            #echo_all(updates)
            handle_updates(updates)
        time.sleep(0.1)


if __name__ == '__main__':
    main()    

#text, chat, interlocutor_name = get_last_chat_id_and_text(get_updates())
#send_message(text, chat, interlocutor_name)



