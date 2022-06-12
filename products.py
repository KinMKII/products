import os

products = []
# 讀取檔案
if os.path.isfile('products.csv'): # 檢查檔案
    print('已找到檔案')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
        name, price = line.strip().split(',')
        products.append([name, price])
else:
    print('檔案不存在')

# 讓使用者輸入
while True:
    name = input('請輸入商物名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])

# 印出所有商品
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')