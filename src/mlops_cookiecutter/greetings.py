import argparse

def main():
    parser = argparse.ArgumentParser(description="Print 'Hello World' multiple times.")
    parser.add_argument('--count', type=int, default=1, help='Number of times to print the message')
    args = parser.parse_args()

    for _ in range(args.count):
        print("Hello World")

if __name__ == "__main__":
    main()