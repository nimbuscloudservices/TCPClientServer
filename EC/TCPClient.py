import socket
import threading

END_CONVO_KEYWORD = "Bye"
SERVER = '10.0.0.3'
PORT = 12013
ADDR = (SERVER, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)
print("Connected to server {0}:{1}".format(SERVER,PORT))


def recv_msg():
    """
    receives messages from server until END_CONVO_KEYWORD
    :return:
    """
    print("[Client] Ready to receive messages.")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg == END_CONVO_KEYWORD:
                break
            elif msg:
                print(msg)
        except socket.error as e:
            print("An error occurred!")
            print(str(e))
            client_socket.close()
            break


def send_msg():
    """
    Sends message to server
    :return:
    """
    print("[Client] Ready to send messages")
    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())


def launch_client():
    recv_thread = threading.Thread(target=recv_msg)
    recv_thread.start()
    send_thread = threading.Thread(target=send_msg)
    send_thread.start()
    # listens for messages from server until END_CONVO_KEYWORD
    recv_msg()

    client_socket.close()


if __name__ == "__main___":
    launch_client()
