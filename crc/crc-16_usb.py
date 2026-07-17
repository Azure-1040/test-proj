import argparse

MODEL = r"CRC-16/USB"
WIDTH = 16
POLY = 0x8005
INIT = 0xFFFF
REFIN = True
REFOUT = True
XOROUT = 0xFFFF

def reverse_bits(din: int, width: int) -> int:
    dout = 0
    for i in range(width):
        dout = dout << 1 | din >> i & 0x1
    return dout

def crc16(din_list: list) -> None:
    crc = INIT
    ref_poly = reverse_bits(POLY, WIDTH)

    for din in din_list:
        crc = crc ^ din & 0xFF
        for _ in range(8):
            if crc & 0x1:
                crc = crc >> 1 ^ ref_poly
            else:
                crc = crc >> 1
    crc = crc ^ XOROUT

    print(f"Input Data = {" ".join(f"0x{i & 0xFF:02X}" for i in din_list)}, CRC = 0x{crc:04X}")

def main() -> None:
    parser = argparse.ArgumentParser(description = f"{MODEL} Calculator")
    parser.add_argument("-i", "--input", nargs = "+", type = lambda s: int(s, 0), required = True, metavar = "DATA", help = "Input Data")
    args = parser.parse_args()

    crc16(args.input)

if __name__ == "__main__":
    main()
