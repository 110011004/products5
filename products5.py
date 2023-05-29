import os
#讀取檔案
products = []
if os.path.isfile('products.csv')：#檢查檔案在不再
	print ('yeah!')
	with open ('products.csv', 'r', encoding-'utf-8') as f:
		for line in f:
			if '商品，價格'in line:
				continue
			name, price = line.strip() .split(',')
			products. append( [name, price])
		print (products)
	else:
		print('找不到檔案'）
#使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q' :
		break
	price = input('請輸入商品價格：')
	price = int (price)
	products. append( [name, price]) 
print (products)




