
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.values.get("un")
        password = request.values.get("pwd")

        try:
            cursor.execute(
                "SELECT id FROM users WHERE name = ? AND pwd = ?", (username, password)
            )
            result = cursor.fetchone()
            print(result)
            if not result:
                return "pass"

            user_id = result[0]
            session["id"] = user_id  # 将用户ID存储在会话中

            # 登录成功后，重定向到主页或其他需要登录的页面
            return "ok"
        except Exception as e:
            conn.rollback()
            error_message = str(e)
            return "err"

    return render_template("login.html")