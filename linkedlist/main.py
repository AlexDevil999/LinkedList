from linked_list import LinkedList

def main():
    
    arr = list()
    ll = LinkedList()
    
    for i in range(1,100,5):
        arr.append(i)
        

    ll.insert_values(arr)
    ll.remove(1)
    ll.insert_index(1,100)
    ll.print()
    print(ll.count())


if __name__ == "__main__":
    main()