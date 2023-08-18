print(f'''
               WELCOME TO BOLLY'S SHOOPING MALL[ FOODS, SNACKS AND WEARS]
Kindly fill in your data for registeration''')
user_info = {}
range = '4'
for i in range:
    Name = input("Enter your name:")
    Email = input("Enter your email:")
    Username = input("Enter your username:")
    Password = int(input("Enter your password:"))
    
    user_info['Name'] = Name
    user_info['Email'] = Email
    user_info['Username'] = Username
    user_info['Password'] = Password
print(user_info)

print(f'''
                LOG INTO YOUR ACCOUNT''')
for i in user_info.keys():
    User = user_info.get('Username')
    Username = input("Please input your username")
    if Username == User:
        pass_code = int(input("Please input your password"))
        # print(pass_code)
        if pass_code == user_info.get('Password'):
            print(f'''
You've logged in successfully\nThanks for being a part of our success advocate \n \n Input your order below
\n \n  Available Products
f'1. Fanta\n
f'2. Softkiss\n
f'3. Burger\n
f'4. Boxers''')

            user_info = user_info
            fanta = 250
            softkiss = 3,200
            burger = 1,000
            boxers = 1,200

            order1 = input('Type in the name of product to be purchased')
            # pickining item 1
            def order_1():
                if (order1 == "fanta"):
                    print("A unit of fanta will cost you $250")
                    q1 = int(input("How many will you like to purchase?"))
                    return fanta * q1
                elif (order1 == "softkiss"):
                    print("A unit of softkiss will cost you $3,200")
                    q1 = int(input("How many packs will you like to purchase?"))
                    return softkiss * q1
                elif (order1 == "burger"):
                    print("A unit of burger will cost you $1,000")
                    q1 = int(input("How many will you like to purchase?"))
                    return burger * q1
                elif (order1 == "boxers"):
                    print("A unit of boxers will cost you $1,200")
                    q1 = int(input("How many will you like to purchase?"))
                    return boxers * q1
                else:
                    print("Product not available")

            order2 = input('Type in the name of product to be purchased')

            # pickining item 2
            def order_2():
                if (order2 == "fanta"):
                    print("A unit of fanta will cost you $250")
                    q1 = int(input("How many will you like to purchase?"))
                    return fanta * q1
                elif (order2 == "softkiss"):
                    print("A unit of softkiss will cost you $3,200")
                    q1 = int(input("How many packs will you like to purchase?"))
                    return softkiss * q1
                elif (order2 == "burger"):
                    print("A unit of burger will cost you $1,000")
                    q1 = int(input("How many will you like to purchase?"))
                    return burger * q1
                elif (order2 == "boxers"):
                    print("A unit of boxers will cost you $1,200")
                    q1 = int(input("How many will you like to purchase?"))
                    return boxers * q1
                else:
                    print("Product not available")


            order3 = input('Type in the name of product to be purchased')

            # pickining item 3
            def order_3():
                if (order3 == "fanta"):
                    print("A unit of fanta will cost you $250")
                    q1 = int(input("How many will you like to purchase?"))
                    return fanta * q1
                elif (order3 == "softkiss"):
                    print("A unit of softkiss will cost you $3,200")
                    q1 = int(input("How many packs will you like to purchase?"))
                    return softkiss * q1
                elif (order3 == "burger"):
                    print("A unit of burger will cost you $1,000")
                    q1 = int(input("How many will you like to purchase?"))
                    return burger * q1
                elif (order3 == "boxers"):
                    print("A unit of boxers will cost you $1,200")
                    q1 = int(input("How many will you like to purchase?"))
                    return boxers * q1
                else:
                    print("Product not available")
            # total spending
            def total_spending():
                    return order_1()+order_2()+order_3()

            user_info['Product History'] = [order1, order2, order3]
            user_info['Net Spending']    = total_spending()
            print(user_info)
        else:
            print("invalid password")
    else:
        print("User can't be found")




    
