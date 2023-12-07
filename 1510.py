'''
Hard:
This problem was asked by Microsoft.

Implement 3 stacks using a single list:
'''
# If array was static size, could use modulo approach (index w/ i*3, i*3+1, i*3+2), or have s1 and s2 grow inward 
#   from ends and s3 grow from middle, with resize on full. with dynamic python list, this was my approach sacrificing TC for SC

# each stack grows left to right sequentially. stack pointers sp hold index to insert next item. 
#    stack 3 appends and pops from end, using sp2 to know if empty, as stack2 uses sp1 to know when it's empty
class Stack:
    def __init__(self):
        self.list = []
        self.sp1 = 0
        self.sp2 = 0

    def pop(self, stack_number):
        if stack_number == 1:
            if self.sp1 > 0:
                self.sp1 -= 1
                self.sp2 -= 1
                return self.list.pop(self.sp1)
            return None
        elif stack_number == 2:
            if self.sp2 > self.sp1:
                self.sp2 -= 1
                return self.list.pop(self.sp2)
            return None
        else:
            if len(self.list) > self.sp2:
                return self.list.pop()
            return None

    def push(self, item, stack_number):
        if stack_number == 1:
            self.list.insert(self.sp1, item)
            self.sp1 += 1
            self.sp2 += 1
        elif stack_number == 2:
            self.list.insert(self.sp2, item)
            self.sp2 += 1
        else:
            self.list.append(item)
        

s = Stack()

s.push(4,2)
s.push(5,2)
s.push(6,2)
s.push(1,1)
s.push(2,1)
s.push(8,3)
s.push(9,3)

# s.pop(2)
# s.pop(3)
# s.pop(1)
# s.pop(2)

print(s.list)