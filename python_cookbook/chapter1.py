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
if __name__ == '__main__':
    with open('SOURCES1.txt') as f:
        for line, prevlines in search(f, 'forms',5):
            for pline in prevlines:
                print("pline",pline, end='')
            print("line",line, end='')
            print('-'*20)
        print("hello worlddsf")
        print("hello world")
        


# %%



# %%



