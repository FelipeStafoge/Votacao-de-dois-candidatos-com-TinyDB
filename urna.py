from tinydb import TinyDB

db = TinyDB('db.json', indent=4)
votos = TinyDB('votos.json')

eleitor = {}
Candidato_A = {}
Candidato_B = {}
Candidato_A['ID'] = 1
Candidato_B['ID'] = 2
Candidato_A['Votos'] = 0
Candidato_B['Votos'] = 0
novoA = 0
novoB = 0


def linha():
    print('-' * 50)


def menu():
    print(f'1- Votar\n2- Ver eleitores\n3- Ver votação\n4- Zerar votos\n5- Sair')
    linha()
    while True:
        resp = int(input('O que deseja fazer? '))
        if 0 < resp <= 5:
            if resp == 1:
                votar()
            if resp == 2:
                lista()
            if resp == 3:
                votacao()
            if resp == 4:
                zerar_votos()
            if resp == 5:
                print('ENCERRANDO...')
                break
            break
        else:
            print('ERRO! Digite um número de 1 a 5!')


def lista():
    soma = 0
    for i in db.all():
        print(
            f'O eleitor {db.all()[soma]["nome"]} votou no {db.all()[soma]["votoID"]}: {db.all()[soma]["candidato"]}  | ',
            end='')
        soma += 1
    print()
    linha()
    menu()


def votar():
    cont = len(db.all()) + 1
    while True:
        global novoA, novoB
        eleitor['ID'] = cont
        eleitor['nome'] = str(input('Nome: '))
        while True:
            eleitor['votoID'] = int(input('Em quem deseja votar? (1/2): '))
            if eleitor['votoID'] == 1 or eleitor['votoID'] == 2:
                break
            else:
                print('ERRO! DIGITE APENAS 1 OU 2')
        if eleitor['votoID'] == 1:
            eleitor['candidato'] = 'Candidato A'
            novoA = votos.all()[0]['Votos'] + 1
            votos.update({'Votos': novoA}, doc_ids=[1])

        if eleitor['votoID'] == 2:
            eleitor['candidato'] = 'Candidato B'
            novoB = votos.all()[1]['Votos'] + 1
            votos.update({'Votos': novoB}, doc_ids=[2])
        db.insert(eleitor.copy())
        eleitor.clear()
        resp = str(input('Deseja continuar? (S/N) '))[0].upper()
        if resp == 'N':
            menu()
            break


def votacao():
    print(f'Candidato A tem {votos.all()[0]["Votos"]} votos | Candidato B tem {votos.all()[1]["Votos"]} votos')
    linha()
    menu()


def zerar_votos():
    votos.truncate()
    db.truncate()
    votos.insert(Candidato_A.copy())
    votos.insert(Candidato_B.copy())
    print('VOTOS ZERADOS!')
    menu()


if Candidato_A not in votos.all():
    votos.insert(Candidato_A.copy())
if Candidato_B not in votos.all():
    votos.insert(Candidato_B.copy())

menu()
