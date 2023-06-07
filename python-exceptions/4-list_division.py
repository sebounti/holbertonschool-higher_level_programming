#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mylist = []
    for index in range(list_length):
        diviseur = 0
        try:
            diviseur = (my_list_1[index] / my_list_2[index])
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by zero")
        except (IndexError):
            print("out of range")
        finally:
            mylist.append(diviseur)
    return (mylist)
