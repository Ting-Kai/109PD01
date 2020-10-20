# -*- coding: utf-8 -*-
name = input()
birthday = input()
name_list = name.split(' ')
birthday_list = birthday.split('/')
print('{0} is born at year {1} month {2} day {3} in {4} family.'.format(name_list[0],birthday_list[0],birthday_list[1],birthday_list[2],name_list[1]))

