import cv2
import os

# パス
import_path = '/path/to/dir/pokequiz/images'
export_path = '/path/to/dir//pokequiz/gray'

# ディレクトリ読み込み
for filename in os.listdir(import_path):
	# 画像ファイル取得
	if os.path.isfile(os.path.join(import_path, filename)):

		# 画像ファイルをグレースケールで読み込み
		image_path = 'images/' + filename
		img = cv2.imread(image_path, 0)

		# 平坦化
		gray = cv2.GaussianBlur(img,(11,11),0)

		# 二値化
		ret, img_thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

		# 二値化した画像の保存
		filename = filename.replace('.png','_gray.png')
		image_export_path = 'gray/' + filename
		cv2.imwrite(image_export_path,img_thresh)