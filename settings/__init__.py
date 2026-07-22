from datetime import timedelta
DB_URI = "mysql+aiomysql://root:123456@localhost:3306/yub_ainame?charset=utf8mb4"
# asrdkenkyjqldjjc
# 邮箱相关配置
MAIL_USERNAME="2391874381@qq.com"
MAIL_PASSWORD="asrdkenkyjqldjjc"
MAIL_FROM="2391874381@qq.com"
MAIL_PORT=587
MAIL_SERVER="smtp.qq.com"
MAIL_FROM_NAME="yub-ainame"
MAIL_STARTTLS=True
MAIL_SSL_TLS=False


JWT_SECRET_KEY = "sfsadadafsj32w"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)