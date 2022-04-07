class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode, terminal:ListNode):
        cur = head
        pre = None
        while cur != terminal:
            # 留下联系方式
            next = cur.next
            # 修改指针
            cur.next = pre

            # 继续往下走
            pre = cur
            cur = next
         # 反转后的新的头尾节点返回出去
        return tail, head

    #递归前序遍历
    def dfs(self,head,pre):
        if head==None:
            return pre
        next=head.next
        head.next=pre
        self.dfs(next,head)

    #递归后序遍历
    def dfs(self,head,next):
        if not next:return head
        self.dfs(next,next.next)
        next.next=head

