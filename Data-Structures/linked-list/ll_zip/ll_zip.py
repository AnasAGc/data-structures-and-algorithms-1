from linked_list.linked_list import LinkedList

# def zipLists (ll1,ll2):
#     current1 = ll1.head
#     current2 = ll2.head
#     status1 = True
#     status2 = True
#     if(not current1):
#         status1 = False
#     if(not current2):
#         status2 = False
#     if(status1 and status2):
#         new = LinkedList()
#         while(current1.next != None or current2.next != None or status1 or status2):
#             if current1.next != None:
#                 new.append(current1.value)
#                 current1 = current1.next
#             elif (current1.value and status1):
#                 new.append(current1.value)
#                 status1 = False

#             if current2.next != None:
#                 new.append(current2.value)
#                 current2 = current2.next
#             elif (current2.value and status2):
#                 new.append(current2.value)
#                 status2 = False
#         return new.head

#     elif status1:
#         return ll1

#     elif status2:
#         return ll2
    
#     else:
#         return LinkedList()

def zipLists (ll1,ll2):
    current1 = ll1.head
    current2 = ll2.head
    new = LinkedList()
    current3 = new.head
    status1 = True
    status2 = True
    if(not current1):
        status1 = False
    if(not current2):
        status2 = False
    if(status1 and status2):
        new.head = current1
        current3 = new.head
        print(current3.value)
        if (not current1.next):
            status1 = False
        else:
            current1 = current1.next
        while(status1 or status2):
            if(status2):
                print(current2.value)
                if current2.next:
                    b = current2.next
                    current3.next = current2
                    current3 = current3.next
                    current2 = b
                elif (current2.value and status2):
                    current3.next = current2
                    current3 = current3.next
                    status2 = False
            if(status1):
                if current1.next:
                    a = current1.next
                    current3.next = current1
                    current3 = current3.next
                    current1 = a
                elif (current1.value and status1):
                    current3.next = current1
                    current3 = current3.next
                    status1 = False
        return new

    elif status1:
        return ll1

    elif status2:
        return ll2
    
    else:
        return LinkedList()


# def zipLists(ll1,ll2):

#     i =0
#     j =0
#     current1 = ll1.head
#     current2 = ll2.head

#     while current1:
#         i += 1
#         current1 = current1.next
#         if current1 == None:
#             break 
#     while current2:
#         j += 1
#         current2 = current2.next
#         if current2 == None:
#             break 

#     if j <= i:
#         current1 = ll1.head
#         current2 = ll2.head

#     if i < j:
#         head = ll2.head.value
#         current1 = ll2.head
#         current2 = ll1.head


#     while current1 != None or current2 != None:

#         if current2 != None:
#             temp = current1.next
#             temp2 = current2.next
#             current1.next = current2
#             current1 = current1.next
#             if temp != None:
#                 current1.next = temp
#                 current1 = current1.next
#             current2 = temp2
        

#         if current1.next == None and current2 == None:
#             current1 = current1.next

#         if current1 == None:
#             if i < j:
#                 ll1.insert(head)
#             return ll1

# def palindrome(ll):
#     current = ll.head
#     res = ''
#     while(current):
#         res += str(current.value)
#         current = current.next
#     rev = res[::-1]
#     if res == rev:
#         return 'TRUE'
#     return 'FALSE'


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    # print(palindrome(ll1))
    # 's' 4 -1 7
    ll2 = LinkedList()
    ll2.append(2)
    # ll2.append(4)
    # ll2.append(6)
    # current1 = ll1.head
    # current2 = ll2.head
    # a = current1.next
    # b = current2.next
    # current1.next = current2
    # current2.next = a
    # current1 = current1.next.next
    new = zipLists(ll1,ll2)
    print('aaa')
    print(str(new))
    # print(ll1.head.value)
    
    # current2 = ll2.head.next
    # print(current1.next.next.value)
    # print(curr)
    # print(str(ll1))
    
    
    # ll2.append(4)
    # ll2.insert('w')
    # 'w' 17 -2 'q'
    # new,h = zipLists(ll1,ll2)
    # print(h)