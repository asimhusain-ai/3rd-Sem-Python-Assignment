def llc(head):
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

s1 = llc([3,5,7,1])
print(s1)