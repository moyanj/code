import sys
#获取命令行参数
command_line_parameters = sys.argv
#判断命令行参数
if "-f" in command_line_parameters:
    #获取-f的索引
    findex = command_line_parameters.index("-f")
    #获取-f的参数
    filepath = command_line_parameters[findex + 1]
    #调用filepath函数运行
    # 代码
    # print(filepath)
#获取参数长度
elif len(command_line_parameters) < 2:
    main()
elif "-v" in command_line_parameters:
    #读取消息并输出
    print(message["version"])
