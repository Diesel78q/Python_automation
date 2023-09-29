import pytest


@pytest.fixture()
def set_up():
    print("login completed")
    yield
    print("Out from system")

@pytest.fixture(scope="function")
def some():
    print("start")
    yield
    print("end")