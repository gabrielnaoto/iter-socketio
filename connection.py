import os
import base64
import requests

host = 'https://iter-api.itertelemetria.com/v1/'
username = os.environ['ITER_USERNAME']
password = os.environ['ITER_PASSWORD']

def url(endpoint):
  return '{host}{endpoint}'.format(host=host, endpoint=endpoint)

def encode(message):
  message_bytes = message.encode('ascii')
  encoded = base64.b64encode(message_bytes)
  base64_message = encoded.decode('ascii')
  return base64_message

def sign_in():
  token = encode('{username}:{password}'.format(username=username, password=password))
  headers = {'Authorization': 'Basic {}'.format(token)}
  response = requests.get(url('sign_in'), headers=headers)
  print(response)

  if response.status_code == 200:
    return response.json()
  else:
    return None

def get_token():
  return sign_in()['token']

def get_channel():
  return sign_in()['realtime_channel_name']
