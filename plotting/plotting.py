import numpy
import pandas
import matplotlib.pyplot as mpl
import os
import configparser


class Plotting:
    def __init__(self, algorithm):
        self.algorithm = algorithm.__name__
        self.data_path = "{}/times/{}.csv".format(os.getcwd(), self.algorithm)
        self.config_path = "{}/config/conf.ini".format(os.getcwd())
        self.graphs_path = "{}/sprawozdanie/graphs/".format(os.getcwd())
        self.data = None
        self.config = None
        self.legend = ""
        self.ax = mpl.gca()
        self.shapes = None

        print("----")
        print("Printing chart for algorithm {} started!".format(
            self.algorithm
        ))

    def plot(self):
        self.read_data()
        self.read_config()
        self.create_plot()
        print("Plotting chart for {} finished".format(self.algorithm))

    def read_data(self):
        print("Reading data")
        with open(self.data_path, "r") as file:
            self.data = pandas.read_csv(file, names=["name", "shape", "amount", "time"])

    def read_config(self):
        print("Reading config")
        with open(self.config_path, "r") as file:
            self.config = configparser.ConfigParser()
            self.config.read_file(file)
            self.shapes = self.config["TEST"]["data_shapes"]
            # print(self.config["TEST"]["data_shapes"])

    def create_plot(self):
        print("Creating plots")
        for shape in self.shapes:
            mask = self.data["shape"] == " " + shape
            # print(mask)
            values = self.data[mask]
            values.plot(kind="line", x="amount", y="time", ax=self.ax, logx=False)
            self.legend += shape
        self.save_plot(self.algorithm + "_gather")
        mpl.close()
        mpl.clf()

        print("Created gathered plot")

        self.legend = "time"
        for shape in self.shapes:
            mask = self.data["shape"] == " " + shape
            # print(mask)
            values = self.data[mask]
            values.plot(kind="bar", x="amount", y="time", logy=True)
            self.save_plot(self.algorithm + "_" + shape)
        mpl.close()
        mpl.clf()

        print("Created plots for each shape")

    def save_plot(self, name):
        print("Saving plot {} under {}".format(name, self.graphs_path))
        mpl.legend(self.legend)
        mpl.title(self.algorithm)
        mpl.savefig(self.graphs_path + name, dpi=200)

    def show_plot(self):
        mpl.legend(self.legend)
        mpl.title(self.algorithm)
        mpl.show()
