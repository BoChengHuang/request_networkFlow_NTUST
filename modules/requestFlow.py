#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup
import datetime
import requests
import time

class RequestFlow(object):
	def __init__(self):
		super(RequestFlow, self).__init__()

	_STATE = "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"
	_VALIDATION = "XvYoM9GBy3IabMc7F4f83TNc4msICd/AtKw5e5Z5ou9m0HKIZ7asfqqu3YIjJeLogIhRfonUQBJosB0TL651O8NIYSGHjnJpzbUQyRY/yl9s13pAMoECqVfd6mtuGHjZH0hB9F8i4/a9z6XtAsPJv5Uka3owDFspA+Zzl3wrnDKsQVff1sENzEl3h7tBt7EgbCTAhxCaQkzssOH6W+2FBVRrBvrIQCCA87TXtk81JP/7rwczJH/IWDz0UZRZADb33SkhyCJ3QKBWhTKx5Mbg2YwVyw+iprnIPm55nqS6VyIKckTYbWDpVeHmc3/Fbpnibq8mqfm3OY2o2t5Nh1tFuD960kgrpN2A2c2smUZjgTAX+e5zNYa6/AXqtW6UtKFgwFcjJjB4xbCtsDYq7ZHDVFRt74USgrnMlVzwzNdb3H+mBx4wLZTMVoEL2tjsbO9eu4yFbZNUqppQ6SvvP0acMrkymzASeFDTHj03zYKluMG9BIuM7i3GLDy9bPO5Kl0vFGAZ2Q9gTUWjVeGaoJx6h5j7SqMRheIqib9gOI8ZKs2cvInOotMH4U2ukhYuOWrtO3mXG4bUoPT/KtTdPp7dcd1qxJfC7W7/88YURbdXnT0pX9tO/+F1rPd/Z5ZNNqJNoEuE1MnoDR+xJhGEJDMr+5nvA9Ira7yqm2s5kXWf78p+HaGdf/PYWrRQ/hXn5nYrdgsabWsqhAJZX4RZRJ01aRapKyAwysqnigzlclvkCHFJqAf5muWN0UieeRx9Fpex2eBK7KpFYZRg/60dW1yQ9BS1RZ5hzrzQfCziMVmGsrzY7GHGxhfLIxc73fAwcw6kqF1yEQieMz41ZXv86K4QlrCWd/wzzRmd9IC1wHwhSUlUMTHIzPS84gQ4/aCAvFS2PvOuNxhpyhCZH5GRIJeb31g44Dh/pVbjkTYObLJ888VKRTOqsm7YvR3XUEjkOVzGSrTqASguoqVqOpCsLRyZG3R5Gfq8hDqQQ+lGv/OWJaAVoRQvjBVSyLqB06HHSqkOg0T6BCwHmW7S0ZrgpJJH0kPOjGcQ6gl2KsBUErC3jBTRZ6ZG7J/GXpnY7fQpPxRFBA9bl4IavVTLU8CPIiSojWdsr9P/fSgGR1G8VCxCBBlDphtmkdmrxkp8JmGcAejl8+mFHvE1/01EAYBFP7Ndge+395rvLZ6Xt6VIOlW6IQRNRew3x9S+Wid+7WNXR9i5"
	_url = "http://network.ntust.edu.tw/flowstatistical.aspx"

	now = datetime.datetime.now()

	def _requestFlow(self, ip, fieldToPost):

	    headers = {"User-Agent": "Mozilla/4.0 (compatible;)"};
	    r = requests.post(self._url, {
	        fieldToPost[0]: self._STATE,
	        fieldToPost[1]: "67237148",
	        fieldToPost[2]: self._VALIDATION,
	        fieldToPost[3]: str(ip),
	        fieldToPost[5]: self.now.year,
	        fieldToPost[6]: self.now.month,
	        fieldToPost[7]: self.now.day, # set timezone
	        fieldToPost[8]: "1048576",
	        fieldToPost[4]: "檢視24小時流量"
	    })

	    soup_ntust = BeautifulSoup(r.text, "html.parser")
	    all_divs = soup_ntust.find_all("div")
	    div = all_divs[5].find_all("td")
	    download, upload, total = div[1], div[2], div[3]
	    return total.getText().strip()

	def _getFields(self):

	    page = urllib2.urlopen(self._url)
	    soup = BeautifulSoup(page, "html.parser")

	    # data field to POST
	    fieldToPost = [];
	    # print soup.title.string
	    all_inputs = soup.find_all("input")
	    for ipts in all_inputs:
	        fieldToPost.append(ipts.get("name"))
	    all_selects = soup.find_all("select")
	    for selects in all_selects:
	        fieldToPost.append(selects.get("name"))
	    return fieldToPost