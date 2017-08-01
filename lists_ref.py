#Example of lists

list1 = [ 0, 1, 2, 3, 4, 5] #List locations start at 0. So when you call 0, returns 0

list2 = [0, 1, 2, 3, 4, 5] #The last item in a list is -1, second to last -2
                            #In list2 if you called -1 its 5, -2 is 4




#You can make a list inside a list. It is not restricted to a certain or just one type.\
x = [["a", "b", "c", "d", "e"],
     ["d", "e", "f", "g", "h", "i"],
     ["g", "h", "i", "j", "k"]]

print(x[2]) #Will print the 3rd list 
print(x[1][2]) # Will print the 2nd list and 3rd item
print(x[0][1:4]) #Will print the list items from 3 to 4, it does not print the end item
print(x[0][2:]) #Will print first list from item 3 to the end
print(x[0][:2]) #will print first list from begining to item 3
#Note: To print the last item on a list you go a number higher than the item


#You can have multiple types inside a list example belows shows integer, string, and an operation
#However this is not the most common use
list3 = [1, "hello", 2 * 2]
print(list3)
print(list3[0]) #Will print the first item


print(type(list3)) #type(variable_Name) shows you what type that variable is

#Adding and Removing Elements to a list

#Add Elemet
list1 + ["Hello", "World"] 
    
#You can also make a list while adding items to a list
list4 = list3 + ["Add", "on"]

#Replacing item on a list

list3[-1] = "Bye"

#Deleting Element
del(list1[0])

#You can place more than one command on the same line by using ;
del(list3[0]); del(list1[1])

#You can also copy a list and make it its own list
superlist = list(list3)
superlist[0] = "new list item" #By doing this it won't change list3 elements
