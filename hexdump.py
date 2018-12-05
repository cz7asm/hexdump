# MIT License
# 
# Copyright (c) 2018 cz7asm
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def dump16(s, offset=0):
	if len(s) > 16: s = s[:16]

	asciipart = ''.join( [(c if c.isalnum() else '.') for c in s] )
	hexpart = ' '.join( [hex(ord(c))[2:].zfill(2) for c in s] )
	hexpart = hexpart.ljust(16*3)

	print '%08x  %s %s |%s|' % (offset, hexpart[:8*3], hexpart[8*3:], asciipart)

def hexdump(s):
	for i in range((len(s)+15)/16):
		pos = i*16
		dump16(s[pos:pos+16], pos)
		
def hexify(s):
    h = " ".join([hex(x)[2:].zfill(2) for x in bytearray(s)])
    return h

hexdump('All this is going to be hexdumped')
print hexify('abcdef')
