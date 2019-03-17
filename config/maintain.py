import configparser
import os


def main():
    conf = configparser.ConfigParser()

    conf.add_section("SAMPLE_SIZES")
    conf["SAMPLE_SIZES"]["tiny_test_size"] = "10"
    conf["SAMPLE_SIZES"]["very_small_test_size"] = "50"
    conf["SAMPLE_SIZES"]["small_test_size"] = "100"
    conf["SAMPLE_SIZES"]["med_test_size"] = "500"
    conf["SAMPLE_SIZES"]["big_test_size"] = "1000"
    conf["SAMPLE_SIZES"]["bigger_test_size"] = "5000"
    conf["SAMPLE_SIZES"]["huge_test_size"] = "10000"
    conf["SAMPLE_SIZES"]["unbelievably_huge_test_size"] = "50000"
    conf["SAMPLE_SIZES"]["colossal_test_size"] = "100000"
    conf["SAMPLE_SIZES"]["extreme_test_size"] = "500000"

    conf.add_section("TEST")
    conf["TEST"]["data_shapes"] = "avglcr"

    with open("{}/conf.ini".format(os.getcwd()), "w") as file:
        conf.write(file)


if __name__ == "__main__":
    main()
