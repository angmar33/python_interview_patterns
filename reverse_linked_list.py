def reverse(head):
    if not head or not head.next:
        return head

    items = head.next
    reversed_list = head
    reversed_list.next = None

    while items:
        temp = items
        items = items.next
        temp.next = reversed_list
        reversed_list = temp

    return reversed_list
