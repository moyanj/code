@app.after_request
def set_response_headers(response):
    global req_ids
    req_id = req_ids
    response.headers["GSAPI-Version"] = conf["version"]
    response.headers["GSAPI-Request-ID"] = req_id
    # response.headers[]
    # 添加更多的响应头设置
    return response