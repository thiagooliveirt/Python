# Função para calcular a média ponderada
def calcular_media(ad, ap):
    return ((ad * 4) + (ap * 6)) / 10

# Função para verificar a situação do aluno
def verificar_situacao(media):
    if media >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'

# Entrada das notas e cálculo das médias
ad1 = float(input('Digite sua nota de AD1: '))
ap1 = float(input('Digite sua nota de AP1: '))
n1 = calcular_media(ad1, ap1)

ad2 = float(input('Digite sua nota de AD2: '))
ap2 = float(input('Digite sua nota de AP2: '))
n2 = calcular_media(ad2, ap2)

# Cálculo da média final
nota_final = (n1 + n2) / 2
print(f'Sua média final foi: {nota_final}')

# Verificação da situação do aluno
situacao = verificar_situacao(nota_final)

if situacao == 'Reprovado':
    maior_nota = max(n1, n2)
    ap3 = float(input('Digite sua nota de AP3: '))
    nota_recuperacao = calcular_media(ap3, maior_nota)
    
    if nota_recuperacao >= 5:
        situacao = f'Aprovado com média de recuperação: {nota_recuperacao}'
    else:
        situacao = 'Reprovado'

print(situacao)
