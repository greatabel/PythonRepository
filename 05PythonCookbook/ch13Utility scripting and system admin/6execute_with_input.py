import subprocess

text = b'''
This is a test.
Hello World!
Abel'''

p = subprocess.Popen(['wc'],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)

stdout, stderr = p.communicate(text)

# To interpret as text, decode
if stdout is not None:
    out = stdout.decode('utf-8')
    print('#'*10,'\n')
    print(out)
if stderr is not None:
    err = stderr.decode('utf-8')
