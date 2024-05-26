import pytest
from hello.hello import hello
def test_hello():
    assert hello("Василий")=="hello"+ " Василий"+"!"
    assert hello(8)=="hello 8!"
    assert hello("fffff")=="hello "+"fffff"+"!"
