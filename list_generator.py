import random
import exceptions


class ListGenerator:
    def __init__(self, amount=10, shape="r", max=100, min=0):
        """
        function used to generate list of elements in difrent shapes and ranges
        :param amount: amount of elements in generated list
        :param shape: shape of generated data
        shapeS:
        r - random
        a - A shaped
        v - V shaped
        g - growing
        l - lowering
        c - continuous
        """
        self.amount = amount
        self.shape = shape
        self.MIN_VALUE = min
        self.MAX_VALUE = max
        self.list = self.generate()

    def generate(self):
        """
        generation algorithm creates two list and compose them,
        to create ordered shape
        :return: list in given shape and range
        """
        if self.shape == "c":
            # creation list with the same value is coping one value
            # "amount" times
            return [self.get_randint()] * self.amount

        part_a = list()
        part_b = list()

        for i in range(self.amount // 2):
            part_a.append(self.get_randint())
            part_b.append(self.get_randint())

        if self.shape == "r":
            # creating random ordered list is concatenating two random ordered lists
            return part_a + part_b

        if self.shape == "l":
            return sorted(part_a + part_b)[::-1]
        if self.shape == "g":
            # ascending ordered list is created by sorting unio of two list
            return sorted(part_a + part_b)

        part_a = sorted(part_a)
        part_b = sorted(part_b)

        if self.shape == "a":
            # a shaped list is created by concat ascending ordered list
            # and reversed ascending ordered list
            return part_a + part_b[::-1]
        if self.shape == "v":
            # v shaped list is created by concat reversed ascending ordered list and
            # ascending ordered list
            return part_a[::-1] + part_b

        # if any of checked shapes was not meet then given shape is wrong
        raise exceptions.ChartShapeException("{} is not a proper chart type".format(self.shape))

    def get_randint(self):
        """
        get random int in given constraints
        :return:
        """
        return random.randint(self.MIN_VALUE, self.MAX_VALUE)


if __name__ == "__main__":
    print(ListGenerator(shape="g",max=1000).generate())
