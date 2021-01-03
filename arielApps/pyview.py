import webview
import json
import requests
import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()
window = webview.create_window('Ariel Billboard', 'http://arielapps.com/')
def on_closed():
    print('pywebview window is closed')


def on_closing():
    print('pywebview window is closing')


def on_shown():
    print('pywebview window shown')

@tl.job(interval=timedelta(seconds=1))
def on_loaded():
	req 	= requests.get(url='http://127.0.0.1:5000/arielAds')
	data = json.loads(req.text)
	for x in range(len(data)):
		webview.windows[0].load_url(data[x])
		print(data[x])
		time.sleep(10)


if __name__ == '__main__':
	tl.start()
	webview.start()
	while True:
		try:
			time.sleep(0.333)
		except KeyboardInterrupt:
			tl.stop()
			break