from decimal import Decimal, ROUND_HALF_UP
deg, dis = map(int, input().split())

dir_list = [('N',0)]
dir_count = 11.25
dir_list_key = ['NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
for i in dir_list_key:
  dir_list.append((i,dir_count))
  dir_count += 22.5

kaze = [0.0, 0.3, 1.6, 3.4, 5.5, 8.0, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]

deg = deg/10
dis = dis/60
dis = float(Decimal(str(dis)).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
dir_ = ''
W = 0
for i in dir_list:
  if deg >= i[1]:
    dir_ = i[0]
for index, k in enumerate(kaze):
  if dis >= k:
    W = index
if W == 0:
  dir_ = 'C'
print(dir_, W)
