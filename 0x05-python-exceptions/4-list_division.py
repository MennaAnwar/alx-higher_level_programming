#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for x in range(list_length):
        result = 0
        try:
            result = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("out of range")
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            newList.append(result or 0)
    return(newList)
