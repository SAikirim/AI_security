.586
.model flat,stdcall
option casemap:none

.data
    message db "1234"

.code
    main proc
        push ebp
        mov ebp, esp
        
        mov eax,11223344h
        mov ebx,12345678h

        xor eax,ebx
        
        xor eax,ebx

        xor eax,eax

        mov esp, ebp
        pop ebp
        retn

    main endp
end main