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
        max_fee = 1500

        value = 0
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

    def _multiplicators(self, value:int)->int:
        value = self._multi_smallCart(value)
        value = self._multi_distance(value)
        value = self._multi_bulk(value)
        value = self._multi_rushTime(value)
        return value

    def _multi_smallCart(self, value:int)->int:
        if self.cart_value < 1000:
            value += 1000 - self.cart_value
        return value

    def _multi_distance(self, value:int)->int:
        distance = self.delivery_distance - 1000
        value+=200
        while distance > 0:
            value+=100
            distance-=500
        return value

    def _multi_bulk(self, value:int)->int:
        items = self.number_of_items
        #fee for items
        if items>=5:
            items-=5
            value+=50
            value+=items*50
        #bulk fee
        if self.number_of_items > 12:
            value += 120
        return value

    def _multi_rushTime(self, value:int)->int:
        if self.time.weekday() == 4:
            if time(15,0) <= self.time.time() < time(20,0):
                try:
                    value = int(value * 1.2)
                except:
                    ...
        return value






