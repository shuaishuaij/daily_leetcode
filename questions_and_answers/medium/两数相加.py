"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""




# Definition for singly-linked list.
class ListNode:
            def __init__(self, x):
                        self.val = x
                        self.next = None


class Solution:
            def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                        prenode = ListNode(0)
                        lastnode = prenode
                        val = 0
                        while val or l1 or l2:
                                    val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
                                    lastnode.next = ListNode(cur)
                                    lastnode = lastnode.next
                                    l1 = l1.next if l1 else None
                                    l2 = l2.next if l2 else None
                        return prenode.next


def generateList(l: list) -> ListNode:
            prenode = ListNode(0)
            lastnode = prenode
            for val in l:
                        # debug('lastnode.next.val')
                        lastnode.next = ListNode(val)

                        lastnode = lastnode.next

            return prenode.next


def printList(l: ListNode):
            while l:
                        print("%d, " % (l.val), end='')
                        l = l.next
            print('')


class Solution2:
            def addTwoNumbers(self, l1, l2):
                        """
                        :type l1: ListNode
                        :type l2: ListNode
                        :rtype: ListNode
                        """
                        re = ListNode(0)

                        r = re

                        carry = 0
                        while (l1 or l2):
                                    x = l1.val if l1 else 0
                                    y = l2.val if l2 else 0
                                    s = carry + x + y

                                    carry = s // 10  # 除以10的商的整数部分

                                    r.next = ListNode(s % 10)  # 模,除以10的商的余数部分

                                    r = r.next
                                    if (l1 != None): l1 = l1.next
                                    if (l2 != None): l2 = l2.next
                        if (carry > 0):
                                    r.next = ListNode(1)
                        return re.next


"""错误做法"""


class wrong_solution1:
            """这个错误例子错在直接计算再转化为链表会遇到溢出的情况
            """

            def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                        x1 = ''
                        while l1:
                                    x1 += str(l1.val)
                                    l1 = l1.next
                        x2 = ''
                        while l2:
                                    x2 += str(l2.val)
                                    l2 = l2.next
                        res = int(x1[::-1]) + int(x2[::-1])
                        res = str(res)[::-1]
                        ans = ListNode(int(res[0]))
                        ans1 = ans
                        for i in res[1:]:
                                    ans.next = ListNode(int(i))
                                    ans = ans.next
                        return ans1


if __name__ == "__main__":
            # l1 = generateList([1, 5, 8])
            # debug('l1.val')
            # l2 = generateList([9, 1, 2, 9])
            # printList(l1)
            # printList(l2)
            # s = Solution()
            # sum = s.addTwoNumbers(l1, l2)
            # printList(sum)
            #
            l1 = ListNode(1)
            l2 = ListNode(2)
            s2 = Solution2()
            sum2 = s2.addTwoNumbers(l1, l2)
            printList(sum2)
