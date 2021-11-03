class SuperList(list):  
    '''using the parameter list inside of superlist() allows
    the append feature on line 12 to append items to the list variable'''
    def __len__(self):
        return 1000


super_list1 = SuperList()


print(len(super_list1))
super_list1.append(5) #error obj has no attr 'append'
print(super_list1[0])
print(issubclass(SuperList, list)) #issubclass checks to see if list is a subclass of superlist
