import random
import os
import json
import cv2

# 1~151の間でランダムに選ぶ
rand = random.randint(1,151)

# name.jsonの読み込み
f = open('name.json', 'r')
jsn = json.load(f)


# 出題する画像の読み込み
os.chdir('/path/to/dir/pokequiz/gray/')
image_file = jsn[str(rand)]["image"]
img = cv2.imread(image_file)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.waitKey(0)


answer = input("だーれだ？ >> ")
if answer == jsn[str(rand)]["name"]:
	print("正解")
else:
	print("残念  正解->" + jsn[str(rand)]["name"])

cv2.destroyAllWindows()
