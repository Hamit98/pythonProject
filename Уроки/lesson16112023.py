import pandas as pd


# data = {
#     "Yes": [50, 21],
#     "No": [131, 2]
# }
#
# data2 = {
#     "Bob": ["I liked it", "It was awesome"],
#     "Sue": ["Pretty good", "Bland"]
# }
# df = pd.DataFrame(data2)
# s = pd.Series([30, 24, 33, 45, 57], index=["2015sales", "2016sales", "2017sales", "2018sales", "2019sales" ], name="Product A")
# # s = df.Bob
# # print(df)
# print(s)


df = pd.read_csv(r"C:\Users\User\Desktop\people.csv")


print(df.empty)
