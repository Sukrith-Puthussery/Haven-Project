print("This is the Anonymous Social Media page.")
print("-------------------------------------------------------------------------------------")


def post_cycle():
 print("Users type below. User one, scroll right and type after the arrow.")
 texter1 = input("User 1, Type Here-->")
 print("                                                      Post:-------------------------------------------------")
 print("                                                      |                                                     |")
 print("                                                     |", (texter1), "                                        |")
 print("                                                    |                                                         |")
 print("                                                    |                                                         |")
 print("                                                     |                                                       |")
 print("                                                      |                                                     |")
 print("                                                      ------------------------------------------------------")



x = 100000000000000000000 #int(input("Type the number of back-and-forth messages. For example, user 1 saying hey and user 2 saying hi would be 1."))
count = 1
while x>0:
    print(count)
    post_cycle()
    count=count+1
