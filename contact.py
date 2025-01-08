#empty dictionary
contacts = {}

while True:
    print('\n Create Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. update Contact')
    print('4. delete Contact')
    print('5. Search Contact')
    print('6. count Contact')
    print('7. exit')
    
    choice = input('Enter your choice = ')

    if choice == '1':
        name = input('Enter your name =')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input ('Enter age = ')
            email = input('enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age':int(age),'email':email,'mobile':mobile}
            print(f'Contact name{name} has been sucessfully!')
    
    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age:{age}, Mobile Number:{mobile}')
        else:
            print('Contact not found!')
    elif choice == '3':
        name = input('Enter name to update = ')
        if name in contacts:
            age = input('Enter updated age = ')
            email = input('Enter updated email = ')
            mobile = input('Enter updated mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile }
        else:
            print('Contact not found!')
    elif choice == '4':
        name = input('Enter contact name to delete')
        if name in contact:
            del contacts[name]
            print(f'Contacts[name] has been deleted succesfully!')
        else:
            print('Contact not found!')
    
    elif choice == '5':
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contact.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name {name}, Age:{age}, Mobile number:{mobile}, Email:{email}')
                found = True
            if not found:
                print('No contacts found')

    elif choice == '6':
        print('Total number of contacts in list = {count(contacts)}')

    elif choice == '7':
        print('Goodbye closing the program')
        break
    else:
        print('Invalid input')

    



            


    

   
