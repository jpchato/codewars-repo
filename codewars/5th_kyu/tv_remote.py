'''
Hint
This Kata is an extension of the earlier ones in this series. Completing those first will make this task easier.

Background
My TV remote control has arrow buttons and an OK button.

I can use these to move a "cursor" on a logical screen keyboard to type words...

Keyboard
The screen "keyboard" layouts look like this

Keypad Mode 1 = alpha-numeric (lowercase)	Keypad Mode 3 = symbols
a	b	c	d	e	1	2	3
f	g	h	i	j	4	5	6
k	l	m	n	o	7	8	9
p	q	r	s	t	.	@	0
u	v	w	x	y	z	_	/
aA#	SP						
^	~	?	!	'	"	(	)
-	:	;	+	&	%	*	=
<	>	€	£	$	¥	¤	\
[	]	{	}	,	.	@	§
#	¿	¡				_	/
aA#	SP						
aA# is the SHIFT key. Pressing this key cycles through THREE keypad modes.
Mode 1 = alpha-numeric keypad with lowercase alpha (as depicted above)
Mode 2 = alpha-numeric keypad with UPPERCASE alpha
Mode 3 = symbolic keypad (as depicted above)
SP is the space character
The other (solid fill) keys in the bottom row have no function
Special Symbols
For your convenience, here are Unicode values for the less obvious symbols of the Mode 3 keypad

¡ = U-00A1	£ = U-00A3	¤ = U-00A4	¥ = U-00A5
§ = U-00A7	¿ = U-00BF	€ = U-20AC	
Kata task
How many button presses on my remote are required to type the given words?

Notes
The cursor always starts on the letter a (top left)
The inital keypad layout is Mode 1
Remember to also press OK to "accept" each letter
Take the shortest route from one letter to the next
The cursor wraps, so as it moves off one edge it will reappear on the opposite edge
Although the blank keys have no function, you may navigate through them if you want to
Spaces may occur anywhere in the words string
Do not press the SHIFT key until you need to. For example, with the word e.Z, the SHIFT change happens after the . is pressed (not before). In other words, do not try to optimize total key presses by pressing SHIFT early.
Example
words = Too Easy?

T => a-aA#-OK-U-V-W-X-Y-T-OK = 9
o => T-Y-X-W-V-U-aA#-OK-OK-a-b-c-d-e-j-o-OK = 16
o => o-OK = 1
space => o-n-m-l-q-v-SP-OK = 7
E => SP-aA#-OK-A-3-2-1--E-OK = 8
a => E-1-2-3-A-aA-OK-OK-a-OK = 9
s => a-b-c-d-i-n-s-OK = 7
y => s-x-y-OK = 3
? => y-x-w-v-u-aA#-OK-OK-^-~-?-OK = 11
Answer = 9 + 16 + 1 + 7 + 8 + 9 + 7 + 3 + 11 = 71
'''

def tv_remote(words):
    # Your code here!
    pass

tv_remote("Too Easy?")#, 71