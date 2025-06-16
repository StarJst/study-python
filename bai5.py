# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 22:22:10 2025
bài 5
@author: meowm
"""
# input là lệnh để đưa dữ liệu vào, còn print là in ra
input('nhập vào 1 con số:')

"""
#nhập 1 biến vô a(bài sau mới học kỹ)
print('nhập số :')
b={0}.format('b')
#erm.. cái trên hình như sai

đầu tiên hình như phải gắn a với input mới nhập được vô dữ liệu rồi sau đó
mới .format để print nó ra được.. lmao

c = input('nhập 1 số bất kỳ:')
#sau khi có chỗ nhận dữ liệu thì mới bắt đầu cho chỗ in
print('c={0}'.format(c))

#ê cái ở trên bị thiếu đầu vô nên mới bị lỗi, nó mới có bộ xử lý với ra thôi
#phải input trước rồi sau đó mới cho a=input để nhận đầu xử lý 
"""

input('nhập số : ')
#input này chỉ là 1 biến để nhập vô thôi

a = input('nhập là: ')
print('a={}'.format('a'))
#wtf??? không hiểu luôn vì sao nó ko ra cái đã nhập mà ra a=a????
#à rồi.. vì format('a') nên máy gộp a=a, phải ghi a thôi

#ví dụ lại
a = input('nhập số là: ')
print('a={}'.format(a))
#ok đã hiểu


ho = input("nhập họ: ")
ten = input("nhập tên: ")
print("xin chào!", ho , ten)
#khi gắn biến ho, tên thì trước đó phải có , để ngăn cách tên với lệnh

