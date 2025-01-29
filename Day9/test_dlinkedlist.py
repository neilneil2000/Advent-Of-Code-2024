from dlinkedlist import DLinkedList


def test_append():
    my_list = DLinkedList()
    my_list.append("Hello")
    assert my_list.length == 1
    assert my_list[0] == "Hello"
    my_list.append(1)
    assert my_list.length == 2
    assert my_list[0] == "Hello"
    assert my_list[1] == 1
    my_list.append([1, 2, 3])
    assert my_list.length == 3
    assert my_list[0] == "Hello"
    assert my_list[1] == 1
    assert my_list[2] == [1, 2, 3]


def test_insert():
    my_list = DLinkedList()
    my_list.append("Hello")
    my_list.append(1)
    my_list.append([1, 2, 3])
    assert my_list.length == 3

    my_list.insert("Inserted 0", 0)
    assert my_list.length == 4
    assert my_list[0] == "Inserted 0"
    assert my_list[1] == "Hello"
    assert my_list[2] == 1
    assert my_list[3] == [1, 2, 3]
    my_list.insert("Inserted 2", 2)
    assert my_list.length == 5
    assert my_list[0] == "Inserted 0"
    assert my_list[1] == "Hello"
    assert my_list[2] == "Inserted 2"
    assert my_list[3] == 1
    assert my_list[4] == [1, 2, 3]
    my_list.insert("Inserted 5", 5)
    assert my_list.length == 6
    assert my_list[0] == "Inserted 0"
    assert my_list[1] == "Hello"
    assert my_list[2] == "Inserted 2"
    assert my_list[3] == 1
    assert my_list[4] == [1, 2, 3]
    assert my_list[5] == "Inserted 5"
