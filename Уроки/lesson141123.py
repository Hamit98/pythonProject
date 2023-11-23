import requests

url = "https://httpbin.org/image/jpeg"
response = requests.get(url)
# print(response)
# print(response.content)

path_to_download = r"C:\Users\User\PycharmProjects\pythonProject\Уроки\test_img.jpg"

with open(path_to_download, "wb") as file:
    file.write(response.content)

