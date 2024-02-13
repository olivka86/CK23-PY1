class Animal:
    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строку с информацией о животном.
        """
        return f"{self.name} - {self.age} years old"

    def __repr__(self) -> str:
        """
        Возвращает строку, представляющую объект класса в виде кода Python.
        """
        return f"Animal(name='{self.name}', age={self.age})"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки в годах.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Возвращает строку с звуком, издаваемым собакой.
        """
        return "Woof woof!"

    def train(self, command: str) -> str:
        """
        Обучает собаку выполнению команды.

        :param command: Команда для обучения собаки.
        :return: Строка с подтверждением выполнения команды.
        """
        return f"{self.name} has executed the command: {command}"


if __name__ == "__main__":
    # Пример использования классов
    my_dog = Dog(name="Buddy", age=3, breed="Labrador Retriever")
    print(my_dog)  # Вывод: Buddy - 3 years old
    print(my_dog.make_sound())  # Вывод: Woof woof!
    print(my_dog.train("Sit"))  # Вывод: Buddy выполнила команду: Сидеть
