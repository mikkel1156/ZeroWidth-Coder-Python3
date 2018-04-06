import zw_coder, argparse
from argparse import RawTextHelpFormatter

if __name__ == '__main__':
    #   Setup the Argument Parser.
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-e", "--encode", help="encode a secret message\n--secret [required]\n--message [optional]", action="store_true")
    parser.add_argument("-d", "--decode", help="decode a secret message\n--secret [required]", action="store_true")
    parser.add_argument("-m", "--message", help="message to insert secret into")
    parser.add_argument("-s", "--secret", help="secret which is either to be encoded into a message, or contains a secret")
    args = parser.parse_args()

    if args.encode and args.decode:
        print("How about no?")
        exit()

    if args.encode:
        if args.secret is None:
            print("-s or --secret is required for this.")
            exit()
        print("Encoded: " + zw_coder.encode(args.secret, args.message))
        print("Note - If you did not specify a message, then you might have a hard time getting the encoded secret.")
    if args.decode:
        if args.secret is None:
            print("-s or --secret is required for this.")
            exit()
        print("Decoded: " + zw_coder.decode(args.secret))