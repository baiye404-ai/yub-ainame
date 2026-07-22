from fastapi import FastAPI
from fastapi_mail import FastMail,MessageSchema,MessageType
from fastapi import Depends
from dependencies import get_mail
from aiosmtplib import SMTPResponseException
from routers.auth_router import router as auth_router
from routers.name_router import router as name_router
app=FastAPI()
app.include_router(auth_router)
app.include_router(name_router)
@app.get("/")
async def read_root():
    return {"Hello": "FastAPI"}
@app.get("/mail/test")
async def mail_test(
        email:str,
        mail: FastMail=Depends(get_mail)
):
    message=MessageSchema(
        subject="hello",
        recipients=[email],
        body=f"hello{email}",
        subtype=MessageType.plain,
        from_email=f"yub-ainame <2391874381@qq.com>"
    )
    try:
        await mail.send_message(message)
    except SMTPResponseException as e:
        if e.code == -1 and b"\\x00\\x00\\x00" in str(e).encode():
            print("⚠️ 忽略 QQ 邮箱 SMTP 关闭阶段的非标准响应（邮件已成功发送）")
    return {"message": "邮件发送成功！"}

# fastapi-env\Scripts\activate
#uvicorn main:app --reload
# sk-4872aa4002c94935b5a4f5f9ae0ac4b7