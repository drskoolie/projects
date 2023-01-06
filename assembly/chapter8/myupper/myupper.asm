SECTION .bss
	Buff resb 1

SECTION .data

SECTION .text
	global _start

_start:
		nop				; Keep our capricious debugger happy

Read:	mov eax,3		; Specify sys_read call
		mov ebx,0		; Specify File Descriptor 0: Standard Input
