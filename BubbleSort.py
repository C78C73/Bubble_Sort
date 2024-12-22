#bubble sort

list = [9,2,6,7,1,3,5,8,4,0]

def main():
    print("\nOriginal list:\n",*list)
    print("\nSorted list:\n")
    bubble_sort(list)

def bubble_sort(list):
    
    x = 0
    y = 1

    for x in range(len(list)-1):
        if (list[x] > list[y]):
            list[x], list[y] = list[y], list[x]
            print(*list)
        else:
            print(*list)
        y += 1
    

main()