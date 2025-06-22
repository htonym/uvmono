from lib_b.info import lib_name
from lib_b.calc import add_two_nums


def main():
    print("Hello from service-2!")
    lib_name()
    print("3 + 4 =", add_two_nums(3, 4))


if __name__ == "__main__":
    main()
