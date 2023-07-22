@app.route("/api/vc")
def verifyCode_create():
    phone = request.args.get("phone")
    code = generate_verification_code()
    print(code)
    session["verify-code"] = code
    return "ok"
