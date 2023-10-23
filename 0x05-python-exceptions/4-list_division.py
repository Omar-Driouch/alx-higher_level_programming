#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]

        except (ValueError, TypeError):
            print("wrong type")
            res = 0

        except ZeroDivisionError:
            print("division by 0")
            res = 0

        except IndexError:
            print("out of range")
            res = 0

        finally:
            my_list_3.append(res)
    return my_list_3
