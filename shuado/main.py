import argparse

VERSION = "1.0.0"

def main():
    parser = argparse.ArgumentParser(description="Shudao")
    parser.add_argument("version", nargs='?', help="显示版本信息")
    
    args = parser.parse_args()
    
    if args.version == "version":
        print(f"shudao {VERSION}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
