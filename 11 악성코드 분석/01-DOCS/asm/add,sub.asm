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

        mov dword ptr [ebp-4h],00401FE3h
        mov eax,dword ptr [ebp-4h]

        add eax,1dh
        sub dword ptr[eax],1dh
        
        mov esp, ebp
        pop ebp
        retn

    main endp
    end main