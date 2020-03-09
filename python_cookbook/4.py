#%%
## 4.1 手动遍历迭代器
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
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
# %%
#note:实现深度优先方式遍历树形借点的生成器
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(Node(4))
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(5))
    child2.add_child(Node(6))
    for ch in root.depth_first():
        print(ch)
#%%
## 4.10 序列上索引值迭代
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list,2):
    print(idx, val)

# %%
#note: 4.11 同时迭代多个序列
xpts = [1, 5, 3, 2, 3, 3,6,33]
ypts = [101, 23, 55, 99, 33, 92,2,2,2,2,2]
zpts = [323, 34,4434, 55,3434, 34]
for i in zip(xpts, ypts,zpts):
    print(i)
# %%
## 4.12 不同集合上元素的迭代
## 4.14 展开嵌套的序列
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, 5,6], [5, 9]]
for x in flatten(items):
    print(x)


# %%
