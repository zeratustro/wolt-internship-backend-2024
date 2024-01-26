import pytest
from modules.Order import Order

# 2 positive test only
@pytest.mark.parametrize("input, output",[
    ({"cart_value": 790, "delivery_distance": 2235, "number_of_items": 1, "time": "2024-01-26T13:00:00Z"}, 710),
    ({"cart_value": 790, "delivery_distance": 2235, "number_of_items": 1, "time": "2024-01-26T16:00:00Z"}, 852),
])
def test_Order(input, output):
    order = Order(**input)
    assert order.fee == output

