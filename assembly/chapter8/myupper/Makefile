myupper: myupper.o
	ld -m elf_i386 -o myupper myupper.o

myupper.o: myupper.asm
	nasm -f elf -g -F stabs myupper.asm -l myupper.lst
