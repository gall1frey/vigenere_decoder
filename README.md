# Vigenere Cipher and Decoder
The Vigenere cipher decoder can be used to encrypt any text using the Vigenere cipher, and also decrypt it.

The script, along with being able to use the key to decrypt ciphertext, also works without the knowledge of a key, provided the ciphertext is long enough.

## Requirements
```
1. python3.x
2. the math module in python3
```

## Installation
In case you don't have a python installation, you can install it using:
1. Linux:
  ```
  sudo apt-get install python3 python3-pip
  ```
2. Windows:
Head over to https://www.python.org/downloads/windows/ and follow the instructions there.

The math module should be available once you've got a python installation.

## Use
### Importing into other scripts
The Vigenere class from this script can be imported into any other script you're writing provided this script and your script are in the same directory. From there, importing works like:
```python
from vigenere import Vigenere
```

### Encryption
First, create an object of the Vigenere class, then set the plaintext and key
```python
v = Vigenere()
v.set_pt('PLAINTEXT TO ENCRYPT')
v.set_key('KEY')
```
Next, call the ```encode()``` method. This returns the encrypted text
```python
v.encode()
```
The whole process:
```python
from vigenere import Vigenere
v = Vigenere()
v.set_pt('PLAINTEXT TO ENCRYPT')
v.set_key('KEY')
v.encode()
>>> ZPYSRROBRDSCXGPITR
```

### Decryption with key
First, create an object of the Vigenere class, then set the ciphertext and key
```python
v = Vigenere()
v.set_ct('ZPYSRROBRDSCXGPITR')
v.set_key('KEY')
```
Next, call the ```decode()``` method. This returns the encrypted text
```python
v.decode()
```
The whole process:
```python
from vigenere import Vigenere
v = Vigenere()
v.set_ct('ZPYSRROBRDSCXGPITR')
v.set_key('KEY')
v.decode()
>>> PLAINTEXTTOENCRYPT
```

### Decryption without key
First, create an object of the Vigenere class, then set the ciphertext
```python
v = Vigenere()
v.set_ct('ZPYSRROBRDSCXGPITR') #The ciphertext needs to be quite long here
```
Next, call the ```decode_no_key()``` method. This returns the encrypted text
```python
v.decode_no_key()
```
The whole process:
```python
from vigenere import Vigenere
v = Vigenere()
v.set_ct('ZPYSRROBRDSCXGPITR')
v.decode_no_key()
>>> PLAINTEXTTOENCRYPT
```

### Custom alphabet
The class allows for encryption and decryption of the vigenere cipher in custom alphabets. To provide your own alphabet, the ```set_alpha()``` method must be called with a string containing the alphabet as argument.

Say a custom alphabet consists of the letters A, B and C. To set this alphabet:
```python
v.set_alpha('ABC')
```

**NOTE:** *In case key-less decryption needs to be performed on a custom alphabet, a dictionary of ```{letter:frequency}``` also must be provided.*
```python
v.set_alpha('ABC')
v.set_freq({'A':0.49,'B':0.21,'C':0.30})
```
