import pytest
from hello.hello import hello
def test_hello():
    assert hello("Василий")=="Hello"+ "Василий"+"!"
    assert hello(8)=="Hello 8!"
    assert hello("fffff")=="Hello "+"fffff"+"!"
