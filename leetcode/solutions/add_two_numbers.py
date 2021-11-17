from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """
        For present ListNode as on LeetCode, e.g.:
        ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3,
        next: None}}}.
        """
        out = f'ListNode{{val: {self.val}, next: '
        current = self
        length = 1
        while current.next:
            current = current.next
            out += f'ListNode{{val:{current.val}, next: '
            length += 1
        return out + 'None' + '}' * length


def str_from_linked_list(linked_list: ListNode):
    result = str(linked_list.val)
    while linked_list.next:
        linked_list = linked_list.next
        result += str(linked_list.val)
    return result[::-1]


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode],
                        l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = int(str_from_linked_list(l1))
        l2 = int(str_from_linked_list(l2))
        result_linked_list = None
        for x in str(l1 + l2):
            result_linked_list = ListNode(x, result_linked_list)
        return result_linked_list


if __name__ == '__main__':
    l1_list = [2, 4, 3]
    l2_list = [5, 6, 4]
    input_l1 = None
    for x in l1_list[::-1]:
        input_l1 = ListNode(x, input_l1)
    input_l2 = None
    for x in l2_list[::-1]:
        input_l2 = ListNode(x, input_l2)

    solution = Solution()
    print(solution.add_two_numbers(input_l1, input_l2))
