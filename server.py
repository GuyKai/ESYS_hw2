#!/usr/bin/env python3

import socket

import numpy as np
import json
import time
import random

HOST = '192.168.50.163' # Standard loopback interface address
PORT = 65431 # Port to listen on (use ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("waiting...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
