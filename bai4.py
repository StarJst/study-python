# -*- coding: utf-8 -*-
"""
Spyder Editor
created 11/6/2025
học bài 4
This is a temporary script file.
khi save bài thì phải có đuôi .py
"""
#các loại print

# print ko có gì
# khi print thì ở đằng sau ko cần ":"
# sử dụng dấu "" hay '' gì cũng được
print()

# print so/ 1 cái lẻ
# print này nó hình như thiếu "" nên không cho chữ
print(32)

#print chuỗi
#print này thì ok có cho đánh chữ 
print("gojo satoru")

"""
dấu ; có chức năng cho phép print nhiều cái cùng
 1 dòng mà không cần phải xuống dòng
"""
print(23);print("gojo satoru")

#có câu lệnh print objects trong cùng 1 print
print("xin chào", "halleluyah", "Jesus is king of the kings", 123424)

"""
khi tách object thì không được sài dấu khác ngoài ","
nhưng dấu , nó chỉ tách là 1 khoảng trắng thôi
nếu muốn cái tách mà không có khoảng cách and được thay bằng ký tự khác thì
sep="," hoặc bên trong "" thì thay cái gì cũng được
"""
print("xin chào", "ô mai ka", 23323, "sos", sep=",")

"""
trường hợp khác khi áp dụng end='' thì khi run nó sẽ cho gắn luôn print ở
dưới vào luôn với print ở trên
"""
#TH mà không có end=''
print("ai là Zeta của gojo nào?")
print("Linh liitch am reen")

#TH mà có end=''
print("ai là Zeta của gojo nào?", end=':')
print("Linh liitch am reen")

"""
ngoài lề if muốn xử lý theo kiểu chuỗi 
muốn điền dữ liệu vào thì thay () => {} 
muốn chữ nào nhảy vô {} thì sau đó .format()
"""
# ví dụ về cái format
print('ai là người gojo simp?={}'.format('linh'))

#ví dụ về muốn nó tự điền thông tin theo 1 trật tự
print('gojo satoru thích={0}, Linh thích={1}'.format('linh', 'satoru'))
# ngoài ra bên trong {} không cần phải điền số

#test 
print('Catoru iu={0}, Liinh iu={1}'.format('hlinh', 'catoru', 'both'))
# hình như tên không được trùng nhau giống object trc, format cũng phải khác 
# hình như cái {} phải bắt đầu từ 0,1,2 theo thứ tự chứ ko cho nhảy lung tung

