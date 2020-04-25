import requests


# #working with png
# url = 'http://www.google.com/images/srpr/logo3w.png'
# getted_url = requests.get(url)
# f = open("google.png", "wb")
# f.write(getted_url.content)
# f.close()

url1 = "https://vk.com/video-128033123_456240317"
url2 = "https://vk.com/video?z=video-128033123_456240317%2F3594562ba7f22bbe47%2Fpl_cat_football_2018_block"
url3 = "https://youtu.be/UchTK-I9Mo4"
getted_url = requests.get(url3)
f = open("ryaba.mp4", "wb")
f.write(getted_url.content)
f.close()

