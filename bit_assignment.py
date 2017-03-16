import sys
import re
import binascii


def write_file(input_file_path, output_file_path):
    with open("\Python27\data.txt") as f, open(output_file_path, 'w') as fout:
        for line in f:
            if line.strip():
                binary_string = bin(int(binascii.hexlify(line.strip()), 16))
                bit_stuffed = re.sub('11111', '111110', binary_string)
                fout.write(bit_stuffed+'\n')
            else:
                fout.write(line+'\n')


def read_file(input_file_path, output_file_path):
    with open("bit_stuffed.txt", 'rb') as f, open(output_file_path, 'w') as fout:
        orig = ''
        for line in f:
            if line.strip():
                bit_unstuffed = re.sub('111110', '11111', line.strip())
                n = int(bit_unstuffed, 2)
                orig = binascii.unhexlify('%x' % n)
                fout.write(orig)
            else:
                fout.write(line)


def main():
    write_file(sys.argv[0], "bit_stuffed.txt")
    read_file("bit_stuffed.txt", "restored.txt")

if __name__ == "__main__":
    main()
