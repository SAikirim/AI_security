.586
.model flat,stdcall
option casemap:none

.code
main proc
    push ebp		//
    mov ebp,esp		//함수 프롤로그 : 함수 초기화
    sub esp,8h		//

    mov dword ptr [ebp-4], 22334455h		//메모리 주소에 접근할 때는 []를 사용
    mov dword ptr [ebp-8], 00000000h

    mov esi,dword ptr [ebp-4]
    mov edi,dword ptr [ebp-8]

    mov esp,ebp		//
    pop ebp		//함수 종료 및 복귀 에필로그
    retn		//

main endp
end main