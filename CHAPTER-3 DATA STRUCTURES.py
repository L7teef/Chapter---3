# 1.                      Store the names of a few of your friends in a list called names. 
#                  Print each person’s name by accessing each element in the list, one at a time.

#ANSWER :

# names = ["Aiman","Ridwan","Gavin","Aarin","Fawwaz","Nattu","Saif"]
# name1,name2,name3,name4,name5,name6,name7 = names
# print(name1)
# print(name2)
# print(name3)
# print(name4)
# print(name5)
# print(name6)
# print(name7)


# 2.                     Start with the list you used in Exercise 1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be 
#                                     personalized with the person’s name.

#ANSWER :

# names = ["Aiman","Ridwan","Gavin","Aarin","Fawwaz","Nattu","Saif"]
# name1,name2,name3,name4,name5,name6,name7 = names
# print(name1,"is from Bangladesh")
# print(name2,"is from Bangladesh too")
# print(name3,"is from Mumbai, India")
# print(name4,"is from Kerala, India")
# print(name5,"is from Nigeria")
# print(name6,"is from Mumbai, India just like", name3)
# print(name7,"is from Alexandria, Egypt")


# 3.          Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list
#                      to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

#ANSWER :

# cars = ['Toyota supra','Nissan skyline','Mazda RX7']
# car1,car2,car3 = cars
# print("I would like to own a",car1)
# print("Or a",car2)
# print("and i would also like to own",car3)

# 4.                          If you could invite anyone to dinner, who would you invite? Make a list that includes at least three people you’d
#                                 like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner.

#ANSWER :

# names = ['Aiman', 'Aarin', 'Gavin']

# print(names[0])
# print(names[1])
# print(names[2])

# 5.                                   You just heard that one of your guests can’t make the
#                     dinner, so you need to send out a new set of invitations. You’ll have to think of
#                                                  someone else to invite.

#ANSWER :

# #Invite some people to dinner.
# guests = ['Aiman', 'Aarin', 'Gavin']

# name = guests[0].title()
# print(name + ", please come to dinner.")

# name = guests[1].title()
# print(name + ", please come to dinner.")

# name = guests[2].title()
# print(name + ", please come to dinner.")

# name = guests[1].title()
# print("\nSorry, " + name + " can't make it to dinner.")

# # Aarin can't make it! Let's invite Gary instead.
# del(guests[1])
# guests.insert(1, 'Ridwan')

# # Print the invitations again.
# name = guests[0].title()
# print("\n" + name + ", please come to dinner.")

# name = guests[1].title()
# print(name + ", please come to dinner.")

# name = guests[2].title()
# print(name + ", please come to dinner.")


# 6.                                  You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#                               Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#                    Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person 
#                                                             letting them know you’re sorry you can’t invite them to dinner.
#                                            Print a message to each of the two people still on your list, letting them know they’re still invited.
#                  Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

#ANSWER :

# print("\nSorry, we can only invite two people to dinner.")

# # There should be two people left. Let's invite them.
# name = guests[0].title()
# print(name + ", please come to dinner.")

# name = guests[1].title()
# print(name + ", please come to dinner.")

# # Empty out the list.
# del(guests[0])
# del(guests[0])

# # Prove the list is empty.
# del(guests[0])
# print(guests)


# 7.Think of at least five places in the world you’d like to visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

#ANSWER :

          ##Store the locations in a list. Make sure the list is not in alphabetical order.
# locations = ['abu dhabi', 'dubai', 'canada', 'global vilage', 'galleria mall']
          ##Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
# print("Original order:")
# print(locations)
          ##Use sorted() to print your list in alphabetical order without modifying the actual list.
# print("\nAlphabetical:")
# print(sorted(locations))
          ##Show that your list is still in its original order by printing it.
# print("\nOriginal order:")
# print(locations)
          ##Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# print("\nReverse alphabetical:")
# print(sorted(locations, reverse=True))
          ##Show that your list is still in its original order by printing it again.
# print("\nOriginal order:")
# print(locations)
          ##Use reverse() to change the order of your list. Print the list to show that its order has changed.
# print("\nReversed:")
# locations.reverse()
# print(locations)
          ##Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# print("\nOriginal order:")
# locations.reverse()
# print(locations)
          ##Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# print("\nAlphabetical")
# locations.sort()
# print(locations)
          ##Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
# print("\nReverse alphabetical")
# locations.sort(reverse=True)
# print(locations)