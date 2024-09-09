from re import sub
from random import randint

def gerar_cpf():
    # gerar os primeiros 9 digitos
    cpf = [randint(0, 9) for _ in range(9)]

    # calcular e adicionar no cpf o 10º e 11º digitos
    for _ in range(2):
        cont = len(cpf) + 1
        digito = sum(d * (cont - i) for i, d in enumerate(cpf)) % 11
        
        cpf.append(11 - digito if digito > 1 else 0)
    
    # tirar qualquer caractere da antiga lista que não seja um número 
    # [0, 1, 2] --> 012
    cpf_num = sub(
        r'[^0-9]',
        '',
        str(cpf)
    )

    return cpf_num

print('''
==================================
||        Gerador de CPF        ||
==================================
''')

while True:
    cpf = gerar_cpf()

    # verificar se o cpf é sequencial
    if cpf[0] * 11 == cpf:
        continue

    # formatar o cpf
    # 12345678901 --> 123.456.789-01
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    print(f'CPF Válido gerado: {cpf}\n' + '=' * 34) 
    
    break