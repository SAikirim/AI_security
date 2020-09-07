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

        mov edx, 0h
        mov eax, 81h
        mov ebx, 2h

        div ebx

        :음수 저장
        mov eax, -48h

        : CWD - AX의 부호 비트를 DX로 확장한다.        +인지 – 인지 dx에다써서 초기화
	: CBW - AL의 부호 비트를 AX로 확장하여 숫자의 부호를 보존합니다.
	: CDQ - EAX의 부호 비트를 EDX로 확장합니다.

        cwd

        mov cx, -5h

        idiv cx : idiv는 부호가 있는 나눗셈
        
        mov esp, ebp
        pop ebp
        retn

    main endp
    end main