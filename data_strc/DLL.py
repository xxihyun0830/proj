
class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
        def __str__(self):
            return f"NODE[{self.value}]"

    def __init__(self):
        # head노드를 만들고, prev, next포인터가 자신을 가르키도록 설정
        self.head = self.Node(None)
        self.head.prev = self.head
        self.head.next = self.head

    def is_empty(self):
        # 리스트가 비어있으면 True, 아니면 False
        if self.head.next == self.head:
            return True
        else :
            return False 


    def add_after(self, node, value):
        # node의 다음에 value 추가
        # 1. 새로운 노드를 만들고
        # 2. 새로운 노드의 prev와 next를 설정하고
        # 3. 이전 노드와 다음 노드가 각각 새 노드를 가르키도록
        n =  self.Node(value) 
        n.prev = node
        n.next = node.next
        node.next.prev = n
        node.next = n


    def add_before(self, node, value):
        # node의 다음에 value 추가
        # 1. 새로운 노드를 만들고
        # 2. 새로운 노드의 prev와 next를 설정하고
        # 3. 이전 노드와 다음 노드가 각각 새 노드를 가르키도록
        n = self.Node(value)
        n.prev = node.prev
        n.next = node
        node.prev.next = n
        node.prev = n

    def add_head(self, value):
        # add_after를 이용하면 쉽게 만들 수 있음
        self.add_after(self.head, value)

    def add_tail(self, value):
        # add_before를 이용하면 쉽게 만들 수 있음
        self.add_before(self.head, value)  ##근데 이거 자체가 circular linked list아닌가,,??

    def remove(self, node):
        # 현재 노드 대신 이 노드의 이전 노드와 다음 노드의 포인터를 서로 연결해줌
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_head(self):
        # remove를 이용하면 쉽게 만들 수 있음
        # 단 현재 리스트가 비어있는 상태인지 확인 필요
        if self.is_empty(): 
            return None
        else : 
            self.remove(self.head.next)


    def remove_tail(self):
        # remove를 이용하면 쉽게 만들 수 있음
        # 단 현재 리스트가 비어있는 상태인지 확인 필요
        if self.is_empty(): 
            return None
        else : 
            self.remove(self.head.prev)


    def traverse(self, dir = 1):
        # generator를 이용하여 리스트를 정방향(dir=1) 혹은 역방향(dir=-1)으로 순회할 수 있도록 함
        node = self.head.next if dir == 1 else self.head.prev
        while node != self.head:
            yield node
            node = node.next if dir == 1 else node.prev


    def find(self, value, from_node = None):
        # from_node 다음부터 시작해서 value 값을 갖는 첫 노드를 찾아서 반환
        # 끝까지 찾아도 없으면 None을 반환
        if from_node == None:
            from_node = self.head
        node = from_node.next
        while node != self.head:
            if node.value == value:
                return node
            node = node.next
        return None

    def print(self, dir = 1):
        # traverse를 이용하여 리스트를 프린트
        print("FORWARD: " if dir==1 else "BACKWARD:", end = "")
        for node in self.traverse(dir):
            print(node.value, end="->")
        print()


# 아래는 위 코드 테스트를 위해서 만들어놓은 샘플입니다. 수정하지 마세요.
# 다음과 같은 결과가 나와야 합니다.
"""
FORWARD:
BACKWARD:
IS_EMPTY? True
FORWARD: 3->1->3->4->
BACKWARD: 4->3->1->3->
IS_EMPTY? False
NODE[3]
NODE[3]
FORWARD: 3->1->9->3->5->4->
BACKWARD: 4->5->3->9->1->3->
FORWARD: 3->1->9->3->5->
BACKWARD: 5->3->9->1->3->
FORWARD: 9->3->5->
BACKWARD: 5->3->9->
FORWARD: 9->
BACKWARD: 9->
IS_EMPTY? False
FORWARD:
IS_EMPTY? True
"""
if __name__ == "__main__":
    list = LinkedList()
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())
    list.add_head(1)
    list.add_head(3)
    list.add_tail(3)
    list.add_tail(4)
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    a = list.find(3)
    print(a)
    b = list.find(3, from_node=a)
    print(b)
    list.add_before(b, 9)
    list.add_after(b, 5)

    list.print()
    list.print(-1)

    c = list.find(4)
    list.remove(c)

    list.print()
    list.print(-1)

    list.remove_head()
    list.remove_head()

    list.print()
    list.print(-1)

    list.remove_tail()
    list.remove_tail()

    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    list.remove_head()
    list.print()
    print("IS_EMPTY?", list.is_empty())
