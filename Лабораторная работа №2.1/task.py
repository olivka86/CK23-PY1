class Wood:
    """Class describe wood parameters"""
    def __init__(self, species: str, length: int, width: int, moisture: int):
        """
        Wood class inizialization

        :param species: type of wood (walnut, cherry, pine, etc.)
        :param length: length of wood piece in millimeters.
        :param width: width of wood piece in millimeters.
        :param moisture:  how much water is present in the wood compared to the dry matter of the wood.

        Example:
        >>> wood = Wood('walnut', 2000, 400, 18)
        """
        self.species = species
        self.length = length
        self.width = width
        self.moisture = moisture

    def check_wood_moisture(self) -> bool:
        """
        Check that wood moisture is under 8% and below 25%

        :return: Boolean valuable.
        """

    def cut_wood(self, new_length: int, new_width: int) -> None:
        """
        Cut wood piece to the new shape

        :param new_length: A new length of the wood piece
        :param new_width: A new width of the wood piece
        """


class Rope:
    ...


class Spoon:
    """Class describes spoon parameters"""
    def __int__(self, shape: str, material: str, size: str, clarity: bool):
        """
        Spoon class initialization

        :param shape: spoon shape
        :param material: spoon material
        :param size: spoon size
        :param clarity: spoon clarity
        """
        self.shape = shape
        self.material = material
        self.size = size
        self.clarity = clarity

    def eat(self, food: str) -> None:
        """
        Eat food with a spoon

        :param food: food type
        """

    def clean_spoon(self) -> None:
        """
        Cleans a spoon
        """


class Knife:
    """Class describes knife parameters"""
    def __int__(self, knife_type: str, material: str, sharpness: int):
        """
        Knife class initialization

        :param knife_type: describe tool assignment
        :param material: describe blade material
        :param sharpness: cutting quality in percent
        """
        self.knife_type = knife_type
        self.material = material
        self.sharpness = sharpness

    def carve_spoon(self, object_to_carve: Wood, shape: str, size: str) -> Spoon:
        """
        Carve a spoon

        :param object_to_carve: input object to carve spoon
        :param shape: describes shape of final spoon
        :param size: describes spoon size type
        :return: Spoon object
        """

    def cut_rope(self, rope: Rope) -> None:
        """
        Cutes the rope

        :param rope: a Rope object
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
