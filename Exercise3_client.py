# -*- coding: utf-8 -*-

#%%

import requests

localhost = "http://127.0.0.1:5000"

def get_phonebook():
    response = requests.get(localhost+"/phonebook")
    if response.status_code == 200:
        return response.json()
    else:
        return "Failure"
    
def get_phone(user):
    response = requests.get(localhost+"/phonebook/"+user)
    if response.status_code == 200:
        return response.json() 
    else:
        return "Failure"

def add_contact(name,phone):
    response = requests.post(localhost+"/add_contact/"+name+"/"+str(phone))
    if response.status_code == 200:
        return response.json()
    else:
        return "Failure"

def delete_contact(name):
    response = requests.delete(localhost+"/delete_contact/"+name)
    if response.status_code == 200:
        return response.json() 
    else:
        return response  
    
def update_contact(name,phone):
    response = requests.post(localhost+"/update_contact/"+name+"/"+str(phone))
    if response.status_code == 200:
        return response.json() 
    else:
        return "Failure"    
    
