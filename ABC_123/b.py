order_time = [int(input()) for _ in range(5)]
wait_time = [10-i%10 for i in order_time if i%10!=0 ]
wait_time = sorted(wait_time)[:-1]
result = sum(order_time)
result += sum(wait_time)
print(result)
