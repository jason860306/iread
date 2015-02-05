#!/usr/bin/env python
#encoding: utf-8

__author__='szj0306'

import csv
import sys
import os
import string
from collections import Counter
reload(sys)
sys.setdefaultencoding("utf-8")

show_log=False

phone_nums=[]
book_names=[]
authers=[]
book_types=[]
read_times=[]
provinces=[]
citys=[]
pays=[]
phone_books=set()
book_rdnums={}
book_ispays=set()

def iread_parser(fname):
    with open(fname, 'rb') as ireadfile:
        ireader = csv.reader(ireadfile, delimiter='|', \
            skipinitialspace=True)
        for row in ireader:
            if show_log:
                print ','.join(row)
            if row[0] not in phone_nums:
                phone_nums.append(row[0])
            if row[1] not in book_names:
                book_names.append(unicode(row[1], "utf-8"))
            if row[2] not in authers:
                authers.append(unicode(row[2], "utf-8"))
            if row[3] not in book_types:
                book_types.append(unicode(row[3], "utf-8"))
            if row[4] not in read_times:
                read_times.append(row[4])
            if row[5] not in provinces:
                provinces.append(unicode(row[5], "utf-8"))
            if row[6] not in citys:
                citys.append(unicode(row[6], "utf-8"))
            pay='charge' if string.atoi(row[7]) else 'free'
            if pay not in pays:
                pays.append(pay)

            phone_book=tuple((phone_nums.index(row[0]), \
                book_names.index(row[1])))
            if phone_book not in phone_books:
                phone_books.add(phone_book)
                book_rdnums[book_names.index(row[1])] = 1
            else:
                book_rdnums[book_names.index(row[1])] += 1

            book_ispay=tuple((book_names.index(row[1]), pay))
            if book_ispay not in book_ispays:
                book_ispays.add(book_ispay)

def write_phone_num():
    with open('phone_num', 'wb') as phone_file:
        phone_file.write('\xEF\xBB\xBF');
        phone_writer = csv.writer(phone_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nphone number as follow: '
        for phone_num in phone_nums:
            phone_writer.writerow([phone_nums.index(phone_num), \
                phone_num])
            if show_log:
                print '#%d. %s' % (phone_nums.index(phone_num), \
                    phone_num)

def write_book_name():
    with open('book_name', 'wb') as book_file:
        book_file.write('\xEF\xBB\xBF');
        book_writer = csv.writer(book_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nbook name as follow: '
        for book_name in book_names:
            book_writer.writerow([book_names.index(book_name), \
                book_name])
            if show_log:
                print '#%d. %s' % (book_names.index(book_name), \
                    book_name)

def write_auther():
    with open('auther', 'wb') as auther_file:
        auther_file.write('\xEF\xBB\xBF');
        auther_writer = csv.writer(auther_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nauther as follow: '
        for auther in authers:
            auther_writer.writerow([authers.index(auther), auther])
            if show_log:
                print '#%d. %s' % (authers.index(auther), auther)

def write_book_type():
    with open('book_type', 'wb') as type_file:
        type_file.write('\xEF\xBB\xBF');
        type_writer = csv.writer(type_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nbook type as follow: '
        for book_type in book_types:
            type_writer.writerow([book_types.index(book_type), \
                book_type])
            if show_log:
                print '#%d. %s' % (book_types.index(book_type), \
                    book_type)

def write_read_time():
    with open('read_time', 'wb') as rdtime_file:
        rdtime_file.write('\xEF\xBB\xBF');
        rdtime_writer = csv.writer(rdtime_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nread time as follow: '
        for read_time in read_times:
            rdtime_writer.writerow([read_times.index(read_time), \
                read_time])
            if show_log:
                print '#%d. %s' % (read_times.index(read_time), \
                read_time)

def write_province():
    with open('province', 'wb') as province_file:
        province_file.write('\xEF\xBB\xBF');
        province_writer=csv.writer(province_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nprovince as follow: '
        for province in provinces:
            province_writer.writerow([provinces.index(province), \
                province])
            if show_log:
                print '#%d. %s' % (provinces.index(province), \
                    province)

def write_city():
    with open('city', 'wb') as city_file:
        city_file.write('\xEF\xBB\xBF');
        city_writer=csv.writer(city_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\ncity as follow: '
        for city in citys:
            city_writer.writerow([citys.index(city), city])
            if show_log:
                print '#%d. %s' % (citys.index(city), city)

def write_pay():
    with open('pay', 'wb') as pay_file:
        pay_file.write('\xEF\xBB\xBF');
        pay_writer=csv.writer(pay_file, delimiter = ',', \
            quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\npay as follow: '
        for pay in pays:
            pay_writer.writerow([pays.index(pay), pay])
            if show_log:
                print '#%d. %s' % (pays.index(pay), pay)

def write_phone_book():
    with open('phone_book', 'wb') as phone_book_file:
        phone_book_file.write('\xEF\xBB\xBF');
        phone_book_writer=csv.writer(phone_book_file, \
            delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nphone - book as follow: '
        for phone_book in phone_books:
            phone_book_writer.writerow([phone_book[0], \
                phone_book[1]])
            if show_log:
                print '#%d.%s - #%d.%s' % \
                    (phone_book[0], phone_nums[phone_book[0]], \
                    phone_book[1], book_names[phone_book[1]])

def write_book_rdnum():
    with open('book_rdnum', 'wb') as book_rdnum_file:
        book_rdnum_file.write('\xEF\xBB\xBF');
        book_rdnum_writer=csv.writer(book_rdnum_file, \
            delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nbook - rdnum as follow: '
        for key in book_rdnums:
            book_rdnum_writer.writerow([key, book_rdnums.get(key)])
            if show_log:
                print '#%d.%s -> %d times' % (key, book_names[key], \
                    book_rdnums.get(key))

def write_book_ispay():
    with open('book_ispay', 'wb') as book_ispay_file:
        book_ispay_file.write('\xEF\xBB\xBF');
        book_ispay_writer=csv.writer(book_ispay_file, \
            delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        if show_log:
            print '\nbook - ispay as follow: '
        for book_ispay in book_ispays:
            book_ispay_writer.writerow([book_ispay[0], \
                book_ispay[1]])
            if show_log:
                print '#%d.%s - %s' % (book_ispay[0], \
                    book_names[book_ispay[0]], book_ispay[1])

def iread_write():
    write_phone_num()
    write_book_name()
    write_auther()
    write_book_type()
    write_read_time()
    write_province()
    write_city()
    write_pay()
    write_phone_book()
    write_book_rdnum()
    write_book_ispay()

if __name__ == '__main__':
    if len(sys.argv) <> 2:
        print "usage: %s fname" % sys.argv[0]
        sys.exit(-1)
    iread_parser(sys.argv[1])
    iread_write()
