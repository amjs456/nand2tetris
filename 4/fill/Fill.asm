// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.



(MAINLOOP)
@n
M=0

(LOOP)
@n
D=M
@8192
D=D-A
@MAINLOOP
D;JEQ


@KBD
D=M
@BLACK
D;JGT
@WHITE
D;JEQ
0;JMP



(BLACK)
@SCREEN
D=A
@n
A=D+M
M=-1
@NEXT
0;JMP

(WHITE)
@SCREEN
D=A
@n
A=D+M
M=0


(NEXT)
@n
M=M+1
@LOOP
0;JMP