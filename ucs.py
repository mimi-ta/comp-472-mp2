from node import Node
from collections import deque
def UCS():
    closed = []
    open = deque()
    open.append("slay")
    open.append("queen")
    open.popleft()
    print(open)

ucd = UCS()
