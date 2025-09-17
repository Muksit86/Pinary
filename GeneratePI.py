import os

input_file = r'Examples\HelloPinary.py'

def file_read():
    with open(input_file, 'r') as file:
        py_text = file.read()
    return py_text


b = file_read().encode('utf-8')

bits = ''.join(f"{byte:08b}" for byte in b)

tokens = ['pi' if bit == '0' else 'ip' for bit in bits]

grouped = [' '.join(tokens[i:i+8]) for i in range(0, len(tokens), 8)]
code = ' '.join(grouped)


filename = os.path.basename(input_file) #Count.py
base, _ = os.path.splitext(filename) #Count, .pi
output_file = base + '.pi' #Count.pi


with open(output_file, 'w') as file2:
    file2.write(code)