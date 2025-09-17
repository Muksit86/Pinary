import re
import argparse
import subprocess


class Compiler:
    #Constructer
    def __init__(self, pi_file):
        self.pi_file = pi_file
        self.read_a_file()
        self.compilation()
        self.write_output()

    #Reading a .pi file
    def read_a_file(self):
        with open(self.pi_file, 'r') as file:
            return file.read()
        
    def compilation(self):
        #Converting the .pi code into tokens [Example: pi ip ip ip ip ip pi -> ['pi', 'ip', 'ip', 'ip', 'ip', 'ip', 'pi']]
        tokens = re.findall(r'\b(pi|ip)\b', self.read_a_file(), re.IGNORECASE)
        
        #Converting the tokens in bits [Example: ['pi', 'ip', 'ip', 'ip', 'ip', 'ip', 'pi'] -> 1000001]
        bits = ''.join('0' if t.lower() == 'pi' else '1' for t in tokens)

        #Cheaking if bits are length of 8 or not. If not then raise Syntax Error
        if len(bits) % 8 != 0:
            raise ValueError("Syntax Error: Bitstream length is not a multiple of 8")
        
        #Converting the bits into decimal number [Example: 1000001 -> [65]]
        bytes_value = [int(bits[i: i+8], 2) for i in range(0, len(bits), 8)]

        #Converting the bytes into raw byte value [Example: 65 -> b'A']
        return bytes(bytes_value)

    def file_name_extractor(self):
        f, ext = self.pi_file.split('.')
        return f

    #Writting a decoded text into file with .py extentsion
    def write_output(self):
        with open(f'{self.file_name_extractor()}.py', 'w') as file2:
            file2.write(self.compilation().decode('utf-8'))

class Run:
    def __init__(self, file_name):
        subprocess.run(["python", file_name])

class Main(Compiler, Run):
    def __init__(self):
        self.create_args()
        self.perfom_args()

    def create_args(self):
        parser = argparse.ArgumentParser(description='A program that compiles and run .pi files')

        # positional argument: the filename
        parser.add_argument("filename", type=str, help="Must provide name of the .pi file.")

        #option flag
        parser.add_argument("--compile", action='store_true', help='Compiles the .pi file')
        parser.add_argument("--run", action='store_true', help='Runs the .pi file')

        #creating the arguments
        args = parser.parse_args()
        return args

    def perfom_args(self):
        args = self.create_args()
        if args.compile:
            compile = Compiler(args.filename)
            compile
        elif args.run:
            run = Run('test.py')
            run
            print("Running")
        else:
            print("Invalid action")

main = Main()
main








# def file_read():
#     with open('test.py', 'r') as file:
#         py_text = file.read()
#     return py_text

# b = file_read().encode('utf-8')

# bits = ''.join(f"{byte:08b}" for byte in b)

# tokens = ['pi' if bit == '0' else 'ip' for bit in bits]

# grouped = [' '.join(tokens[i:i+8]) for i in range(0, len(tokens), 8)]
# code = ' '.join(grouped)

# with open('test.pi', 'w') as file2:
#     file2.write(code)