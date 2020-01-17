import numpy as np
import zmq


class SerializerSocket(zmq.Socket):
    def send_image(self, arr, flags=0, copy=True, track=False):
        configs = dict(
            dtype=str(arr.dtype),
            shape=arr.shape
        )
        self.send_json(configs, flags | zmq.SNDMORE)
        return self.send(arr, flags, copy=copy, track=track)

    def recv_image(self, flags=0, copy=True, track=False):
        configs = self.recv_json(flags=flags)
        raw = self.recv(flags=flags, copy=copy, track=track)
        image = np.frombuffer(raw, dtype=configs['dtype'])
        return image.reshape(configs['shape'])


class SerializerContext(zmq.Context):
    _socket_class = SerializerSocket


class Connector:
    def __init__(self, host, port=2436):
        address = "tcp://{}:{}".format(host, port)
        self.context = SerializerContext()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(address)

    def query(self, image):
        if not image.flags['C_CONTIGUOUS']:
            image = np.ascontiguousarray(image)
        self.socket.send_image(image, copy=False)
        return self.receive()

    def receive(self):
        return self.socket.recv_pyobj()
