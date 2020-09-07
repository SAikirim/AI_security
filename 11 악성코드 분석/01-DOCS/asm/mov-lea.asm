.586
.model flat,stdcall
option casemap:none

.data
    message db "1234"

.code
    main proc
        push ebp
        mov ebp, esp
        sub esp,4h

        mov dword ptr [ebp-4h], 00402000h
        mov eax, dword ptr [ebp-4h]

        lea ecx, dword ptr [ebp-4h]

        mov ebx,[eax]
        mov edx,[ecx]

        mov esp,ebp
        pop ebp
        retn
        
    main endp
    end main