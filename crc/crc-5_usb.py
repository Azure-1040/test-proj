import argparse

MODEL = r"CRC-5/USB"
WIDTH = 5
POLY = 0x05
INIT = 0x1F
REFIN = True
REFOUT = True
XOROUT = 0x1F

def reverse_bits(din: int, width: int) -> int:
    dout = 0
    for i in range(width):
        dout = dout << 1 | din >> i & 0x1
    return dout

def crc5(din: int) -> None:
    crc = INIT
    ref_poly = reverse_bits(POLY, WIDTH)

    for i in range(11):
        if (crc ^ din >> i) & 0x1:
            crc = crc >> 1 ^ ref_poly
        else:
            crc = crc >> 1
    crc = crc ^ XOROUT

    print(f"Input Data = 0x{din & 0x3FF:03X}, CRC = 0x{crc:02X}")

def main() -> None:
    parser = argparse.ArgumentParser(description = f"{MODEL} Calculator")
    parser.add_argument("-i", "--input", type = lambda s: int(s, 0), required = True, metavar = "DATA", help = "Input Data")
    args = parser.parse_args()

    crc5(args.input)

if __name__ == "__main__":
    main()
