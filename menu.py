menu_file="menu.txt"
def lode_menu():
    menu=[]
    try:
        with open(menu_file,'r') as file:
            line=file.readlines()
            for l in line:
                menu_info=l.strip().split(",")
                print(menu_info)
                items={
                    'name':menu_info[0],
                    'price':menu_info[1],
                    'description':menu_info[2]
                        }
                menu.append(items)
    except FileNotFoundError:
        print("file not found")
    return menu

def save_menu(menu):
    with open(menu_file,'w') as file:
        for item in menu:
            line=f"{item['name']},{item['price']},{item['description']}\n"
            file.write(line)

def add_items(menu):
    name=input("enter name:")
    price=input("enter price:")
    description=input("enter description:")

    item={
        'name':name,
        'price':price,
        'description':description
        }
    menu.append(item)
    save_menu(menu)
    print("item saved..")

def display_menu(menu):
    if len(menu)>0:
        for index,item in enumerate(menu,1):
            print("="*20)
            print(f"item{index}:")
            print(f"name:{item['name']}")
            print(f"price:{item['price']}")
            print(f"description:{item['description']}")
            print("="*20)
    else:
        print("no item found")

def remove_item(menu):
    name=input("enter name of item to remove: ")
    found_item=[]
    for item in menu:
        if item["name"].lower()==name.lower():
            found_item.append(item)

        if found_item:
            display_menu(found_item)
            index=int(input("enter the index of value to remove:(start from 0)"))
        
        if index>=0 and len(found_item):
            item=found_item[index]
            menu.remove(item)
            save_menu(menu)
            print("item remove suxxesfully...")
        else:
            print("enter valid index")

def search_item(menu):
    quary=input("enter quary: ")
    found_item=[]
    for items in menu:
        if quary.lower() in items['name'].lower() or quary.lower() in items['price'].lower() or quary.lower() in items['description'].lower():
            found_item.append(items)
        
        if found_item:
            print("searching for quary...")
            display_menu(found_item)
        else:
            print("no contact found...")

def edit_menu(menu):
    name=input("enter name of the item to edit: ")
    items_found=[]
    for items in menu:
        if name.lower()==items['name'].lower():
            items_found.append(items)
        
        if items_found:
            display_menu(items_found)
            print("what to edit: ")
            print("1.name")
            print("2.price")
            print("3.decription")

            choice=int(input("enter your choice:"))

            if choice==1:
                new_item=input("enter new name:")
                items['name']=new_item
                save_menu(menu)
                break
            elif choice==2:
                new_item=input("enter new price:")
                items['price']=new_item
                save_menu(menu)
                break
            elif choice==3:
                new_item=input("enter new decription:")
                items['description']=new_item
                save_menu(menu)
                break
            else:
                print("pls enter valid value:")
        else:
            print("item not found:")

def manage_item():
    menu=lode_menu()

    while True:
        print("1:add item:")
        print("2:display item")
        print("3:search item")
        print("4:edit item")
        print("5:remove item")
        print("6:exit")

        choice=input("enter choice: ")

        if choice=="1":
            add_items(menu)
        elif choice=="2":
            display_menu(menu)
        elif choice=="3":
            search_item(menu)
        elif choice=="4":
            edit_menu(menu)
        elif choice=="5":
            remove_item(menu)
        elif choice=="6":
            break
        else:
            print("pls enter valid value")
        
    save_menu(menu)



manage_item()








    
