"""
Iterator: an object that can be iterated upon. An object that returns data
when next() is called. Like list, string..
Iterable: An object which will return iterator when iter() is called.
For example:

my_list = [1,2,3,4,5]
iter(my_list) ==> my_list is iterable which returns Iterator when iter() is called.
When next() is called on iter(my_list) it will run until StopIteration Error.
"""

def my_for(iterable):
    """
    Here iterable is string or list and iterator is returned after iter()
    """
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("End of iterator")
            break


my_for("Hello")
my_for([1,2,3,4,5])
