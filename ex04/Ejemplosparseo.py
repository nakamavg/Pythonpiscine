# Ejemplo de parseo de argumentos en Python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("patata" ,type=int ,help="el tipo de dato")
args = parser.parse_args()
print(args.patata)