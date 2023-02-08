print( "PROJETO INDIVIDUAL 01 MÓDULO 02" )
print( "ANGÉLICA MONTEIRO" )
print ( "#" * 30 )
print("CADASTRO DE CANDIDATOS A COLABORADORES")
print ( "#" * 30 )

quantCandidatos = int(input("Informe a quantidade de candidatos a serem registrados: "))

candidato = ()
listaCandidatos = {}
list1 = {}
lCand = []


for i in range(quantCandidatos):
    
    numeroCandidato = int(input("Insira o número do candidato: "))
    nome = input ( "Insira o nome do candidato: " )
    cargo = input ( "Insira o cargo pretendido: " )
    print( "#" * 30 )

    entrevista = "e_"
    testeTeórico = "t_"
    testePrático = "p_"
    softSkill = "s_"
    avaliacoes = [entrevista, testePrático, testeTeórico, softSkill]
    
    en = int(input( "Insira a nota da entrevista: " ))
    tn = int(input ( "Insira a nota do teste teórico: " ))
    pn = int(input ( "Insira a nota do teste prático: " ))
    sn = int(input ( "Insira a nota da avaliação Soft Skill: "))
    

    valorNotas= [en, tn, pn, sn]
    notas = ["%s%s" % (entrevista, en),"%s%s" % (testeTeórico, tn),"%s%s" % (testePrático,pn),"%s%s" % (softSkill, sn)]
    candidato = [numeroCandidato," Nome: "and(nome), "Cargo pretendido:"and(cargo), "Avaliações: "and(notas)]

    def insereOutrasEtapas(novaAvaliacao):
        pergunta = input("Deseja inserir outra avaliação para este candidato? S/N")
        pergunta = pergunta.upper()
        
        while pergunta != "N":
            nomeAvaliacao = input("Digite o nome da avaliação: ")
            letra = input("Digite uma letra correspondente ao nome da avaliação: ")
            letra = letra.lower()
            avaliacao = int(input("Digite a nota: "))
            
            novaAvaliacao =("%s%s" % (letra, avaliacao))
            avaliacoes.append(letra)
            notas.append(novaAvaliacao)
            print(novaAvaliacao)
            print(candidato)

            break

    insereOutrasEtapas(candidato)
   
    listaCandidatos[numeroCandidato, nome, cargo] = [notas]
   
    while quantCandidatos:
        lCand.append(valorNotas)
        lCand.append(numeroCandidato)
        lCand.append(nome)
        lCand.append(cargo)
        break
    print(lCand)

    def buscandoCandidatos():
        
    
        buscaConjNotas = []
        resultBusca = []
    
    
        print("BUSCA DE CANDIDATOS POR NOTA MAIOR OU IGUAL")
            
        nEntrevista = input("Informe a nota da entrevista: ")
        nEntrevista =  valorNotas[0]
        nTeorico = input("Informe a nota do teste teórico: ")
        nTeorico = valorNotas[1]
        nPratico = input("Informe a nota do teste prático: ")
        nPratico = valorNotas[2]
        nSoft = input("Informe a nota do soft skill: ")
        nSoft = valorNotas[3]
        buscaConjNotas.append(nEntrevista)
        buscaConjNotas.append(nTeorico)
        buscaConjNotas.append(nPratico)
        buscaConjNotas.append(nSoft)

        for i in range(len(lCand)): 
             
            while buscaConjNotas <= lCand[0]:
                resultBusca.append(lCand)
                break 
            break     
    
        
        print(resultBusca)
    
        
print("#"*30)
print("Lista de todos os candidatos: ",listaCandidatos)
print("#"*30) 


buscandoCandidatos()
