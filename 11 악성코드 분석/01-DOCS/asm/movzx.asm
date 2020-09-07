.586
.model flat,stdcall
option casemap:none

.code
main proc
    push ebp
    mov ebp,esp
    sub esp,4h

    mov dword ptr [ebp-4h],0000ffffh

    mov bx, word ptr [ebp-4h]

    movzx eax,bx
    
    mov esp,ebp
    pop ebp
    retn
    
main endp
end main