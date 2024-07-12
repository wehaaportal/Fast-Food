#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Load '''
import os, sys, socket, time

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def is_connected_to_internet() -> bool:
    try:
        socket.gethostbyname("google.com")
        connection = socket.create_connection(("google.com", 80), timeout=1)
        connection.close()
        return True
    except socket.error:
        return False
    
#
# person = {
#    'surname': 'str',
#    'name': 'str',
#    'dob': '00/00/0000',
#    'gender': 'M' or 'F'
# }
#
def Usr_id(person: dict) -> str:
    months = ' ABCDEHLMPRST'
    
    def get_v(s):
        return ''.join([c for c in s.upper() if c in 'AEIOU'])
    
    def get_c(s):
        return ''.join([c for c in s.upper() if c not in 'AEIOU'])
    
    def code(s):
        return (get_c(s) + get_v(s) + 'XXX')[:3]
    
    d, m, y = person['dob'].split('/')
    
    s_code = code(person['surname'])
    f_con = get_c(person['name'])
    f_code = f_con[:3] if len(f_con) > 3 else code(person['name'])
    
    n_code = y[-2:] + months[int(m)] + (f'{int(d):02d}' if person['gender'] == 'M' else f'{int(d) + 40:02d}')
    
    return s_code + f_code + n_code # Salida: RSSMRA85D15
