class Hotel:
    def __init__(self, name, location, star_rating):
        self.__name = name
        self.__location = location
        self.__star_rating = star_rating
        self.__rooms = []
        self.__reviews = []

    def add_room(self, room):
        self.__rooms.append(room)

    def get_available_rooms(self):
        return [room for room in self.__rooms if not room.is_booked()]

    def book_room(self, room_number):
        for room in self.__rooms:
            if room.get_room_number() == room_number and not room.is_booked():
                room.book()
                return f"Номер {room_number} был забронирован."
        return f"Номер {room_number} не доступен для бронирования."

    def add_review(self, review):
        self.__reviews.append(review)

    def show_reviews(self):
        for review in self.__reviews:
            print(review)

    def __str__(self):
        return f"{self.__name} ({self.__star_rating} звезд(-ы) по адресу {self.__location}"


class Review:
    def __init__(self, customer, rating, comment):
        self.__customer = customer
        self.__rating = rating
        self.__comment = comment

    def __str__(self):
        return f"Оценка: {self.__rating}\nКомментарий: {self.__comment}\nОт: {self.__customer}"


class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.__room_number = room_number
        self.__capacity = capacity
        self.__price_per_night = price_per_night
        self.__is_booked = False

    def get_room_number(self):
        return self.__room_number

    def is_booked(self):
        return self.__is_booked

    def book(self):
        self.__is_booked = True

    def __str__(self):
        return f"Номер комнаты: {self.__room_number}, Вместимость: {self.__capacity}, Цена за сутки: ${self.__price_per_night}"


class Customer:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def __str__(self):
        return f"{self.__name} ({self.__email})"


class Menu:
    customer1 = Customer("Hamit", "hamit123@email.com")

    hotel = Hotel("СуперОтель", "Восточная-Объездная", 4)
    room1 = Room(32, 1, 75)
    hotel.add_room(room1)

    while True:
        print("\n1. Показать отели")
        print("2. Показать отзывы")
        print("3. Забронировать номер")
        print("4. Оставить отзыв")
        print("5. Выход")
        choice = input("Выберите действие [1-5]: ")

        if choice == "1":
            print(hotel)

        elif choice == "2":
            hotel.show_reviews()

        elif choice == "3":
            available_rooms = hotel.get_available_rooms()
            print("Доступные номера:")
            for room in available_rooms:
                print(room)
            room_number = int(input("Введите номер комнаты, которую хотите забронировать: "))
            print(hotel.book_room(room_number))

        elif choice == "4":
            rating = int(input("Поставьте вашу оценку (1-5): "))
            comment = input("Напишите отзыв: ")
            review = Review(customer1, rating, comment)
            hotel.add_review(review)

        elif choice == "5":
            print("До свидания!")
            break

        else:
            print("Произошла ошибка, попробуйте ещё-раз.")