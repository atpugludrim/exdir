	.file	"rosetta.c"
# GNU C17 (Ubuntu 11.3.0-1ubuntu1~22.04) version 11.3.0 (x86_64-linux-gnu)
#	compiled by GNU C version 11.3.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version isl-0.24-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed: -mtune=generic -march=x86-64 -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
	.text
	.globl	returny_func
	.type	returny_func, @function
returny_func:
.LFB0:
	.cfi_startproc
	endbr64	
	pushq	%rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp	#,
	.cfi_def_cfa_register 6
	movq	%rdi, -8(%rbp)	# a, a
	movl	%edx, %eax	# c, tmp88
	movl	%ecx, -20(%rbp)	# d, d
	movl	%esi, %edx	# tmp86, tmp87
	movb	%dl, -12(%rbp)	# tmp87, b
	movw	%ax, -16(%rbp)	# tmp89, c
# rosetta.c:6:     return b+c;
	movsbl	-12(%rbp), %edx	# b, _1
	movswl	-16(%rbp), %eax	# c, _2
	addl	%edx, %eax	# _1, _5
# rosetta.c:7: }
	popq	%rbp	#
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE0:
	.size	returny_func, .-returny_func
	.section	.rodata
.LC0:
	.string	"done:)\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	endbr64	
	pushq	%rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp	#,
	.cfi_def_cfa_register 6
	subq	$64, %rsp	#,
	movl	%edi, -52(%rbp)	# argc, argc
	movq	%rsi, -64(%rbp)	# argv, argv
# rosetta.c:8: int main(int argc, char* argv[]){
	movq	%fs:40, %rax	# MEM[(<address-space-1> long unsigned int *)40B], tmp91
	movq	%rax, -8(%rbp)	# tmp91, D.2983
	xorl	%eax, %eax	# tmp91
# rosetta.c:9:     long long mylong = 0xbabecafef00dface;
	movabsq	$-4990328140781978930, %rax	#, tmp94
	movq	%rax, -24(%rbp)	# tmp94, mylong
# rosetta.c:10:     int myint = 0xdeadf00d;
	movl	$-559026163, -32(%rbp)	#, myint
# rosetta.c:11:     char str[] = "mystr";
	movl	$1953724781, -14(%rbp)	#, str
	movw	$114, -10(%rbp)	#, str
# rosetta.c:12:     int i = 1337;
	movl	$1337, -36(%rbp)	#, i
# rosetta.c:13:     while(i){
	jmp	.L4	#
.L5:
# rosetta.c:14:         i--;
	movl	-36(%rbp), %eax	# i, i.0_1
	subl	$1, %eax	#, _2
	movl	%eax, -36(%rbp)	# _2, i
.L4:
# rosetta.c:13:     while(i){
	movl	-36(%rbp), %eax	# i, i.1_3
	testl	%eax, %eax	# i.1_3
	jne	.L5	#,
# rosetta.c:16:     int ret = returny_func(&i, 0x42, 0x69, 0x31337);
	leaq	-36(%rbp), %rax	#, tmp87
	movl	$201527, %ecx	#,
	movl	$105, %edx	#,
	movl	$66, %esi	#,
	movq	%rax, %rdi	# tmp87,
	call	returny_func	#
	movl	%eax, -28(%rbp)	# tmp88, ret
# rosetta.c:17:     syscall(SYS_write, 1, "done:)\n", 7);
	movl	$7, %ecx	#,
	leaq	.LC0(%rip), %rax	#, tmp89
	movq	%rax, %rdx	# tmp89,
	movl	$1, %esi	#,
	movl	$1, %edi	#,
	movl	$0, %eax	#,
	call	syscall@PLT	#
# rosetta.c:18:     return 32;
	movl	$32, %eax	#, _13
# rosetta.c:19: }
	movq	-8(%rbp), %rdx	# D.2983, tmp92
	subq	%fs:40, %rdx	# MEM[(<address-space-1> long unsigned int *)40B], tmp92
	je	.L7	#,
	call	__stack_chk_fail@PLT	#
.L7:
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
