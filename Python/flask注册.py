@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        username = request.values.get("un")
        password = request.values.get("pwd")
        tel = request.values.get("tel")
        verifyCode = request.values.get("vc")
        try:
            VCYes = session.get("verify-code")
            if verifyCode == VCYes:
                cursor.execute(
                    "INSERT INTO users (name, pwd, tel) VALUES (?, ?, ?)",
                    (username, password, tel),
                )
                conn.commit()

                # 注册成功后，返回信息
                return "ok"
            else:
                # 验证码错误
                return "vc-err"
        except Exception as e:
            conn.rollback()
            error_message = str(e)
            return "server-err"

    return render_template("reg.html")
