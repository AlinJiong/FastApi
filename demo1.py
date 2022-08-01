from pkgutil import extend_path
from typing import List, Optional
from pydantic import BaseModel


from datetime import datetime, date


class User(BaseModel):
    id: int  # 必填字段
    name: str = 'John'  # 有默认值，选填字段
    signup_ts: Optional[datetime] = None # 等价于 Union[datetime, None]
    friends: List[int] = [] # 列表中的元素是int类型，或者可以转换成int类型的数据，例如'123'


external_data = {
    'id':1,
    'signup_ts':'2022-7-14 15:25:21',
    'friends':[1,2,3]
}


user = User(**external_data)
print(user.json())
