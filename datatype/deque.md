# deque

파이썬에서 큐(queue)는 First-In-First-Out(FIFO) 의 방식으로 작동된다. deque는 큐이지만 양방향인 큐이다. 즉 앞, 뒤 양쪽 방향에서 요소를 추가하거나 삭제할 수 있다.

<br>

## deque 사용법

```python
from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()
```

<br>

## deque 메소드

```python
# append(x): 큐의 뒤로 삽입
from collections import deque

queue= deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']


# appendleft(x): 큐의 앞으로 삽입
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']

queue.appendleft('a')
# queue = ['a', 'b', 'c']


# clear: 큐의 모든 요소를 삭제함
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']

queue.appendleft('a')
# queue = ['a', 'b', 'c']

queue.clear()
# queue = []


# copy: 얕은 복사
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

copied_queue = queue.copy()
# copied_queue = ['b']


# count(x): 큐에서 x와 같은 값의 개수
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('a')
# queue = ['b', 'a']

queue.appendleft('a')
# queue = ['a', 'b', 'a']

print(queue.count('a')
# 2


# extend(iterable): iterable한 값을 파라미터로 넣으면 해당 값들이 하나씩 큐의 오른쪽에 붙음
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.extend('lft')
# queue = ['b', 'l', 'f', 't']

queue.append('lft')
# queue = ['b', 'l', 'f', 't', 'lft']


# extendleft(iterable): iterable한 값을 파라미터로 넣으면 해당 값들이 하나씩 큐의 왼쪽에 붙음
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.extendleft('lft')
# queue = ['t', 'f', 'l', 'b']

queue.appendleft('lft')
# queue = ['lft', 't', 'f', 'l', 'b']


# index(x[, start[, stop]]): 큐(인덱스 시작 후 및 인덱스 중지 전)에서 x의 위치를 반환. 첫 번째 일치를 반환하거나 찾을 수 없는 경우 ValueError 발생.
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.extendleft('kny')
# queue = ['y', 'n', 'k', 'b']

# index(x)
print(queue.index('b'))
# 4

# index(x, start: int)
print(queue.index('b', 1))
# 4

# index(x, start: int, stop: int)
print(queue.index('b', 0, 1))
# ValueError: 'b' is not in deque


# insert(i, x): i 위치에 x를 삽입
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']

queue.insert(0, 'a')
# queue = ['a', 'b', 'c']

# queue.maxlen()을 넘어선 위치에 insert를 하고자 하면, IndexError가 발생한다.


# pop(): 큐의 맨 오른쪽의 element를 삭제하고 반환. element가 없으면, IndexError가 발생.
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']

popped = queue.pop()
# popped = 'c'


# popleft(): 큐의 맨 왼쪽의 element를 삭제하고 반환. element가 없으면, IndexError가 발생.
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']

popped_left = queue.popleft()
# popped_left = 'b'


# remove(value): 큐에 있는 value 값 중 처음으로 등장한 value를 삭제. 못 찾으면, ValueError가 발생
from collections import deque

queue = deque()
queue.append('b')
# queue = ['b']

queue.append('c')
# queue = ['b', 'c']

queue.append('b')
# queue = ['b', 'c', 'b']

queue.remove('b')
# queue = ['c', 'b']


# reverse(): 큐를 제자리에서 반대로 뒤집는다. 반환값은 없음.
from collections import deque

queue = deque()
queue.append('c')
# queue = ['c']

queue.append('b')
# queue = ['c', 'b']

queue.append('a')
# queue = ['c', 'b', 'a']

queue.reverse()
# queue = ['a', 'b', 'c']


# rotate(n=1): n만큼 오른쪽으로 회전. n이 음수면, 왼쪽으로 회전, 반환값은 없음. 큐(q)가 비어있지 않다면, q.rotate(1)을 하는 것은 q.appendleft(q.pop())과 같음.
또한, q,rotate(-1)을 하는 것은 q.append(q.popleft())과 같음.
from collections import deque

queue = deque()
queue.append('c')
# queue = ['c']

queue.append('b')
# queue = ['c', 'b']

queue.append('a')
# queue = ['c', 'b', 'a']

queue.rotate(1)
# queue = ['a', 'c', 'b']

queue.rotate(-1)
# queue = ['c', 'b', 'a']


# maxlen: 큐 생성 시, 정했던 큐의 최대 크기, 정하지 않았으면 None 반환
# 최대 크기를 정했을 시
from collections import deque

# class collections.deque([iterable[, maxlen]])
# deque(iterable, maxlen: int)
queue = deque('fnd', 3)
print(queue)
# deque(['f', 'n', 'd'], maxlen=3)

queue.append('b')
print(queue)
# deque(['n', 'd', 'b'], maxlen=3)

queue.append('c')
print(queue)
# deque(['d', 'b', 'c'], maxlen=3)

queue.appendleft('a')
print(queue)
# deque(['a', 'd', 'b'], maxlen=3)

print(queue.maxlen)
# 3
# 최대 크기를 정하지 않았을 때
from collections import deque

# class collections.deque([iterable[, maxlen]])
# deque(iterable)
queue = deque('fnd')
print(queue)
# deque(['f', 'n', 'd'])

queue.append('b')
print(queue)
# deque(['f', 'n', 'd', 'b'])

queue.append('c')
print(queue)
# deque(['f', 'n', 'd', 'b', 'c'])

queue.appendleft('a')
print(queue)
# deque(['a', 'f', 'n', 'd', 'b', 'c'])

print(queue.maxlen)
# None
```

<br>

## deque의 장점
리스트의 pop(0)은 O(n)인데 반해, 데크의 popleft()는 O(1)이기 때문이며, 각각 n번씩 반복하면 리스트 구현은 O(n2), 데크 구현은 O(n)으로 성능 차이가 크다. 최적화된 내부 기능을 잘 활용해 성능을 좀 더 높일 수 있다.

<br>

## deque의 활용
deque는 스택처럼 활용할 수도 있고 큐처럼 사용할 수도 있다. 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공한다. 즉, 대부분의 경우에 deque 리스트(list)보다 월등한 옵션이다.
