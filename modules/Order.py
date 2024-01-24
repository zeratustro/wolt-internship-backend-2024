from pydantic import BaseModel, Field, computed_field, model_validator, ValidationError
from datetime import datetime

class Order(BaseModel):
    '''
    Basic Order model
    '''
    cart_value: int = Field(gt=0)
    delivery_distance: int = Field(gt=0)
    number_of_items: int = Field(gt=0)
    time: str

    @model_validator(mode='before')
    @classmethod
    def check_input_data_keys(cls, data):
        if isinstance(data, dict):
            assert set(Order.model_fields.keys()) == set(data.keys())
        else:
            raise ValidationError(f"Incoming JSON do not contain required keys: {Order.model_fields.keys()},"
                                  f"\n provided keys:{data.keys()}")
        return data

    @computed_field(return_type=int)
    @property
    def fee(self):
        #constants for fee
        max_fee = 1500
        zero_fee = 20000
        value = 0
        value = self.multiplicators(value)

        #max fee check
        value = max_fee if value > max_fee else value
        #free delivery check
        value = 0 if value >= zero_fee else value
        return value

    def multiplicators(self, value):
        return value
