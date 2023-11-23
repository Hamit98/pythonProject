if __name__ == '__main__':
# s.remove(65)
# s.discard(65)
# res = s2.issubset(s)
# res = s.issuperset(s2)
# res = s.difference(s2)
# res = s - s2
# res = s2.difference(s)
# res = s2 - s
# res = s.union(s2)
# res = s.intersection(s2)
# s.add("new elem")
# s.update({"new1", "new2", 90})

#     word = "justcode"
#     glasnye = set()
#     gl2 = "aeiou"
#
#     for i in word:
#         if i in gl2:
#          glasnye.add(i)
#
# print(glasnye)

# s = {1, 2, 3, 4, 5}
#
#     s.remove(3)
#     print(s)

    # a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # b = {2, 4, 6, 8, 10}
    # c = {1, 3, 5, 7, 9}
    #
    # print(a.intersection(b))
    # print(a.difference(b))
    # print(b.union(c))
    #
    # a.clear()
    # b.clear()
    # c.clear()
    #
    # print(a, b, c)

    friends = [
        {"name": "Hamit",
         "age": "24",
         "first_meet_year": 1998
         }, {"name": "Oleg",
         "age": "25",
         "first_meet_year": 1999
         }, {"name": "Arman",
         "age": "26",
         "first_meet_year": 2002
        }
    ]
    current_year = 2023
    for friend in friends:
        if current_year