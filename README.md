# ZeroWidth ⁠‌‍‌‌‍‍‌‍​‌‍‍‍‌‍‌‍​‌‍‍‌‌‌‍‍​‌‍‍‌‍‌‌‌​‌‌‍‌‌‌‌‌​‌‍‍‌‍‍‌‌​‌‍‍‌‍‍‍‍​‌‍‍‍‌‍‍‌​‌‍‍‌‌‍‌‍​‌‌‍‌‌‌‌‌​‌‌‍‍‍‍‌‌​‌‌‍‍‌‌‍‍​⁠Coder
A very simple script to encode/decode text into zero-width characters which will result in them being *"invisible"*. The repo also contains a small tool (`main.py`) to use the encoder/decoder from a CLI.

## Usage
```
usage: main.py [-h] [-e] [-d] [-m MSG] [-s SEC]

optional arguments:
  -h, --help         show this help message and exit
  -e, --encode       encode a secret message
                     --sec [required]
                     --msg [optional]
  -d, --decode       decode a secret message
                     --sec [required]
  -m MSG, --msg MSG  message to insert secret into
  -s SEC, --sec SEC  secret which is either to be encoded into a message, or contains a secret

```

## Code Example
```
import zw_coder

print("Encoded: " + zw_coder.encode("TOP-SECRET", "This does so not contain a secret..."))
print("Decoded: " + zw_coder.decode(encoded))
```
