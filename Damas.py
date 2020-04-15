  #Damas Project - O retorno

#Cria o tabuleiro
def criar_tabuleiro():
  numero_linha = -1

  Tabuleiro = [[' ']*23 for i in range(23)]

  linha_separadora = [' ','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+',' ']

  nome_coluna = [' ',' ','A',' ','B',' ','C',' ','D',' ','E',' ','F',' ','G',' ','H',' ','I',' ','J',' ',' ']

  for linha in range(23):

    #Atribui a primeira e última linha com as letras das Colunas
    if linha == 0 or linha == 22: 
      Tabuleiro[linha] = nome_coluna 
  
    #Atribui as linhas de +-+- no tabuleiro e soma 1 no número da linha
    if linha%2 != 0:
      Tabuleiro[linha] = linha_separadora
      numero_linha += 1


    for coluna in range(23):

      if linha%2 == 0 and linha > 0 and linha <= 21:
        
        #Coloca os números das linhas 
        if coluna == 0 or coluna == 22:
          Tabuleiro[linha][coluna] = str(numero_linha)

        #Coloca os elementos '|' no tabuleiro
        else:
          if coluna%2 != 0:
            Tabuleiro[linha][coluna] = '|'

          else:
            if numero_linha%2 == 0:
              
              #Coloca os elementos '#' no tabuleiro
              if coluna%2 == 0 and coluna%4 != 0:
                Tabuleiro[linha][coluna] = '#'

              #Coloca as peças 'o' e '@' no tabuleiro nas linhas pares
              else:
                if numero_linha < 3:
                  Tabuleiro[linha][coluna] = 'o'
                if numero_linha > 6:
                  Tabuleiro[linha][coluna] = '@'

            else:
              
              #Coloca os elementos # no tabuleiro
              if coluna%4 == 0:
                Tabuleiro[linha][coluna] = '#'

              #Coloca as peças 'o' e '@' no tabuleiro nas linhas impares
              else:
                if numero_linha < 3:
                  Tabuleiro[linha][coluna] = 'o'
                if numero_linha > 6:
                  Tabuleiro[linha][coluna] = '@'

  return Tabuleiro

#Imprime o tabuleiro
def imprimir_tabuleiro(matriz):
  print('\n')
  for i in range(23):
    print(''.join(matriz[i]))

#Move a peça e retorna True, caso o movimento seja inválido, retorna False
def movimento_peça(Jogador,movimento,matriz):
  
  global Peças_obtidas0
  global Peças_obtidas1
  
  if len(movimento) < 6:
    return False

  else:
    posição_peça_atual = verificar_posição_atual(movimento[0],movimento[1],matriz)
    posição_peça_desejada = verificar_posição_desejada(movimento[4],movimento[5],matriz)

    if posição_peça_atual != False and posição_peça_desejada != False:
      #Movimento da peça (o)
      if Jogador%2 == 0:
        #Movimento de uma peça normal (o) sem capturar peça:
        if posição_peça_desejada[0] == posição_peça_atual[0]+2 and matriz[posição_peça_atual[0]][posição_peça_atual[1]] == "o":

          #Esquerda ou Direita:
          if posição_peça_desejada[1] == posição_peça_atual[1]+2 or posição_peça_desejada[1] == posição_peça_atual[1]-2:
            matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
            matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "o"
            return True

        #Movimento de uma peça normal (o) capturando peça (Para trás ou para frente):
        elif (posição_peça_desejada[0] == posição_peça_atual[0]+4 or posição_peça_desejada[0] == posição_peça_atual[0]-4) and matriz[posição_peça_atual[0]][posição_peça_atual[1]] == "o":

          #Direita:
          if posição_peça_desejada[1] == posição_peça_atual[1]+4:
            if (matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] == "@" or matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] == "&") and matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] == matriz[posição_peça_desejada[0]-2][posição_peça_desejada[1]-2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "o"
              Peças_obtidas0 += 1
              return True

            elif (matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] == "@" or matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] == "&") and matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] == matriz[posição_peça_desejada[0]+2][posição_peça_desejada[1]-2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "o"
              Peças_obtidas0 += 1
              return True
            
            else:
              return False

          #Esquerda:
          elif posição_peça_desejada[1] == posição_peça_atual[1]-4:

            if (matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] == "@" or matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] == "&") and matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] == matriz[posição_peça_desejada[0]+2][posição_peça_desejada[1]+2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "o"
              Peças_obtidas0 += 1
              return True

            elif (matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] == "@" or matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] == "&") and matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] == matriz[posição_peça_desejada[0]-2][posição_peça_desejada[1]+2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "o"
              Peças_obtidas0 += 1
              return True
            
            else:
              return False

          else:
            return False

        #Movimento de uma dama (O) (Qualquer lugar)
        elif matriz[posição_peça_atual[0]][posição_peça_atual[1]] == "O":
          return mover_dama1(posição_peça_atual,posição_peça_desejada,matriz)

        else:
          return False

      #Movimento da peça (@)
      else:
        #Movimento de uma peça normal (@) sem capturar peça:
        if posição_peça_desejada[0] == posição_peça_atual[0]-2 and matriz[posição_peça_atual[0]][posição_peça_atual[1]] == "@":

          #Esquerda ou Direita:
          if posição_peça_desejada[1] == posição_peça_atual[1]+2 or posição_peça_desejada[1] == posição_peça_atual[1]-2:
            matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
            matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "@"
            return True

        #Movimento de uma peça normal (@) capturando peça (Para trás ou para frente):
        elif (posição_peça_desejada[0] == posição_peça_atual[0]+4 or posição_peça_desejada[0] == posição_peça_atual[0]-4) and matriz[posição_peça_atual[0]][posição_peça_atual[1]] == "@":

          #Direita (Pra frente ou pra trás):
          if posição_peça_desejada[1] == posição_peça_atual[1]+4:

            if (matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] == "o" or matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] == "O") and matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] == matriz[posição_peça_desejada[0]+2][posição_peça_desejada[1]-2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]-2][posição_peça_atual[1]+2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "@"
              Peças_obtidas1 += 1
              return True
            
            elif (matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] == "o" or matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] == "O") and matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] == matriz[posição_peça_desejada[0]-2][posição_peça_desejada[1]-2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]+2][posição_peça_atual[1]+2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "@"
              Peças_obtidas1 += 1
              return True
            
            else:
              return False

          #Esquerda (Pra frente ou pra trás):
          if posição_peça_desejada[1] == posição_peça_atual[1]-4:

            if (matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] == "o" or matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] == "O") and matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] == matriz[posição_peça_desejada[0]+2][posição_peça_desejada[1]+2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]-2][posição_peça_atual[1]-2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "@"
              Peças_obtidas1 += 1
              return True

            elif (matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] == "o" or matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] == "O") and matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] == matriz[posição_peça_desejada[0]-2][posição_peça_desejada[1]+2]:

              matriz[posição_peça_atual[0]][posição_peça_atual[1]] = " "
              matriz[posição_peça_atual[0]+2][posição_peça_atual[1]-2] = " "
              matriz[posição_peça_desejada[0]][posição_peça_desejada[1]] = "@"
              Peças_obtidas1 += 1
              return True
            
            else:
              return False


        #Movimento de uma dama(&) (Qualquer lugar)
        if matriz[posição_peça_atual[0]][posição_peça_atual[1]] == "&":
          return mover_dama2(posição_peça_atual,posição_peça_desejada,matriz)
    
  return False

#Verifica se alguma peça pode virar dama e põe a dama
def verificar_dama(matriz):
  for i in range(2,20,4):
    if matriz[2][i+2] == "@":
      matriz[2][i+2] = "&"
    if matriz[20][i] == "o":
      matriz[20][i] = "O"

#Mover uma dama (O), retorna True caso o movimento seja válido
def mover_dama1(posição_atual,posição_desejada,matriz):

  num_peças1 = 0
  local_peça1 = []
  aux = 2
  global Peças_obtidas0

  #Se o movimento for para direita (Para trás ou para frente): 
  if posição_desejada[1] > posição_atual[1]:

    #Para frente
    if posição_desejada[0] > posição_atual[0]:
        while posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]:

          #Verifica se há alguma peça adversária entre o caminho atual e desejado
          if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "&":
            num_peças1 += 1
            local_peça1 = [posição_atual[0]+aux,posição_atual[1]+aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
          if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "O" or num_peças1 > 1:
            return False

          if posição_atual[0]+aux > 20 or posição_atual[1]+aux > 20:
            return False

          aux += 2

    #Para Trás 
    elif posição_desejada[0] < posição_atual[0]:
      while posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]:

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "&":
          num_peças1 += 1
          local_peça1 = [posição_atual[0]-aux,posição_atual[1]+aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "O" or num_peças1 > 1:
          return False
        
        if posição_atual[0]-aux < 2 or posição_atual[1]+aux > 20 :
          return False
        
        aux += 2

    else:
        return False

    #Verificar se há e pode obter uma peça adversária
    if num_peças1 == 1:
      matriz[local_peça1[0]][local_peça1[1]] = " "
      Peças_obtidas0 += 1

    matriz[posição_atual[0]][posição_atual[1]] = " "
    matriz[posição_desejada[0]][posição_desejada[1]] = "O"
    return True

  #Se o movimento for para esquerda (Para trás ou para frente):
  elif posição_desejada[1] < posição_atual[1]:

    #Para frente
    if posição_desejada[0] > posição_atual[0]:
        while posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]:

          #Verifica se há alguma peça adversária entre o caminho atual e desejado
          if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "&":
            num_peças1 += 1
            local_peça1 = [posição_atual[0]+aux,posição_atual[1]-aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
          if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "O" or num_peças1 > 1:
            return False

          if posição_atual[0]+aux > 20 or posição_atual[1]-aux < 2:
            return False

          aux += 2

    #Para Trás
    elif posição_desejada[0] < posição_atual[0]:
        while posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]:

          #Verifica se há alguma peça adversária entre o caminho atual e desejado
          if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "&":
            num_peças1 += 1
            local_peça1 = [posição_atual[0]-aux,posição_atual[1]-aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
          if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "O" or num_peças1 > 1:
            return False

          if posição_atual[0]-aux < 2 or posição_atual[1]-aux < 2:
            return False

          aux += 2

    else:
        return False

      #Verificar se tinha alguma peça adversária obtida ou não
    if num_peças1 == 1:
      matriz[local_peça1[0]][local_peça1[1]] = " "
      Peças_obtidas0 += 1

    matriz[posição_atual[0]][posição_atual[1]] = " "
    matriz[posição_desejada[0]][posição_desejada[1]] = "O"
    return True
  else:
    return False

#Mover uma dama(&), retorna True caso o movimento seja válido
def mover_dama2(posição_atual,posição_desejada,matriz):

  num_peças2 = 0
  local_peça2 = []
  aux = 2
  global Peças_obtidas1

  #Se o movimento for para direita (Para trás ou para frente): 
  if posição_desejada[1] > posição_atual[1]:

    #Para Trás
    if posição_desejada[0] > posição_atual[0]:
      while posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]:

          #Verifica se há alguma peça adversária entre o caminho atual e desejado
          if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "O":
            num_peças2 += 1
            local_peça2 = [posição_atual[0]+aux,posição_atual[1]+aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
          if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "&" or num_peças2 > 1:
            return False

          if posição_atual[0]+aux > 20 or posição_atual[1]+aux > 20:
            return False

          aux += 2

    #Para Frente
    elif posição_desejada[0] < posição_atual[0]:
      while posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]:

          #Verifica se há alguma peça adversária entre o caminho atual e desejado
          if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "O":
            num_peças2 += 1
            local_peça2 = [posição_atual[0]-aux,posição_atual[1]+aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
          if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "&" or num_peças2 > 1:
            return False

          if posição_atual[0]-aux < 2 or posição_atual[1]+aux > 20:
            return False

          aux += 2

    else:
      return False

    #Verificar se tinha alguma peça adversária obtida ou não
    if num_peças2 == 1:
      matriz[local_peça2[0]][local_peça2[1]] = " "
      Peças_obtidas1 += 1

    matriz[posição_atual[0]][posição_atual[1]] = " "
    matriz[posição_desejada[0]][posição_desejada[1]] = "&"
    return True

  #Se o movimento for para esquerda (Para trás ou para frente):
  elif posição_desejada[1] < posição_atual[1]:

    #Para Trás
    if posição_desejada[0] > posição_atual[0]:
          while posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]:

            #Verifica se há alguma peça adversária entre o caminho atual e desejado
            if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "O":
              num_peças2 += 1
              local_peça2 = [posição_atual[0]+aux,posição_atual[1]-aux]

            #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
            if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "&" or num_peças2 > 1:
              return False

            if posição_atual[0]+aux > 20 or posição_atual[1]-aux < 2:
              return False

            aux += 2
        
    #Para Frente
    elif posição_desejada[0] < posição_atual[0]:
      while posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]:

            #Verifica se há alguma peça adversária entre o caminho atual e desejado
            if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "O":
              num_peças2 += 1
              local_peça2 = [posição_atual[0]-aux,posição_atual[1]-aux]

            #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
            if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "&" or num_peças2 > 1:
              return False

            if posição_atual[0]-aux < 2 or posição_atual[1]-aux < 2:
              return False

            aux += 2

    else:
      return False

    #Verificar se tinha alguma peça adversária obtida ou não
    if num_peças2 == 1:
      matriz[local_peça2[0]][local_peça2[1]] = " "
      Peças_obtidas1 += 1

    matriz[posição_atual[0]][posição_atual[1]] = " "
    matriz[posição_desejada[0]][posição_desejada[1]] = "&"
    return True
  
  else:
    return False

#Verifica e retorna a posição da peça atual se existir
def verificar_posição_atual(coluna_atual,linha_atual,matriz):

  coluna = 2
  linha = 2

  while matriz[0][coluna] != coluna_atual and coluna < 21:
    coluna += 2
  while matriz[linha][0] != linha_atual and linha < 21:
    linha += 2
    
  posição =[linha,coluna]

  if matriz[linha][coluna] == "o" or matriz[linha][coluna] == "O" or matriz[linha][coluna] == "@" or matriz[linha][coluna] == "&":
    return posição

  else:
    return False

#Verifica se existe um espaço vazio válido na posição desejada,se sim, retorna a posição
def verificar_posição_desejada(coluna_desejada,linha_desejada,matriz):

  coluna = 2
  linha = 2

  #Percorre a primeira coluna da primeira linha
  while matriz[0][coluna] != coluna_desejada and coluna < 21:
    coluna += 2

  #Perocrre a primeira linha da primeira coluna
  while matriz[linha][0] != linha_desejada and linha < 21:
    linha += 2

  posição = [linha,coluna]
  #Verifica se a posição da linha e coluna percorrida é valida
  if matriz[linha][coluna] == " " and coluna < 21 and linha < 21:
    return posição
  else:
    return False
    
Recomeçar = "S"

while Recomeçar == "S":
  Peças_obtidas1 = 0
  Peças_obtidas0 = 0
  Vencedor = False
  
  Tabuleiro = criar_tabuleiro()

  print("Bem vindo ao jogo de Damas!")
  Jogador = input("Para começar, digite qual peça você quer ser (@ ou o): ")

  #Verificar se a peça digitada é válida
  while Jogador != "@" and Jogador != "o":
    Jogador = input("Peça inválida! Digite novamente (@ ou o): ")


  #Troca o simbolo da peça digitada para número
  if Jogador == "@":
    Jogador = 1
  if Jogador == "o":
    Jogador = 0

  while Vencedor == False:

    if Jogador%2 == 0:
      print("\nÉ a vez do jogador de cima (o)!")
    else:
      print("\nÉ a vez do jogador de baixo (@)!")
    
    imprimir_tabuleiro(Tabuleiro)
    print("\nPeças obtidas pelo Jogador 0 (o/O) = %d" % Peças_obtidas0)
    print("Peças obtidas pelo Jogador 1 (@/&) = %d\n" % Peças_obtidas1)

    movimento = input("Digite o local da sua peça e para onde deseja mover conforme o exemplo (Ex: A7--B6): ")
    mover_peça = movimento_peça(Jogador,movimento,Tabuleiro)

    #Verificar se o movimento foi válido
    while mover_peça == False :
      movimento = input("\nJogada inválida, digite um movimento válido (Ex: A7--B6): ")
      mover_peça = movimento_peça(Jogador,movimento,Tabuleiro)

    #Verifica se todas as peças de alguem foram obtidas (Vencedor)
    if Peças_obtidas0 == 15 or Peças_obtidas1 == 15:
      Vencedor = True
      imprimir_tabuleiro(Tabuleiro)
      if Peças_obtidas1 == 15:
        print("\nParabéns jogador das peças (@/&), você ganhou!")
      else:
        print("\nParabéns jogador das peças (o/O), você ganhou!")
      
    if Vencedor == True:
      Recomeçar = input("\nDeseja jogar novamente a partida? digite (S) para sim e (N) para não: ")
      print("\n\n")

    verificar_dama(Tabuleiro)
    Jogador += 1
