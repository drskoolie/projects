SECTION .bss
	Buff resb 1

SECTION .data

SECTION .text
	global _start

_start:
		nop						; Keep our capricious debugger happy

Read:	mov eax,3				; Specify sys_read call
		mov ebx,0				; Specify File Descriptor 0: Standard Input
		mov ecx,Buff			; Pass address of buffer to read to
		mov edx,1024			; Tell sys_read to read one char from stdin
		int 80H					; Call sys_read
		mov esi,eax				; Copy sys_read return value for safekeeping

		cmp eax,0				; Look at sys_read's return value in EAX
		je Exit					; Jump If Equal to 0 (0 means EOF) to Exit

		; --- Set up registers for the process buffer step
		mov ecx,esi				; Place the number of bytes read into ecx
		mov ebp,Buff			; Place the address of the buffer into ebp
		dec ebp					; Decrease it by one so we can use it as an offset
								; (Instead of a count)
Scan:
		cmp byte [ebp+ecx],61H	; Test input char against lowercase 'a'
		jb ScanEnd				; If below 'a' in ASCII chart, not lowercase
		cmp byte [ebp+ecx],7AH	; Test input char against lowercase 'z'
		ja ScanEnd				; If above 'z' in ASCII chart, not lowercase
								; --> At this point, the char is lowercase
		sub byte [ebp+ecx],20H

ScanEnd:
		dec ecx					; Decrement the number of bytes (ecx)
		jnz Scan				; If more characters, continue scanning
Write:
		mov eax,4				; Code for sys_write call
		mov ebx,1				; Specify File Descriptor 1: Standard Output
		mov ecx,Buff			; Pass address of the character to write
		mov edx,esi				; Pass number of chars to write (stored it in esi)
		int 80H					; Call sys_write
		jmp Read				; Go back to Read to get another character


Exit:	mov eax,1				; Code for Exit Systcall
		mov ebx,0				; Return a code of zero to Linux
		int 80H					; Make kernel call to exit program
