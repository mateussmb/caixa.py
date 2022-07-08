#FIZ ESSE NAS PRESSAS, ACHEI QUE O MODELO CORRETO ERA O COMENTADO NO FIM DESSE PROGRAMAA.

#Front
from datetime import datetime
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
horario = data_e_hora_atuais.strftime('%H:%M')
cores = {
    '': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'negrito': '\033[1;1m',
    'branco': '\033[1;37m'
}

def cor(txt='', cor=''):
    return f'{cores[cor]}{txt}{cores[""]}'

def divisas(tam=40):
    return '_' * tam

def titulo(texto):
    print(divisas())
    print('|', texto.center(38), '|')
    print(divisas())

#Front


#Validação
def leiaNumero(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite um número válido.', cor='vermelho'))
        except KeyboardInterrupt:
            print(cor(txt='ERRO: Usúario não digitou o valor.', cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor

#FimValidação

#Menu

def menu(*opcs):
    titulo('MENU PRINCIPAL')
    for n, item in enumerate(opcs, 1):
        print('|', f"{cor(txt=n, cor='amarelo') } - {cor(txt=item, cor='azul')}".ljust(54), '|')
    divisas()
    opc = leiaNumero(cor(txt='Digite a opção desejada: ', cor='magenta'))
    while opc not in range(1, len(opcs) + 1):
        if opc not in range(1, len(opcs) + 1):
            print(cor(txt='ERRO: Digite uma opção válida!!!', cor='vermelho'))
        opc = leiaNumero(cor(txt='Digite a opção desejada: ', cor='magenta'))
    return opc

#FIMMENU

def escolhabanco():
    numero_valido = False
    while numero_valido == False:
        bancos = [' ','INTER', 'BRADESCO', 'BRASIL', 'NUBANK']

        print('Bancos disponíveis: ', '\n1 - ',bancos[1],'\n2 - ',bancos[2],'\n3 - ',bancos[3],'\n4 - ',bancos[4])

        banco_escolhido = int((input('Digite o número do banco escolhido: ')))

        if banco_escolhido == 1 or banco_escolhido == 2 or banco_escolhido == 3 or banco_escolhido == 4:
            numero_valido = True
        else:
            numero_valido = False
            print(cor(txt='ERRO: Informe um número válido.', cor='vermelho'))

    print(cor('Banco Selecionado: ', cor='ciano'),cor(bancos[banco_escolhido], cor='amarelo' ))


def saque_valor():
    validacao = False
    if validacao == False:
        saque =  float(input('Digite o valor que deseja sacar: '))
        print('Deseja sacar R${saque}? (SIM / NAO')
        validacao_valor = input()
        if validacao_valor == 'NAO':
            validacao = False
        else:
            validacao = True


arquivo_diretorio_nome = './nomeEconta_log.txt'
arquivo_diretorio_banco = './banco_log.txt'
arquivo_diretorio_saque = './saque_log.txt'

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(cor(txt='ERRO: Não foi possivel ler o arquivo.', cor='vermelho'))
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{cor(txt=dado[0], cor='ciano'):<36}{cor(txt=dado[1], cor='ciano'):>2}")
    finally:
        a.close()


def escreveArquivo(arq, nome, conta):
    try:
        a = open(arq, 'at')
    except:
        print(cor(txt='ERRO: Não foi possivel abrir o arquivo.', cor='vermelho'))
    else:
        try:
            a.write(f'{nome};{conta}\n')
        except:
            print(cor(txt='ERRO: Nào foi possivel inserir os dados.', cor='vermelho'))
        else:
            print(f'Nome: {nome},conta: {conta}')
            a.close()



while True:
    escolha = menu('Nome e conta', 'Selecionar Banco', 'Sacar Valor')

    if escolha == 1:
        titulo(cor(txt='NOVO CADASTRO', cor='azul'))
        nome = str(input(cor(txt='Nome: ', cor='amarelo')))
        conta = float(input(cor(txt='conta: ', cor='amarelo')))
        escreveArquivo(arquivo_diretorio_nome, nome, conta)
    if escolha == 2:
        titulo(cor(txt='SELECIONAR BANCO', cor='azul'))
        escolhabanco()
        
    if escolha == 3:
        titulo(cor(txt='SACAR VALOR', cor='azul'))
        saque_valor()
    with open(arquivo_diretorio_saque, 'a') as arqui:
            arqui.write('\n-----------------------\n Saque: R${} \n Data: {}\n----------------------- \n          ---'.format(saque,data_e_hora_em_texto))
            print(cor(txt='Saque realizado com Sucesso.', cor='verde'))




