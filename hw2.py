#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from collections import deque
import json

import socket
import json

# plot

plt.ion() # turn interactive mode on
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

DATA_POINTS = 5
AXIS_LIMITS = (-1200, 1200)

points = deque([])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_xlim3d(AXIS_LIMITS[0], AXIS_LIMITS[1])
ax.set_ylim3d(AXIS_LIMITS[0], AXIS_LIMITS[1])
ax.set_zlim3d(AXIS_LIMITS[0], AXIS_LIMITS[1])
plt.show()

# socket

HOST = '192.168.50.163'  # Standard loopback interface address 
PORT = 65431            # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	print("waiting...")
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			dataString = conn.recv(1024).decode('utf-8')
			# print('Received from socket server : ', dataString)

			data = json.loads(dataString)
			# print(data)

			points.append(ax.scatter(data['x'], data['y'], data['z']))
			while(len(points) > DATA_POINTS):
				points.popleft().remove()
			plt.pause(0.05)
