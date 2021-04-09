from ctypes import cdll
import subprocess
from Crypto.Cipher import AES

start_time = int(subprocess.check_output(['date', '-d', "2018-04-17 20:08:49", '+%s']).decode())
prng = cdll.LoadLibrary("./libprng.so").key_gen
iv = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")
pt = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
ct = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")

def check(key:bytes):
    encrypt = AES.new(key=key, mode=AES.MODE_CBC, iv=iv).encrypt
    return ct == encrypt(pt)

def main():
    duration = 24 * 3600
    print("[start]")
    for t in range(start_time, start_time + duration):
        key = b"0"*16
        prng(key, t)
        if check(key):
            print(f"found key:{key.hex()}")
    print("[end]")

if __name__ == "__main__":
    seed_lab_time_zone = 1523977729
    my_time_zone = int(subprocess.check_output(['date', '-d', "2018-04-17 23:08:49", '+%s']).decode())
    start_time = start_time + (seed_lab_time_zone - my_time_zone)
    main()