.586
.model flat,stdcall
option casemap:none

.data
    message db "1234"

.code
    main proc
        push ebp
        mov ebp, esp
        sub esp,8h

        mov dword ptr [ebp-4h], 10h
        mov dword ptr [ebp-8h], 20h

        mov eax, dword ptr [ebp-4h]
        mov ebx, dword ptr [ebp-8h]
        
        :반복문 실행(실제 실행할 땐 없앨 것)
        start:
            inc eax
            cmp eax,ebx
            je Exit
            ja Exit     
            
            jmp start
        Exit:
            pop ebp
            retn

    main endp
    end main