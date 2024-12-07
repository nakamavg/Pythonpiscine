import argparse
import sys

def main():
    # Crear el parser
    parser = argparse.ArgumentParser(description="this script checks if a number is even or odd")
    
    # Agregar un argumento posicional obligatorio
    parser.add_argument(
        "number", 
        type=int, 
        help="the number to check"
    )
    
    # Parsear los argumentos
    args = parser.parse_args()
    
    # Verificar que hay exactamente un argumento (además del nombre del script)
    if len(sys.argv) != 2:
        print("Error: only one argument is allowed.")
        sys.exit(1)
    
    # Determinar si es par o impar
    if args.number % 2 == 0:
        print(f"{args.number} is even.")
    else:
        print(f"{args.number} is odd.")

if __name__ == "__main__":
    main()
