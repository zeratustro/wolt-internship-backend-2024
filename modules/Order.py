from pydantic import BaseModel, Field, computed_field, field_validator
from datetime import datetime, time

class Order(BaseModel):
    '''
    Basic Order model
    '''
    cart_value: int = Field(gt=0)
    delivery_distance: int = Field(gt=0)
    number_of_items: int = Field(gt=0)
    time: datetime

    @computed_field(return_type=int)
    @property
    def fee(self):
        print("FEE count")
        max_fee = 1500

        value = 10
        value = self._multiplicators(value)
        #max fee check
        value = max_fee if value > max_fee else value
        #free delivery check
        value = 0 if self.cart_value >= 20000 else value
        return value

    @field_validator('time')
    def time_utc_only(cls, v: datetime):
        if not v.tzname() == "UTC":
            raise ValueError('only UTC zone is allowed.')
        return v

    def _multiplicators(self, value):
        value = self._multi_rushTime(value)
        return value

    def _multi_rushTime(self, value):
        print(type(self.time.tzinfo))
        print(self.time.tzname())
        if self.time.weekday() == 4:
            if time(15,0) <= self.time.time() < time(20,0):
                return int(value * 1.2)
        return value



