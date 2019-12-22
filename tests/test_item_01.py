import pytest
from ch1.item_01_byte_str_unicode import to_str

def test_item_3_to_str_should_return_str():
    input_str = to_str('hello')
    input_bytes = to_str(b'hello')
    assert input_str == 'hello'
    assert input_bytes == 'hello'
    assert isinstance(input_bytes, str)


