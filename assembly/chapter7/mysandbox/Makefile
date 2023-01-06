mysandbox: mysandbox.o
	ld -m elf_i386 -o mysandbox mysandbox.o
mysandbox.o: mysandbox.asm
	nasm -f elf -g -F stabs mysandbox.asm -l mysandbox.lst
