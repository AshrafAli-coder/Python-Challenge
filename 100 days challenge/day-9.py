logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dic={}
choice="yes"
while choice!="no":
    name=input("What is your name: ")
    bid=int(input("What is your bid: $"))
    dic[name]=bid
    choice=input("Are there any other bidders? yes or no.\n").lower()
    print("\n"*75)
win=max(dic,key=dic.get)
t=dic[win]
print(f"The winner is {win} with a bid of ${t}")