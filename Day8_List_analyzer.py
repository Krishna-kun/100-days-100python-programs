def basic_stat(number):
    print("\n--->Basic statistics and extremes<---\n")
    if not number:
        print("[!] List is empty")
        return
    total=sum(number)
    count=len(number)
    avg=total/count
    sorted_nums=sorted(number)
    min_sorted_num=sorted_nums[0]
    max_sorted_num=sorted_nums[-1]
    print(f"Total elements  :{count}")
    print(f"Original list   :{number}")
    print(f"Sorted list     :{sorted_nums}")
    print(f"Sum of elements :{total}")
    print(f"Average         :{avg}")
    print(f"Minimum value   :{min_sorted_num}")
    print(f"Maximum value   :{max_sorted_num}")
    unique_sort=sorted(set(number))
    if len(unique_sort)>=2:
        print(f"Second largest from sorted list:{unique_sort[-2]}")
    else:
        print(f"Second largest from sorted list: NONE (all elements are identical)")
def rem_dup_sort(number):
    print("\n--->Remove Duplicate & Sorts<---\n")
    if not number:
        print("\n[!] List is empty")
        return
    unique_ordered=[]
    for num in number:
            if not in unique_ordered:
                unique_ordered.append(num)

    asc_sorted=sorted(unique_ordered)
    desc_sorted=sorted(unique_ordered,reverse=True)
    print(f"\nOrignal list            :{number}")
    print(f"Unique list (Preserved) :{unique_ordered} ")
    print(f"Sorted (Ascending)      :{asc_sorted}")
    print(f"Sorted (Descending)     :{desc_sorted}\n")

def Filter(number):
    print("\n--->Remove Duplicate & Sorts<---\n")
    if not number:
        print("\n[!] List is empty")
        return
    Evenlst=[]
    oddlst=[]
    for num in number:
        if num%2==0:
            Evenlst.append(num)
        else:
            oddlst.append(num)

    print(f"Original list   :{number}")
    print(f"Even list       :{Evenlst}")
    print(f"Odd list        :{oddlst}")

def slicing_list(number):
    print("\n--->Remove Duplicate & Sorts<---\n")
    if not number:
        print("\n[!] List is empty")
        return
    print(f"\nOriginal list       :{number}")
    print(f"Reversed lsit       :{number[::-1]}")
    print(f"Even index element  :{number[::2]}")
    print(f"Odd index element   :{number[1::2]}\n")

#main loop
while True:
    print("="*35)
    print("     LIST ANALYZER       ")
    print("="*35)
    print("1) Basic statistics and extremes")
    print("2) Remove duplicate & sorts")
    print("3) Filter Even 0dd & primes")
    print("4) Slicing & list comprehensions")
    print("5) Exit\n")

    try:
        choose=int(input("Enter your choice[1,2,3,4,5]:"))
    except ValueError:
        print("[!] Enter valid number...")

    if 