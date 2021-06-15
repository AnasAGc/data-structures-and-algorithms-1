from linked_list.linked_list import LinkedList

def zipLists (ll1,ll2):
    current1 = ll1.head
    current2 = ll2.head
    status1 = True
    status2 = True
    if(not current1):
        status1 = False
    if(not current2):
        status2 = False
    if(status1 and status2):
        new = LinkedList()
        while(current1.next != None or current2.next != None or status1 or status2):
            if current1.next != None:
                new.append(current1.value)
                current1 = current1.next
            elif (current1.value and status1):
                new.append(current1.value)
                status1 = False

            if current2.next != None:
                new.append(current2.value)
                current2 = current2.next
            elif (current2.value and status2):
                new.append(current2.value)
                status2 = False
        return new.head
    elif status1:
        new = ll1
        return new.head
    elif status2:
        new = ll2
        return new.head
    else:
        new = LinkedList()
        return new.head



if __name__ == '__main__':
    ll1 = LinkedList()
    # ll1.append(1)
    # ll1.append(3)
    # ll1.append(2)
    # 's' 4 -1 7
    ll2 = LinkedList()
    # ll2.append(5)
    # ll2.append(9)
    # ll2.append(4)
    # ll2.insert('w')
    # 'w' 17 -2 'q'
    # new,h = zipLists(ll1,ll2)
    # print(h)