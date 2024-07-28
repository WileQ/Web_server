import socket

HOST, PORT = '', 8000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f"Listening to port {PORT}")
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    output = request_data.decode().split('\n')
    filename = output[0].split()[1]

    filename = "htmls" + filename

    if filename == "htmls/":
        filename = "htmls/general.html"

    try:
        fin = open(filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'


    client_connection.sendall(response.encode())
    client_connection.close()