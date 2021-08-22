	.file	"helloworld.cpp"
	.section	.text$_ZNKSt5ctypeIcE8do_widenEc,"x"
	.linkonce discard
	.align 2
	.p2align 4,,15
	.globl	__ZNKSt5ctypeIcE8do_widenEc
	.def	__ZNKSt5ctypeIcE8do_widenEc;	.scl	2;	.type	32;	.endef
__ZNKSt5ctypeIcE8do_widenEc:
LFB1246:
	.cfi_startproc
	movzbl	4(%esp), %eax
	ret	$4
	.cfi_endproc
LFE1246:
	.text
	.p2align 4,,15
	.def	___tcf_0;	.scl	3;	.type	32;	.endef
___tcf_0:
LFB1926:
	.cfi_startproc
	movl	$__ZStL8__ioinit, %ecx
	jmp	__ZNSt8ios_base4InitD1Ev
	.cfi_endproc
LFE1926:
	.p2align 4,,15
	.globl	__Z10helloworldv
	.def	__Z10helloworldv;	.scl	2;	.type	32;	.endef
__Z10helloworldv:
LFB1490:
	.cfi_startproc
	pushl	%esi
	.cfi_def_cfa_offset 8
	.cfi_offset 6, -8
	pushl	%ebx
	.cfi_def_cfa_offset 12
	.cfi_offset 3, -12
	movl	$__ZSt4cout, %ecx
	subl	$20, %esp
	.cfi_def_cfa_offset 32
	movl	$10, (%esp)
	call	__ZNSo9_M_insertIlEERSoT_
	.cfi_def_cfa_offset 28
	movl	%eax, %esi
	movl	(%eax), %eax
	subl	$4, %esp
	.cfi_def_cfa_offset 32
	movl	-12(%eax), %eax
	movl	124(%esi,%eax), %ebx
	testl	%ebx, %ebx
	je	L11
	cmpb	$0, 28(%ebx)
	je	L5
	movsbl	39(%ebx), %eax
L6:
	movl	%esi, %ecx
	movl	%eax, (%esp)
	call	__ZNSo3putEc
	.cfi_def_cfa_offset 28
	subl	$4, %esp
	.cfi_def_cfa_offset 32
	movl	%eax, %ecx
	addl	$20, %esp
	.cfi_remember_state
	.cfi_def_cfa_offset 12
	popl	%ebx
	.cfi_restore 3
	.cfi_def_cfa_offset 8
	popl	%esi
	.cfi_restore 6
	.cfi_def_cfa_offset 4
	jmp	__ZNSo5flushEv
	.p2align 4,,10
L5:
	.cfi_restore_state
	movl	%ebx, %ecx
	call	__ZNKSt5ctypeIcE13_M_widen_initEv
	movl	(%ebx), %eax
	movl	24(%eax), %edx
	movl	$10, %eax
	cmpl	$__ZNKSt5ctypeIcE8do_widenEc, %edx
	je	L6
	movl	$10, (%esp)
	movl	%ebx, %ecx
	call	*%edx
	.cfi_def_cfa_offset 28
	subl	$4, %esp
	.cfi_def_cfa_offset 32
	movsbl	%al, %eax
	jmp	L6
L11:
	call	__ZSt16__throw_bad_castv
	.cfi_endproc
LFE1490:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "\0"
	.section	.text.startup,"x"
	.p2align 4,,15
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB1491:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$LC0, 4(%esp)
	movl	$0, (%esp)
	call	_setlocale
	movl	12(%ebp), %eax
	movl	%eax, _argv
	call	__Z10helloworldv
	xorl	%eax, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE1491:
	.p2align 4,,15
	.def	__GLOBAL__sub_I_argv;	.scl	3;	.type	32;	.endef
__GLOBAL__sub_I_argv:
LFB1927:
	.cfi_startproc
	subl	$28, %esp
	.cfi_def_cfa_offset 32
	movl	$__ZStL8__ioinit, %ecx
	call	__ZNSt8ios_base4InitC1Ev
	movl	$___tcf_0, (%esp)
	call	_atexit
	addl	$28, %esp
	.cfi_def_cfa_offset 4
	ret
	.cfi_endproc
LFE1927:
	.section	.ctors,"w"
	.align 4
	.long	__GLOBAL__sub_I_argv
	.globl	_argv
	.bss
	.align 4
_argv:
	.space 4
.lcomm __ZStL8__ioinit,1,1
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	__ZNSt8ios_base4InitD1Ev;	.scl	2;	.type	32;	.endef
	.def	__ZNSo9_M_insertIlEERSoT_;	.scl	2;	.type	32;	.endef
	.def	__ZNSo3putEc;	.scl	2;	.type	32;	.endef
	.def	__ZNSo5flushEv;	.scl	2;	.type	32;	.endef
	.def	__ZNKSt5ctypeIcE13_M_widen_initEv;	.scl	2;	.type	32;	.endef
	.def	__ZSt16__throw_bad_castv;	.scl	2;	.type	32;	.endef
	.def	_setlocale;	.scl	2;	.type	32;	.endef
	.def	__ZNSt8ios_base4InitC1Ev;	.scl	2;	.type	32;	.endef
	.def	_atexit;	.scl	2;	.type	32;	.endef
