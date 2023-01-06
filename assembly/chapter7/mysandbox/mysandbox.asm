section .data
section .text

	global _start

_start:
		nop
		mov eax,0FFFFFFFFh
		mov ebx,03B72h
		mul ebx
		nop

section .bss
