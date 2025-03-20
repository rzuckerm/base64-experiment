from base64 import b64encode
import random
import sys


class Base64:
    DECODE = {}

    def __init__(self):
        if not Base64.DECODE:
            Base64.DECODE = {}
            for a in range(32, 127):
                ac = chr(a)
                for b in range(32, 127):
                    bc = chr(b)
                    for c in range(32, 127):
                        cc = chr(b)
                        s_in = ac + bc + cc
                        s_out = b64encode(s_in.encode("ascii")).decode("ascii")
                        if len(s_out) == 4:
                            Base64.DECODE[s_out] = s_in

        self.decode_list = list(Base64.DECODE)
        random.shuffle(self.decode_list)
        self.encode_str = ""
        self.decode_str = ""

    def select_decode_chunk(self, count: int) -> bool:
        for n, decode_chunk in enumerate(self.decode_list):
            if sum(c not in self.decode_str for c in decode_chunk) >= count:
                self.decode_str += decode_chunk
                self.encode_str += Base64.DECODE[decode_chunk]
                self.decode_list[n] = self.decode_list[-1]
                del self.decode_list[-1]
                return True

        return False

    def select_encode_decode_string(self) -> tuple[str, str]:
        num_unique = 0
        while num_unique < 64:
            for count in range(4, 0, -1):
                if self.select_decode_chunk(count):
                    break

            num_unique = len(set(self.decode_str))

        print(f"input:       {len(self.encode_str):3d}: '{self.encode_str}'")
        print(f"output:      {len(self.decode_str):3d}: '{self.decode_str}'")
        return self.encode_str, self.decode_str


def main():
    num_passes = int(sys.argv[1]) if len(sys.argv[1]) >= 1 else 1000
    best_encode_str = ""
    best_decode_str = ""
    best_decode_len = -1
    for n in range(1, num_passes + 1):
        print(f"*** {n} of {num_passes} ***")
        encode_str, decode_str = Base64().select_encode_decode_string()
        decode_len = len(decode_str)
        if best_decode_len < 0 or decode_len < best_decode_len:
            best_decode_str = decode_str
            best_decode_len = decode_len
            best_encode_str = encode_str
            best_encode_len = len(encode_str)

        print(f"best input:  {best_encode_len:3d}: '{best_encode_str}'")
        print(f"best output: {best_decode_len:3d}: '{best_decode_str}'")
        if best_decode_len == 64:
            break

if __name__ == "__main__":
    main()
