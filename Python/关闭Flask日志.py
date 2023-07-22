from logging import getLogger  # 用于关闭Flask日志
# 关闭flask日志
flog = getLogger("werkzeug")
flog.disabled = True