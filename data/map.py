from zlib import decompress, compress
from base64 import b64decode, b64encode
from colorama import Back

class Map:

    def __init__(self):
        self

    def pre_map(self, index):
        room = [" ", " "]
        room[index] = Back.GREEN + "Y" + Back.RESET
        compressed_pre_map = decompress(b64decode('eJzjUlDwU0AFXOEK2gquqEIKCsHoqhQwAFRIX1dXVxuIYxBCNQrVtTACKhQDVaUPVgUAEN0UxQ==')).decode("utf-8")
        print(compressed_pre_map.format(room[0],room[1]))

    def post_map(self, index):
        room = [" "," "," "," "," "," "," "," "," "]
        room[index] = Back.GREEN + "Y" + Back.RESET
        compressed_post_map = decompress(b64decode('eJzjUlDwU0AF+rq6ujFgFle4graCK4pkjUJ1LZAASSooBKPp0AbS2gpQSQwdcAYXQpc2MkbWCVWMRkAlY9B06uO0Ew6QJGPgOuCSAM1ALos=')).decode("utf-8")
        print(compressed_post_map.format(room[7], room[2], room[6], room[0], room[1], room[4], room[5], room[3]))    

    def encode(self, data):
        return b64encode(compress(data.encode("utf-8")))

    def decode(self, data):
        return decompress(b64decode(data)).decode("utf-8")