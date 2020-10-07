# import requests
# import json
#
# def sendASMS(contactno = "",message="Sorry! Message is not Available"):
#
#     url = "https://www.fast2sms.com/dev/bulk"
#
#     payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno
#     headers = {
#         'authorization': "NxU4iT4ONuPxrlrupmmhmLSpp9B1C1Yey0cZkblkEnUaX4gZTFb6Ykh1oifU",
#         'Content-Type': "application/x-www-form-urlencoded",
#         'Cache-Control': "no-cache",
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#     d1 = response.text
#     json.loads(response.text)
#     return d1
# st = sendASMS()
