import sys

def main():
    if len(sys.argv) > 1:
        print(sys.argv[:6])

if __name__ == "__main__":
    main()