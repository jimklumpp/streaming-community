import struct, sys, json
import SocketServer
from base64 import b64encode
from hashlib import sha1
from mimetools import Message
from StringIO import StringIO

CHANNELS = {}
CLIENTS = []

class WebSocketsHandler(SocketServer.StreamRequestHandler):
    magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

    def setup(self):
        SocketServer.StreamRequestHandler.setup(self)
        print "Connection established", self.client_address
        self.handshake_done = False
        self.keep_alive = True
        CLIENTS.append(self)

    def handle(self):
        while self.keep_alive:
            if not self.handshake_done:
                self.handshake()
            else:
                self.read_next_message()

    def read_next_message(self):
        b2 = self.rfile.read(2)
        if len(b2) < 1 or ord(b2[0]) & 15 == 8:
            self.finish()
            return False
        
        length = ord(b2[1]) & 127
        if length == 126:
            length = struct.unpack(">H", self.rfile.read(2))[0]
        elif length == 127:
            length = struct.unpack(">Q", self.rfile.read(8))[0]
        masks = [ord(byte) for byte in self.rfile.read(4)]
        
        decoded = ""
        for char in self.rfile.read(length):
            decoded += chr(ord(char) ^ masks[len(decoded) % 4])

        print decoded
        self.on_message(decoded)

    def send_message(self, message):
        self.request.send(chr(129))
        length = len(message)
        if length <= 125:
            self.request.send(chr(length))
        elif length >= 126 and length <= 65535:
            self.request.send(126)
            self.request.send(struct.pack(">H", length))
        else:
            self.request.send(127)
            self.request.send(struct.pack(">Q", length))
        self.request.send(message)

    def handshake(self):
        data = self.request.recv(1024).strip()
        headers = Message(StringIO(data.split('\r\n', 1)[1]))
        if headers.get("Upgrade", None) != "websocket":
            return
        
        print 'Handshaking...'
        key = headers['Sec-WebSocket-Key']
        digest = b64encode(sha1(key + self.magic).hexdigest().decode('hex'))
        response = 'HTTP/1.1 101 Switching Protocols\r\n'
        response += 'Upgrade: websocket\r\n'
        response += 'Connection: Upgrade\r\n'
        response += 'Sec-WebSocket-Accept: %s\r\n\r\n' % digest
        self.handshake_done = self.request.send(response)
        print "Handshake done!"

    def on_message(self, message):
        for CLIENT in CLIENTS:
            CLIENT.send_message(message)

    def finish(self):
        if self.keep_alive == True:
            print "Client closed connection"
            self.keep_alive = False
            if self in CLIENTS:
                CLIENTS.remove(self)
            self.request.close()

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    server = ThreadedServer(("", 8080), WebSocketsHandler)
    server.serve_forever()
