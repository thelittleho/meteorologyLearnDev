import datetime

from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):
    content : str

    # 빈 문자열 방지
    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("not allow empty value")
        return v
    

class Answer(BaseModel):
    id : int
    content : str
    create_date : datetime.datetime