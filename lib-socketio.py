import os
import socketio
import json
import connection

from alarm_masks import masks

ws_host = 'iter-websockets.iter.sc'
ws_port = '8081'

sio = socketio.Client(ssl_verify=False)

@sio.event
def connect():
  channel = connection.get_channel()
  sio.emit('psubscribe', channel)
  print('connection established')

@sio.event
def disconnect():
  print('disconnected from server')

@sio.on('message')
def message(response):
  data = response['data']
  converted = json.loads(data)['t']
  mask = converted['alarm_mask']
  print('New message: ' + masks.get(str(mask), 'mask not found').lower().replace('_', ' '))
  print(converted)

sio.connect('https://' + ws_host + ':' + ws_port)
sio.wait()
