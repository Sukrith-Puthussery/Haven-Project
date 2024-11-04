print("This is the Anonymous Messaging page.")
print("-------------------------------------------------------------------------------------")
def text_cycle():
 print("Users type below. User one, scroll right and type after the arrow.")
 texter1 = input("User 1 -                                                                                                                                                                              Here-->")
 print("                                                      Anonymous User 1:------------------------------------")
 print("                                                      |                                                   |")
 print("                                                      |", (texter1), "                                    |")
 print("                                                      |                                                   |")
 print("                                                      |                                                   |")
 print("                                                      |                                                   |")
 print("                                                      |                                                   |")
 print("                                                      ------------------------------------------------------")
 texter2 = input("User 2 -Here-->")

 print("                                                                                 Anonymous User 2:------------------------------------")
 print("                                                                                 |                                                   |")
 print("                                                                                 |", (texter2), "                                    |")
 print("                                                                                 |                                                   |")
 print("                                                                                 |                                                   |")
 print("                                                                                 |                                                   |")
 print("                                                                                 |                                                   |")
 print("                                                                                 ------------------------------------------------------")

x = 5 #int(input("Type the number of back-and-forth messages. For example, user 1 saying hey and user 2 saying hi would be 1."))
count = 0
while x>0:
    text_cycle()






