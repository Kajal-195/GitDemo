import pytest


@pytest.fixture()
def firsttest():
    print("Kajal")
    yield
    print("execute later")

@pytest.fixture()
def dataload():
    print("user profile")
    return ["kajal" , "Panda" , "new@abac.com"]