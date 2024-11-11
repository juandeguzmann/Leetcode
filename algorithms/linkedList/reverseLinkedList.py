def reverseList(lst):
    # Step 1: Convert list to linked list
    head = None
    for value in reversed(lst):  # Build linked list from the end
        head = {"value": value, "next": head}
    
    # Step 2: Reverse the linked list
    prev = None
    current = head
    while current is not None:
        next_node = current["next"]
        current["next"] = prev
        prev = current
        current = next_node
    
    # Step 3: Convert reversed linked list back to a list
    reversed_list = []
    while prev is not None:
        reversed_list.append(prev["value"])
        prev = prev["next"]
    
    print(reversed_list)
