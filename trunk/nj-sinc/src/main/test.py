'''
Created on Feb 26, 2015

@author: huhe
'''

import re, math


def print_n_record(index, spirals, remove_list):
    print str(spirals[index]) + ', '
    remove_list.append(spirals[index])

def remove_items(spirals, remove_list):
    for i in remove_list:
        spirals.remove(i)
        

def print_outter(spirals):
    if len(spirals) == 0: return
    remove_list = []
    n = int(math.sqrt(len(spirals)))
    for i in range(n):
        # process first row
        if i == 0:
            for j in range(n):
                index = i * n + j
                print_n_record(index, spirals, remove_list)
        # process last row
        elif i == n - 1:
            for j in reversed(range(n)):
                index = i * n + j
                print_n_record(index, spirals, remove_list)
        # process rows in between
        else:
            index = i * n + n - 1
            print_n_record(index, spirals, remove_list)
    # process first column excluding first row and last row
    for i in reversed(range(1, n-1)):
        index = i * n 
        print_n_record(index, spirals, remove_list)
    
    remove_items(spirals, remove_list)
    print_outter(spirals)
    

if __name__ == '__main__':
    
    ''' A list of number. Find the number could be divided by either 3 or 5, but not both ''' 
    l = [1, 4, 3, 5, 15, 45, 10, 9]
    a = [x for x in l if (x % 3 == 0 or x % 5 == 0) and not(x % 3 == 0 and x % 5 == 0)]
    print a
    
    
    ''' In 2 lists, find the common numbers or different numbers, can't use set function '''
    a = [1, 2, 3, 4]
    b = [2, 4, 6, 8]
    c = []
    d = []
    for i in a:
        if i in b:
            c.append(i)
        else:
            d.append(i)
    for j in b:
        if j not in a and j not in d:
            d.append(j)
    print c
    print d 
    
    
    ''' Valid a x.x.x.x is a valid ip address format '''
    def validate_ip(ip):
        try:
            a=ip.split(".")
            if len(a) != 4: return False
            for i in a:
                if int(i) > 255: return False
            return True
        except:
            return False
        

    ''' print 1, 3-5, 8-9, 11, 14-15 form list a[] '''
    a = [1, 3,4,5, 8,9, 11, 14, 15]
    a_dict = {}
    pre = None
    cur_key = None
    for n in a:
        if pre is None:
            a_dict[n] = 1
            pre = n
            cur_key = n
        else:
            if n != pre + 1:
                a_dict[n] = 1
                pre = n
                cur_key = n
            else:
                a_dict[cur_key] += 1
                pre = n
    for key in sorted(a_dict.keys()):
        val = a_dict[key]
        if val == 1:
            print str(key)
        elif val == 2:
            print str(key) + "," + str(key + 1)
        else:
            print str(key) + "-" + str(key + val - 1)
            
    
    ''' print following '''
    '''
    1 2 3 4
          5
          6
      9 8 7
    '''
    
    a = [x for x in range(10)]
    a1 = a[1:5]
    a2 = a[5:6]
    a3 = a[6:7]
    a4 = reversed(a[7:])
    
    print "%d "*4 % tuple(a1)
    print "%7d" % tuple(a2)
    print "%7d" % tuple(a3)
    print " " + " %d"*3 % tuple(a4)
    
    
    ''' Read through a file, print out 3rd word of each line.  If the word doesn't exist, print null '''
    p = re.compile('\ +')
    with open('/tmp/tt') as f:
        for line in f:
            line = line.strip()
            items = p.split(line)
            if len(items) < 3:
                print 'null'
            else:
                print items[2]
        f.close()
                
    ###
    
    ''' print extract spiral array '''
    ''' 
    input list as 
    01, 02, 03 
    08, 09, 04
    07, 06, 05
    output as
    01, 02, 03, 04, 05, 06, 07, 08, 09
    '''
    lists = [1, 2, 3, 4, 12, 13, 14, 5, 11, 16, 15, 6, 10, 9, 8, 7]
    print_outter(lists)
    
    
    ''' lambda '''
    l = lambda x, y: x + y;
    n = l(1, 5)
    print str(n)
    print (lambda x, y : x**2 + y)(5, 2)
    
    
    ''' print duplicated numbers '''
    a = [1, 3, 3, 3, 5, 5, 5, 8, 9, 10, 12, 12, 12]
    b = list(set(a))
    for n in b:
        cnt = a.count(n)
        if cnt > 1:
            print str(n)*cnt
            
    
    ''' find the square root for an integer 15==>3, 45==>6 '''
    ''' method 1 '''
    num = 36
    if num > 0:
        for i in range(num):
            if i**2 > num: 
                print str(i-1)
                break
        
    ''' method 2 '''
    num = 81
    xstart = 0
    xend = num 
    while True:
        mid = (xend + xstart + 1) / 2
        if mid ** 2 > num:
            if (mid - 1) ** 2 <= num:
                print str(mid-1)
                break
            else:
                xend = mid
        elif mid ** 2 <= num:
            if (mid + 1) > num:
                print str(mid)
                break
            else:
                xstart = mid
    
        
    ''' keyword argument '''
    my_list = ['i1', 'i2', 'i3']
    def test_l(*a_list):
        for i in a_list:
            print i
    test_l(*my_list)
    test_l('i1', 'i2', 'i3')
            
    my_dict = {'frst': 'huan', 'last': 'he', 'middle': 'C'}
    def test_d(**a_dict):
        for k, v in a_dict.iteritems():
            print k, '=', v
    test_d(**my_dict)
    test_d(frst='huan', last='he', middle='C')
    
    
    ''' ["1", "2", "3"]   ["ab", "c"]--> ["1ab", "2c", "3"]  '''
    lista = ["1", "2", "3"]
    listb = ["ab", "c", "g", "f"]
    lena = len(lista)
    lenb = len(listb)
    listz = []
    listr = []
    lenz = None
    if lena > lenb:
        listz = lista[lenb:]
        lenz = lenb
    else:
        listz = listb[lena:]
        lenz = lena
    for i in range(lenz):
        listr.append(lista[i] + listb[i])
    listr = listr + listz
    print listr
    
    ''' how zip works '''
    listc = []
    for a, b in zip(lista, listb):
        listc.append(a + b)
    print listc
    
    
    ''' how many -, number, +, numerator, denumerator ''' 
    lines = ['-1+1/2', '5+6', '3/2-4']
    result = {'-':0, '+':0, 'n':0, 'num':0, 'den': 0}
    for line in lines:
        for i, c in enumerate(line):
            if c == '-':
                result['-'] += 1
            elif c == '+':
                result['+'] += 1
            elif c != '/':
                if i != len(line) - 1 and line[i+1] == '/':
                    result['num'] += 1
                elif line[i-1] == '/':
                    result['den'] += 1
                result['n'] += 1
    print result
                
                    
                    
    
    