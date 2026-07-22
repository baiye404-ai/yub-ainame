from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Annotated, Literal, List
UsernameStr=Annotated[str,Field(...,min_length=4,max_length=20,description="用户名")]
RawPasswordStr = Annotated[str, Field(min_length=6, max_length=20, description="密码")]
class RegisterIn(BaseModel):
    email:EmailStr
    username:UsernameStr
    password:RawPasswordStr
    confirm_password:RawPasswordStr
    code:Annotated[str,Field(min_length=4,max_length=4,description="邮箱验证码")]
    @model_validator(mode="after")
    def password_is_match(self):
        if self.password!=self.confirm_password:
            raise ValueError("两个密码不统一!")
        return self
class UserCreateSchema(BaseModel):
    email:EmailStr
    username:UsernameStr
    password : RawPasswordStr
class LoginIn(BaseModel):
    email:EmailStr
    password:RawPasswordStr
class UserSchema(BaseModel):
    id:Annotated[int,Field(...)]
    email:EmailStr
    username:UsernameStr
class LoginOut(BaseModel):
    user:UserSchema
    token:str