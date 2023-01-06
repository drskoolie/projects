simple: simple.o
	ld -m elf_i386 -o simple simple.o
simple.o: simple.asm
	nasm -f elf -g -F stabs simple.asm
