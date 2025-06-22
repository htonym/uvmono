from lib_b.calc import add_two_nums
from lib_b.info import lib_name


def test_add_two_nums():
    assert add_two_nums(3, 4) == 7


def test_lib_name():
    lib_name()
    assert True
