#!/usr/bin/python

# This is the CLI version of SimplyPy
# The instructions available are : 
# println! { <string> and println! # <variable>
# Mathematicals operations :  '+' '-' '/' '*' 'sqrt'
# Variables declaration : let <name> <value>

variables = dict()

def saisie():
    saisie = input('>>> $ ')
    splited = saisie.split(' ', 2)


    if(splited[0] == 'println!'):
        if(splited[1] == '{'):
            toShow = splited[2]
            print(toShow)
        if(splited[1] == '#'):
            instruct =  splited[2]
            if(instruct in variables.keys()):
                print(variables[instruct])
            else:
                print('No variable named "' + splited[2] + '"')

    if(splited[0] == 'let'):
        variables[splited[1]] = splited[2]
        print('Val \'' + str(splited[2]) + '\' assigned to ' + str(splited[1]))
    
        
    elif(splited[0] != 'println!' and splited[0] != 'let'):
        if(splited[0] in variables.keys() and splited[2] in variables.keys()):
            if(splited[1] == '+'):
                print(variables[splited[0]] + variables[splited[2]])
        else:
            print('Error, "' + splited[0] + '" doesn\'t exists')

while True:
    saisie()