# -*- coding: utf-8 -*-
#%%

#Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server

#%%
from flask import Flask, jsonify

server = Flask("phonebook server ")

phonebook = {"flo" : "123456789",
              "pepe": "987654321",
              "pope":"9999999999",
              "hawkins": "2357911"}


@server.route("/phonebook")
def phonebook_handler():
    return jsonify(phonebook)


@server.route("/phonebook/<name>")
def getphone_handler(name):
    for i in phonebook:
        if i == name:
            return  jsonify(phonebook[name])
    return jsonify({"message":"Cannot find the name "+ str(name) + " in the phonebook, press button to add contact"})


@server.route("/add_contact/<name>/<phone>", methods = ["POST"])
def add_contact_handler(name,phone):
    for i in phonebook:
        if i == name:
            return jsonify({"message":"Contact already exists"})
    phonebook[name] = str(phone)   
    return jsonify({"message":"Contact has been added"})
        

@server.route("/delete_contact/<name>", methods = ["DELETE"])
def delete_contact_handler(name):
    for i in phonebook:
        if i == name:
            phonebook.pop(name)
            return jsonify("Contact has been deleted!")
    return jsonify({"message":"Cannot find the name "+ str(name) + " in the phonebook, press button to add contact"})

@server.route("/update_contact/<name>/<phone>", methods = ["POST"])
def update_contact_handler(name,phone):
    for i in phonebook:
        if i == name:
            phonebook[name] = str(phone) 
            return jsonify({"message":"Contact has been added"})
    return jsonify({"message":"Cannot find the name "+ str(name) + " in the phonebook, press button to add contact"})

    


server.run()