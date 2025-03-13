import socket as sc
import termcolor as tc

with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as socket:
    port=int(input("port > "))
    address=(sc.gethostname(), port)
    socket.bind(address)
    print(tc.colored("bound to the port!", "green"))
    socket.listen()
    print(tc.colored("  listening for images...", "light_cyan"))
    def get_image():
        usr, addr = socket.accept()
        size = usr.recv(1024).decode()
        print(tc.colored("--  received size info "+size, "light_grey"))
        size = int(size)
        print(tc.colored("--  requesting the image...", "light_grey"))
        usr.send("hello there!".encode())
        image_bytes = usr.recv(size)
        with open("received.png", "wb") as f:
            print(tc.colored(f"wrote {len(image_bytes)} bytes", "black", on_color="on_white"))
            f.write(image_bytes)
    while True:
        get_image()