import pytest


@pytest.mark.usefixtures("setup")
class fixdemo:

    def testFirstdemo(self):
        print("demo1")


    def testFirstdemo2(self):
        print("demo2")

    def testFirstdemo3(self):
        print("demo3")

def testFirstdemo4():
    print("demo4")