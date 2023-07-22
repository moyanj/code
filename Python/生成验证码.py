def generate_verification_code():
    # 生成所有可能出现在验证码中的字符
    characters = string.ascii_letters + string.digits

    # 生成8位随机验证码
    verification_code = "".join(random.choice(characters) for _ in range(8))

    return verification_code
