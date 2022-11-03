def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return  list1[::n]

print(main([1,"a",2,"b",3,"c",4,"d"],2))