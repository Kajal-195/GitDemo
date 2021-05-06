import pytest

from PytestDemo.baseclass import baseclass


@pytest.mark.usefixtures("dataload")
class newdata(baseclass):

    def test_userprofile(self, dataload):
        log = self.test_logging()
        log.info(dataload)
        print(dataload)