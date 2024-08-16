# CVE-2024-21733-POC

## 注意：

1. tomcat 英文环境
2. 特定构造后端代码，如 ROOT/vulnerable.jsp 内所示
3. 如有需要，修改脚本中的**服务器地址和端口**。默认 `127.0.0.1:8080`
4. 超时触发，默认 20 秒，一般会小于这个时间

## 流程：

1. 下载特定版本 tomcat

https://archive.apache.org/dist/tomcat/

或者使用 docker 环境：`tomcat:9.0.43`
```bash
docker-compose up -d
```

2. 构造 vulnerable.jsp (`ROOT/vulnerable.jsp`) 并上传至 ROOT

3. 运行脚本

![image-20240815174502677](images/image-20240815174502677.png)

## 或者模拟真实环境进行漏洞利用

1. 运行 `victim.py` 模拟正常用户的 POST 请求，响应输出 `ID` 数据
    ![](images/victim.png)
2. 当提示 `[*] Press Enter to close socket connection...` 时运行 `attacker.py` 进行漏洞利用。如果成功，则会在返回数据中出现 `Invalid character found in method name` 以及部分 `ID` 数据
    ![](images/attacker.png)
3. 在运行 `victim.py` 的命令行输入回车结束连接
