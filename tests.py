import configparser
import datetime
import os
import exceptions
import list_generator
import colored
import random


class Test:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.conf = self.read_config()
        self.test()

    def test(self):
        for data_shape in self.conf["TEST"]["data_shapes"]:
            for data_size in self.conf["SAMPLE_SIZES"]:
                # print(data_shape, data_size)
                self.color_console()
                data_size = self.conf["SAMPLE_SIZES"][data_size]
                print("Testing {}, on data type \"{}\" containing {} elements".format(
                    self.algorithm.__name__,
                    data_shape,
                    data_size
                ))
                data = list_generator.ListGenerator(
                    amount=int(data_size),
                    shape=data_shape)
                self.test_unit(data)
                print()

    def test_unit(self, data):
        list = data.list
        algorithm_name = self.algorithm.__name__
        time_delta = 0

        start_date = datetime.datetime.now()
        self.algorithm(list)
        end_date = datetime.datetime.now()
        time_delta = end_date - start_date

        print("--- RESULT ---")
        print("Name: {}".format(algorithm_name))
        print("Time: {}".format(time_delta.total_seconds()))
        print("list sample: {} elements, in shape {}".format(
            len(list),
            data.shape
        ))

        with open("{}/times/{}.csv".format(os.getcwd(), algorithm_name), "a") as file:
            text = "{}, {}, {}, {}\n".format(
                algorithm_name,
                data.shape,
                len(list),
                time_delta.total_seconds()
            )

            file.write(text)
            file.close()

    def read_config(self):
        conf = configparser.ConfigParser()
        with open("{}/config/conf.ini".format(os.getcwd()), "r") as file:
            conf.read_file(file)
            return conf
        raise exceptions.NoIniFile()

    def color_console(self):
        color = colored.fg(random.randint(0, 255))
        print(color)
