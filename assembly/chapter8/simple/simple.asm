; Description:	 The most basic hello world example written in assembly 
; 				 for 32-bit Linux
; 
;   Build using these commands:
; 	nasm -f elf -g -F stabs simple.asm
; 	ld -o simple simple.o


SECTION .data			; Section containing initialized data

EatMsg: db "Eat at Joe's",10
EatLen: equ $-EatMsg

SECTION .bss			; Section containing uninitialized data

SECTION .txt			; Section containing code

global _start			; Linker needs this to find the entry point!

_start:
		nop				; This no-op keeps gdb happy (see text)
		mov eax,4		; Specify sys_write syscall
		mov ebx,1		; Specify File Descriptor 1: Standard Output
		mov ecx,EatMsg	; Pass offset of the message
		mov edx,EatLen	; Pass the length of the message
		int 80H			; Make syscall to output the text to stdout

		mov eax,1		; Specify Exit syscall
		mov ebx,0		; Return a code of zero
		int 80H			; Make syscall to terminate the program
