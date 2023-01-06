SECTION .bss
	Buff resb 1

SECTION .data

SECTION .text
	global _start

_start:
		nop				; Keep our capricious debugger happy

Read:	mov eax,3		; Specify sys_read call
		mov ebx,0		; Specify File Descriptor 0: Standard Input
		mov ecx,Buff	; Pass address of buffer to read to
		mov edx,1		; Tell sys_read to read on char from stdin
		int 80H			; Call sys_read

		cmp eax,0		; Look at sys_read's return value in EAX
		je Exit			; Jump If Equal to 0 (0 means EOF) to Exit

		cmp byte [Buff],61H		; Test input char against lowercase 'a'
		jb Write				; If below 'a' in ASCII chart, not lowercase
		cmp byte [Buff],7AH		; Test input char against lowercase 'z'
		ja Write				; If above 'z' in ASCII chart, not lowercase
								; --> At this point, the char is lowercase
		sub byte [Buff],20H

Write:
		mov eax,4		; Code for sys_write call
		mov ebx,1		; Specify File Descriptor 1: Standard Output
		mov ecx,Buff	; Pass address of the character to write
		mov edx,1		; Pass number of chars to write
		int 80H			; Call sys_write
		jmp Read		; Go back to Read to get another character


Exit:	mov eax,1		; Code for Exit Systcall
		mov ebx,0		; Return a code of zero to Linux
		int 80H			; Make kernel call to exit program
