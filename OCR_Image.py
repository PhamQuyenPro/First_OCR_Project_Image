import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

### Read image with opencv
img_path = '1.png'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1, img2, img3 = img.copy(), img.copy(), img.copy()
hImg, wImg, _ = img.shape

### Detecting Characters
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
	#=======================#
	# print(b)
	# Output:
	# I 182 224 185 242 0
	# m 188 224 207 237 0
	# a 208 224 221 237 0
	# g 222 219 234 237 0
	# e 236 224 249 237 0
	#=======================#
	b = b.split(' ')
	#=======================#
	# print(b)
	# ['I', '182', '224', '185', '242', '0']
	# ['m', '188', '224', '207', '237', '0']
	# ['a', '208', '224', '221', '237', '0']
	# ['g', '222', '219', '234', '237', '0']
	# ['e', '236', '224', '249', '237', '0']
	# ['1', '41', '157', '69', '200', '0']
	#=======================#
	x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
	cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 1)
	cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

# Save image detected characters
cv2.imwrite('Detecting_Characters.png', img)
# cv2.imshow('Quyen', img)
# cv2.waitKey(0)

### Detecting Words
words = pytesseract.image_to_data(img1)
for idx, word in enumerate(words.splitlines()):
	#=======================#
	# print(word)
	# Output:
	# level   page_num        block_num       par_num line_num        word_num        left    top     width   height  conf
	#         text
	# 1       1       0       0       0       0       0       0       455     262     -1
	# 2       1       1       0       0       0       182     20      67      23      -1
	# 3       1       1       1       0       0       182     20      67      23      -1
	# 4       1       1       1       1       0       182     20      67      23      -1
	# 5       1       1       1       1       1       182     20      67      23      94.201080       Image
	# 2       1       2       0       0       0       41      59      378     46      -1
	# 3       1       2       1       0       0       41      59      378     46      -1
	# 4       1       2       1       1       0       41      59      378     46      -1
	# 5       1       2       1       1       1       41      59      378     46      96.005333       1234567890
	# 2       1       3       0       0       0       175     131     81      18      -1
	# 3       1       3       1       0       0       175     131     81      18      -1
	# 4       1       3       1       1       0       175     131     81      18      -1
	# 5       1       3       1       1       1       175     131     81      18      96.846848       Results
	# 2       1       4       0       0       0       177     188     76      10      -1
	# 3       1       4       1       0       0       177     188     76      10      -1
	# 4       1       4       1       1       0       177     188     76      10      -1
	# 5       1       4       1       1       1       177     188     76      10      90.130615       1234567890
	#=======================#
	if idx != 0:
		word = word.split()
		#=======================#
		# print(word)
		# Output
		# ['1', '1', '0', '0', '0', '0', '0', '0', '455', '262', '-1']
		# ['2', '1', '1', '0', '0', '0', '182', '20', '67', '23', '-1']
		# ['3', '1', '1', '1', '0', '0', '182', '20', '67', '23', '-1']
		# ['4', '1', '1', '1', '1', '0', '182', '20', '67', '23', '-1']
		# ['5', '1', '1', '1', '1', '1', '182', '20', '67', '23', '94.201080', 'Image']
		# ['2', '1', '2', '0', '0', '0', '41', '59', '378', '46', '-1']
		# ['3', '1', '2', '1', '0', '0', '41', '59', '378', '46', '-1']
		# ['4', '1', '2', '1', '1', '0', '41', '59', '378', '46', '-1']
		# ['5', '1', '2', '1', '1', '1', '41', '59', '378', '46', '96.005333', '1234567890']
		# ['2', '1', '3', '0', '0', '0', '175', '131', '81', '18', '-1']
		# ['3', '1', '3', '1', '0', '0', '175', '131', '81', '18', '-1']
		# ['4', '1', '3', '1', '1', '0', '175', '131', '81', '18', '-1']
		# ['5', '1', '3', '1', '1', '1', '175', '131', '81', '18', '96.846848', 'Results']
		# ['2', '1', '4', '0', '0', '0', '177', '188', '76', '10', '-1']
		# ['3', '1', '4', '1', '0', '0', '177', '188', '76', '10', '-1']
		# ['4', '1', '4', '1', '1', '0', '177', '188', '76', '10', '-1']
		# ['5', '1', '4', '1', '1', '1', '177', '188', '76', '10', '90.130615', '1234567890']
		#=======================#
		if len(word) == 12:
			x, y, w, h = int(word[6]), int(word[7]), int(word[8]), int(word[9])
			cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 1)
			cv2.putText(img1, word[11], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

# Save image detected words
cv2.imwrite('Detecting_Words.png', img1)
# cv2.imshow('Quyen', img1)
# cv2.waitKey(0)

### Detecting Characters Only Digits
conf = r'--oem 3 --psm 6 outputbase digits'
char_digits = pytesseract.image_to_boxes(img2, config=conf)
# print(char_digits)
# print(type(char_digits))
for b in char_digits.splitlines():
	b = b.split(' ')
	x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
	cv2.rectangle(img2, (x, hImg-y), (w, hImg-h), (255, 0, 0), 1)
	cv2.putText(img2, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

# Save image detected characters only digits
cv2.imwrite('Detecting_Characters_Only_Digits.png', img2)
# cv2.imshow('Quyen', img2)
# cv2.waitKey(0)

### Detecting Words Only digits
conf = r'--oem 3 --psm 6 outputbase digits'
digits_words = pytesseract.image_to_data(img3, config=conf)
for idx, word in enumerate(digits_words.splitlines()):
	if idx != 0:
		word = word.split()
		if len(word) == 12:
			x, y, w, h = int(word[6]), int(word[7]), int(word[8]), int(word[9])
			cv2.rectangle(img3, (x, y), (x+w, y+h), (0, 255, 0), 1)
			cv2.putText(img3, word[11], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

# Save image detected words only digits
cv2.imwrite('Detecting_Words_Only_Digits.png', img3)
# cv2.imshow('Quyen', img3)
# cv2.waitKey(0)
