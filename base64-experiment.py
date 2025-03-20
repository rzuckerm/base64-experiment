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
                        if len(set(s_out)) == 4:
                            Base64.DECODE[s_out] = s_in

        self.decode_list = list(Base64.DECODE)
        random.shuffle(self.decode_list)
        self.decode_list_len = len(self.decode_list)
        self.encode_str = ""
        self.decode_str = ""

    def select_decode_chunk(self):
        n = 0
        candidates = {m: (-1, "") for m in range(4, 0, -1)}
        decode_set = set(self.decode_str)
        while n < self.decode_list_len:
            decode_chunk = self.decode_list[n]
            num_unique = len(set(decode_chunk) - decode_set)
            if num_unique == 0:
                self.decode_list_len -= 1
                self.decode_list[n] = self.decode_list[self.decode_list_len]
            else:
                if not candidates[num_unique][1]:
                    candidates[num_unique] = (n, decode_chunk)

                if num_unique == 4:
                    break

                n += 1

        for n, decode_chunk in candidates.values():
            if decode_chunk:
                self.decode_str += decode_chunk
                self.encode_str += Base64.DECODE[decode_chunk]
                self.decode_list_len -= 1
                self.decode_list[n] = self.decode_list[self.decode_list_len]
                break

    def select_encode_decode_string(self) -> tuple[str, str]:
        num_unique = 0
        while num_unique < 64:
            if self.select_decode_chunk():
                break

            num_unique = len(set(self.decode_str))

        return self.encode_str, self.decode_str


def show_results(best_encode_str: str, best_decode_str: str):
    print()
    print(f"best input:  {len(best_encode_str):3d}: '{best_encode_str}'")
    print(f"best output: {len(best_decode_str):3d}: '{best_decode_str}'")


def main():
    num_passes = int(sys.argv[1]) if len(sys.argv[1]) >= 1 else 1000
    best_encode_str = ""
    best_decode_str = ""
    best_decode_len = -1
    for n in range(1, num_passes + 1):
        print(f"*** {n} of {num_passes} ***\r", end="", flush=True)
        encode_str, decode_str = Base64().select_encode_decode_string()
        decode_len = len(decode_str)
        if best_decode_len < 0 or decode_len < best_decode_len:
            best_decode_str = decode_str
            best_decode_len = decode_len
            best_encode_str = encode_str
            show_results(best_encode_str, best_decode_str)
            if best_decode_len == 64:
                break

    show_results(best_encode_str, best_decode_str)


if __name__ == "__main__":
    main()
