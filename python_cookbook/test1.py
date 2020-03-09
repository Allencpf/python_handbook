#!/usr/local/bin/python3.7
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## 1.1 解压序列赋值给多个变量
# 问题
# 
# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值 给 N 个变量？
# 
# 解决方案
# 
# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多 个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

# %%
data = ['asdf', 32, 88.3, (2012, 12, 21)]
_, share, _, (year, month, day) = data


# %%
day

# %% [markdown]
# ## 1.2 解压可迭代对象赋值给多个变量
# **？** 如果一个可迭代对象的元素超过变量个数时， 会抛出一个valueerror。 那么怎么样才能从这个可迭代对象中解压出N个元素出来？
# **-** Python 的 星号表达式可以来解决。比如，你在学一门课程，在学期末的时候你想统计一下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。 如果一共四个可以手动排除，但如果有24个呢？ then * works
# 

# %%
def drop_first_last(grades):
    first, *middle, last = grades
    #first, **middle, lsat = grade
    return middle

midlle= drop_first_last({'toe':11,'sdf': 22,'FD': 33, 'dsf':44,'dsf': 55})


# %%
midlle

# %% [markdown]
# * work in 迭代元素为可变长元祖的序列时，下面是一个带有标签的元祖序列

# %%
records = [
    ('foo', 1, 2,2, 3, 4),
    ('bar', 'hello', 's', 'sdf',('dfs',1)),
    ('foo', 6, 6),
]

def def_foo(*x):
    print('foo',*x)
def def_bar(*s):
    print('bar',*s)
    
for tag, *tags in records:
    if tag == 'foo':
        def_foo(*tags)
    elif tag == 'bar':
        def_bar(*tags)


# %%
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false:sdfdf/'

uname, *fields, homedir,ssh,  sh = line.split('/')


# %%
homedir


# %%
record = (('ACME',2,33,'sdf'), 50, 123.45,'sdf',1, 'sdf',2,(12, 18,23,'dsf', 2012))
(name,*_), *_, (*_, year) =record


# %%
year

# %% [markdown]
# use * 可以很快将一个列表分成前后俩个部分

# %%
items = [1, 10, 7, 4,5,9]
head, *tail = items


# %%
tail

# %% [markdown]
# 采用这种分割语法实现递归算法
import sys
sys.setrecursionlimit(1000000)
def sum(tiems):
    head, *tail = items
    return head + sum(tail) if tail else head
sum(items)# %% [markdown]
# ## 1.3 保留最后N个元素
# 问题
# 
# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
# 
# 解决方案
# 
# 保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码 在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行：

# %%
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
## Example use on a file
#tag:__name__ == '__main__'
if __name__ == '__main__':
    with open('SOURCES1.txt') as f:
        for line, prevlines in search(f, 'forms',5):
            for pline in prevlines:
                print("pline",pline, end='')
            print("line",line, end='')
            print('-'*20)
        print("hello world")
        print(len(pline))


# %%
import heapq
nums = [1, 2, 4, 1e10, 1e-10, 23, 323,434,55]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


# %%
portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
cheap = heapq.nsmallest(3, portfolio, key = lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s: s['price'])


# %%
cheap

# %% [markdown]
# cheap; expesive
# %% [markdown]
# ## 1.5 实现一个优先级队列
# by use heapq

# %%
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# %%
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item{!r}'.format(self.name)


# %%
Item('foo')


# %%
q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('gsd'),4)
q.push(Item('grok'),1)


# %%
q.pop()

# %% [markdown]
# ## 1.6 字典中的键映射多个值

# %%
from collections import defaultdict
def constant_dactory(value):
    return lambda: value
d = defaultdict(constant_dactory('<missing>'))
print('\n',d)
d.update(name='john', action='ran')
print('\n', d)
print('\n', '{0[name]} {0[action]} to {0[object]}'.format(d))


# %%
from  collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(2)
d['b'].append(3)
m = defaultdict(set)
m['a'].add(10)
m['a'].add(10)
m['a'].add(5)
m['b'].add(3)

# %% [markdown]
# ## 1.7 字典顺序

# %%
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
print(d)

# %%
import json
json.dumps(d) 
type(json.dumps(d))
# %%
## 1.8 字典的运算
prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price,'\n',max_price)
prices_sorted = sorted((zip(prices.values(), prices.keys())))
print(prices_sorted)

# %%
#note: 这个zip 是一个只能访问一次的迭代器 
prices_and_names = zip(prices.values(),prices.keys()) 
print(min(prices_and_names))
#print(max(prices_and_names)) # 所以这个就会报错
min(prices)
max(prices)
min(prices.values())
min(prices, key=lambda k:prices[k]) #note:
min_value = prices[min(prices,key=lambda k:prices[k])]
print(min_value)
# %%
# 1.9 查找俩字典的相同点
a = { 'x' : 1, 'y' : 2, 'z' : 11 , "m":5} 
b = { 'w' : 10, 'x' : 11, 'y' : 2 , 'm':5}
# Find keys in common
a.keys() & b.keys()
# Find keys in a that are not in b
a.keys() - b.keys()
# Find (key, value) pairs in common
a.items() & b.items()

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z','w'}}
c
# %%
## 1.10 删除序列相同元素并保持顺序
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

# %%
def dedupe_dic(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
#if __name__ == '__main__':
a =[{'x':1, 'y':2}, {'x':1,'y':3}, {'x':1,'y':2}, {'x':2,'y':4}]
list(dedupe_dic(a, key=lambda d:(d['x'],d['y'])))

list(dedupe_dic(a, key=lambda d: d['y']))


# %%
record = '....................100 .......513.25 ..........'
shares = slice(20, 23)
price = slice(31, 37)
print('{}'.format(int(record[shares])* float(record[price])))
#%%
# 1.12 序列中出现次数最多的元素
words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]
from collections import Counter
word_counts = Counter(words)
print(word_counts)
top_four = word_counts.most_common(4)
print(top_four)
print(word_counts['eyes'])
#%%
# 1.13 通过某个关键字排序一个字典列表
rows = [ {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname,'\n','-'*8)
rows_by_lfname = min(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
#%%
# 1.14 排序不支持原生比较的对象
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
def sort_notcompare():
    users = [User(23),User(3),User(99)]
    print(users)
    #note:key = lambda x
    print(sorted(users, key = lambda x: x.user_id))
    #note:法2： key = attrgetter()
    from operator import attrgetter
    print(sorted(users, key = attrgetter('user_id')))

sort_notcompare()
#%%
rows = [ {'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'}, {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'}, {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'}, {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('',i)

#%%
a = [1, 2, 3]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
get_1 = itemgetter(1)
get_1(a)
get_1(b)
get_21 = itemgetter(2, 1)
get_21(a)
get_21(b)

b_21 = [get_21(temp) for temp in b]
b_21
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
#%%
## 1.16 过滤列元素
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n+1 if n>0 else n-1 for n in mylist]
[n for n in mylist if n > 0]
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        int(val)
        return False
    except ValueError:
        return True
ivals = list(filter(is_int, values))
print(ivals)
#%%
addresses = [ '5412 N CLARK', '5148 N CLARK', '5800 E 58TH', '2122 N CLARK', '5645 N RAVENSWOOD', '1060 W ADDISON', '4801 N BROADWAY', '1039 W GRANVILLE', ] 
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 =[n <= 5 for n in counts]
list(compress(addresses, more5))
#%%
## 1.17 从字典中提取子集
prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
p1 = {key:value for key, value in prices.items() if value>200}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
p3 = dict((key, value) for key, value in prices.items() if key in tech_names)
p3
#%%
from datetime import datetime
datetime.today()

#%%
# %% [markdown]
# # 第四章： 迭代器与生成器
# ## 4.1 手动遍历迭代器
# 问题： 你想遍历一个可迭代对象中的所有元素，但是不想使用for循环
# 方案： 使用next（）函数并在代码中捕获StopIteration异常。

# %%
def manual_iter():
    with open('SOURCES1.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass 


# %%
with open('SOURCES1.txt') as f:
    while True:
        line = next(f)
        if line is None:
            break
        print(line, end='')

# %% [markdown]
# ## 4.2 代理迭代
# 问题： 你构建了一个自定义容器对象，里面包含有列表，元祖或其他可迭代对象。你想直接在你的这个新容器上执行迭代操作
# 方法： 实际上你只需要一个__iter__() 方法， 将迭代操作代理到容器内部的对象上

# %%
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_children(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)


# %%
# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    # Out puts Node(1) , Node(2)
    for ch in root:
        print(ch)

# %% [markdown]
# ## 4.3 使用生成器创建新的迭代模式

# %%
list(range(1,100,5))


# %%
def frange(start, stop, increment):
    x = start 
    while x < stop :
        yield x
        x += increment


# %%
for n in frange(0,4,0.5):
    print(n)


# %%
list(frange(1,100,5))


# %%
def countdown(n):
    print("Starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    else :
        print("Done")


# %%
c = countdown(5)


# %%
next(c)

# %% [markdown]
# ## 4.4 实现迭代器协议

# %%
class Node:
    def __init__(self, value):
        self._value = value 
        self._children = []
    def __repr__(self):
        return 'Noed({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# %%
## example 
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(8))
    child1.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    
    for ch in root.depth_first():
        print(ch)


# %%
class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._vlaue)
    def add_childe(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):
    """
    Depth-first traversal
    """
    def __init__(self, start_node):
        self._node = start_node
        self._childrent_iter = None
        self._child_iter = None
    def __iter__(self):
        return self
    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._child_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._childrent_iter).depth_first()
            return next(self)
## example 
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(8))
    child1.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    
    for ch in root.depth_first():
        print(ch)


# %%
class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start :
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
#for rr in Countdown(30):
   # print(rr)
        


# %%



# %%



# %%



