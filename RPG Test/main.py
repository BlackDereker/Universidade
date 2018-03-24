import os

# NOMES: BRUNO GODOI MACHADO / HENRIQUE DIAS

# Variavel para auxiliar a funcao eval()
my_conditional = False


# Metodo com o objetivo de ler o arquivo de texto e sua formatacao personalizada
def execScene(fileName):

    #Abrir o arquivo
    file = open(os.getcwd() + "/Historia/" + fileName, "r")

    # Possiveis escolhas
    escolhas = []

    # Condiconal para indicar quando comecar a ler as escolhas
    lerEscolhas = False;

    choiceIndex = 0

    # Ler a historia/descricao do arquivo
    for line in file:

        # Leia as linhas da historia
        if not lerEscolhas:
            # Se recebe uma linha vazia, pule
            if line.strip() == "":
                continue
            # Se recebe uma linha que comeca com '$', avalie a condicao
            elif line[0] == "$":
                if not eval(line[1:].strip()):
                    file.readline()
                continue
            # Se recebe uma linha que comeca com '#', execute o comando
            elif line[0] == "#":
                exec(line[1:].strip(), globals())
                continue
            # Se recebe uma linha que comeca com '%', comece a ler a escolhas possiveis
            elif line[0] == "%":
                lerEscolhas = True
                print("")
                continue
            print(line)
        # Leia as linhas das possiveis escolhas
        else:

            if line.strip() == "":
                continue
            elif line[0] == "$":
                if not eval(line[1:].strip()):
                    file.readline()
                    file.readline()
                    continue
                else:
                    continue

            choiceIndex += 1
            print(choiceIndex, ". " + line[2:].strip())

            nextFileLine = file.readline()
            escolhas.insert(int(line[0]) - 1, nextFileLine[0: len(nextFileLine) - 1])

    print("")

    # Fechar o arquivo depois de sua leitura
    file.close()

    if lerEscolhas:
        # Ler input
        escolha = 0
        while True:
            try:
                escolha = int(input("Escolha: "))
            except ValueError:
                continue
            if escolha > 0 and escolha <= len(escolhas):
              break

        # Pegar o arquivo correspondente com a escolha
        arquivo = escolhas[escolha - 1]

        print("=" * 100)

        # Se a escolha tiver um arquivo correspondente, executar a funcao denovo
        if not arquivo == "":
            execScene(arquivo)


execScene("setup.txt")
execScene("cela.txt")
