import pytest

@pytest.mark.run(order=2)
def test_method_1(set_up):
    print("Method 1")

@pytest.mark.run(order=1)
def test_method_2(set_up):
    print("Method 2")

@pytest.mark.run(order=6)
def test_method_3(set_up):
    print("Method 3")

@pytest.mark.run(order=3)
def test_method_4(set_up):
    print("Method 4")

@pytest.mark.run(order=5)
def test_method_5(set_up):
    print("Method 5")

@pytest.mark.run(order=4)
def test_method_6(set_up):
    print("Method 6")
