# Viết một chương trình chuyển giá trị nhập vào từ thập phân sang nhị phân
out = ''
n = int(input("Nhập vào giá trị bạn muốn chuyển sang nhị phân: "))
p = n
while n> 0 :
    out = out + str(n%2)
    print('{0}/2 = {1} dư {2}'.format(n,int(n/2),n%2))
    n = int(n/2)
else:
    print('Kết quả chuyển từ {} sàng nhị phân là {} '.format(p,out[::-1]))
    print('Kiểm tra Kết quả chuyển từ {} sàng nhị phân là {} '.format(p,bin(p)))
# n = 5%2
# m = int(5/2)
# print(n)
# print(m)