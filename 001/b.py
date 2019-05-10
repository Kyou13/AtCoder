m = int(input())
km = m/1000

if km < 0.1:
  print('00')
elif km >= 0.1 and km <= 5:
  print("{:02.0f}".format(km*10))
elif km >= 6 and km <= 30:
  print("{:02.0f}".format(km+50))
elif km >= 35 and km <= 70:
  print("{:02.0f}".format((km-30)/5+80))
elif km > 70:
  print("89")
