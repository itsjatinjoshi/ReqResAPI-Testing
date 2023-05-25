import pytest

from Base.DrivedClass import URL


@pytest.fixture(scope='class')
def class_fixture(request):
    print("Before Class")
    url = URL()
    base_url = url.base_url()
    if request.cls is not None:
        request.cls.base_url = base_url
    yield base_url
    print('\n')


@pytest.fixture()
def method_fixture():
    print("Method Starting")
    yield
    print("Method Ending")
