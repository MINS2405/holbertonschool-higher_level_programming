#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list


if __name__ == "__main__":
    # Exemple de test
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    idx = 3
    new_list = delete_at(my_list, idx)
    print("List after deletion at index {}:".format(idx), new_list)
    print("Current state of my_list:", my_list)

    # Test avec un index négatif
    my_list2 = [10, 20, 30]
    print("\nOriginal list:", my_list2)
    idx = -1
    new_list2 = delete_at(my_list2, idx)
    print("List after deletion at index {}:".format(idx), new_list2)

    # Test avec un index trop grand
    my_list3 = [100, 200, 300]
    idx = 10
    print("\nOriginal list:", my_list3)
    new_list3 = delete_at(my_list3, idx)
    print("List after deletion at index {}:".format(idx), new_list3)
