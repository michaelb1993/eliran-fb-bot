import json
import time
from datetime import datetime

from bunch import Bunch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Site address
SITE_ADDRESS = "https://www.facebook.com/groups/512147718851893/"

# Credentials
CREDS_FILE = "ebs_creds.json"
creds = Bunch(json.load(open(CREDS_FILE, "rb")))

# Order to bounce
ORDER_NUM = 0

# Javascript code
LOGIN_CODE = "document.getElementById('email').value='%s'; document.getElementById('pass').value='%s';document.getElementById('u_0_2').click();" % (creds.user, creds.password)
OPEN_COMMENT_DIALOG = "document.querySelector('[data-pagelet=\"GroupInlineComposer\"]').children[0].children[0].children[0].children[0].children[1].children[0].click();"
WRITE_COMMENT = 'var textbox=document.querySelectorAll(\'[role="textbox"]\');textbox[textbox.length-1].children[0].children[0].children[0].children[0].innerHTML = \'<span data-text="true">blat!</span>\''
POST_COMMENT = 'document.querySelector(\'[aria-label=Post]\').children[0].children[0].click()'


def bounce():
	browser = webdriver.Chrome()
	browser.get(SITE_ADDRESS)
	browser.execute_script(LOGIN_CODE)
	time.sleep(10)
	browser.execute_script(OPEN_COMMENT_DIALOG)
	time.sleep(2)
	browser.execute_script(WRITE_COMMENT)
	browser.execute_script([[POST_COMMENT]])

	# After done posting close thr browser
	# browser.close()


def main():
	while True:
		try:
			bounce()
			print('Done bounce, finish time:\t%s' % datetime.now())
			# Every 4 hours
			time.sleep(4 * 60 * 60)
		except KeyboardInterrupt:
			break


if __name__ == '__main__' :
	main()
