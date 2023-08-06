import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process file and apply modifications')

    parser.add_argument('input_file', type=str, help='Path to the input HTML file in .txt format')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print('file found :^)')
    except FileNotFoundError:
        print('file not found :^(')
    except:
        print('error :^(')
