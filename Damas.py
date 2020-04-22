  #Damas v1.0

#Cria o tabuleiro
def criar_tabuleiro():
  numero_linha = -1

  Tabuleiro = [[' ']*23 for i in range(23)]

  linha_separadora = [' ','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+','-','+',' ']

  nome_coluna = [' ',' ','A',' ','B',' ','C',' ','D',' ','E',' ','F',' ','G',' ','H',' ','I',' ','J',' ',' ']

  for linha in range(23):

    #Atribui a primeira e última linha com as letras das colunas
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
              """else:
                if numero_linha < 3:
                  Tabuleiro[linha][coluna] = 'o'
                if numero_linha > 6:
                  Tabuleiro[linha][coluna] = '@'"""

            else:
              
              #Coloca os elementos # no tabuleiro
              if coluna%4 == 0:
                Tabuleiro[linha][coluna] = '#'

              #Coloca as peças 'o' e '@' no tabuleiro nas linhas impares
              """else:
                if numero_linha < 3:
                  Tabuleiro[linha][coluna] = 'o'
                if numero_linha > 6:
                  Tabuleiro[linha][coluna] = '@'"""
              
              Tabuleiro[10][8] = "&"
              Tabuleiro[12][10] = "@"
              Tabuleiro[6][12] = "o"
              Tabuleiro[6][4] = "o"
              Tabuleiro[2][16] = "o"

  return Tabuleiro

#Imprime o tabuleiro
def imprimir_tabuleiro(matriz):
  print('\n')
  for i in range(23):
    print(''.join(matriz[i]))

#Move ou captura uma peça e retorna True, caso o movimento seja inválido, retorna False
def movimento_peça(movimento,matriz):
  
  global Peças_obtidas0
  global Peças_obtidas1
  global Jogador

  #Verifica se o que foi digitado está de acordo com o exemplo mostrado
  if len(movimento) < 6 or movimento[2:4] != "--":
    return False

  else:
    posição_atual = verificar_posição_atual(movimento[0],movimento[1],matriz)
    posição_desejada = verificar_posição_desejada(movimento[4],movimento[5],matriz)

    if posição_atual != False and posição_desejada != False:
      #Movimento da peça (o)
      if Jogador%2 == 0:
        #Movimento de uma peça normal (o) sem capturar peça (Esquerda ou direita):
        if verificar_movimento(posição_atual,posição_desejada,"E/D","M","o",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "o"
          return True

        #Movimento de uma peça normal (o) capturando peça:
        #Direita p/ frente:
        elif verificar_movimento(posição_atual,posição_desejada,"DF","C","o",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]+2][posição_atual[1]+2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "o"
          Peças_obtidas0 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True

        #Direita p/ trás
        elif verificar_movimento(posição_atual,posição_desejada,"DT","C","o",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]-2][posição_atual[1]+2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "o"
          Peças_obtidas0 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True

        #Esquerda p/ trás:
        elif verificar_movimento(posição_atual,posição_desejada,"ET","C","o",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]-2][posição_atual[1]-2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "o"
          Peças_obtidas0 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True
        
        #Esquerda p/ frente:
        elif verificar_movimento(posição_atual,posição_desejada,"EF","C","o",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]+2][posição_atual[1]-2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "o"
          Peças_obtidas0 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True

        #Movimento de uma dama (O) (Qualquer lugar)
        elif matriz[posição_atual[0]][posição_atual[1]] == "O":
          move_dama1 = mover_dama0(posição_atual,posição_desejada,matriz)

          if move_dama1 == False:
            return False

          else:
            if move_dama1 != True:
              matriz[move_dama1[0]][move_dama1[1]] = " "
              Jogador -= 1
              Peças_obtidas0 += 1
              print("\nVocê obteve uma peça adversária! Jogue Novamente")
            
            matriz[posição_atual[0]][posição_atual[1]] = " "
            matriz[posição_desejada[0]][posição_desejada[1]] = "O"
            return True

        else:
          return False

      #Movimento da peça (@)
      else:
        #Movimento de uma peça normal (@) sem capturar peça:
        if verificar_movimento(posição_atual,posição_desejada,"E/D","M","@",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "@"
          return True

        #Movimento de uma peça normal (@) capturando peça:

        #Direita p/ Frente
        elif verificar_movimento(posição_atual,posição_desejada,"DF","C","@",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]-2][posição_atual[1]+2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "@"
          Peças_obtidas1 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True
            
        #Direita p/ trás
        elif verificar_movimento(posição_atual,posição_desejada,"DT","C","@",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]+2][posição_atual[1]+2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "@"
          Peças_obtidas1 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True

        #Esquerda p/ frente:
        elif verificar_movimento(posição_atual,posição_desejada,"EF","C","@",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]-2][posição_atual[1]-2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "@"
          Peças_obtidas1 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True

        #Esquerda p/ trás:
        elif verificar_movimento(posição_atual,posição_desejada,"ET","C","@",matriz):
          matriz[posição_atual[0]][posição_atual[1]] = " "
          matriz[posição_atual[0]+2][posição_atual[1]-2] = " "
          matriz[posição_desejada[0]][posição_desejada[1]] = "@"
          Peças_obtidas1 += 1
          Jogador -= 1
          print("\nVocê obteve uma peça adversária! Jogue Novamente")
          return True

        #Movimento de uma dama(&) (Qualquer lugar)
        elif matriz[posição_atual[0]][posição_atual[1]] == "&":
          move_dama2 = mover_dama1(posição_atual,posição_desejada,matriz)

          if move_dama2 == False:
            return False

          else:
            if move_dama2 != True:
              matriz[move_dama2[0]][move_dama2[1]] = " "
              Jogador -= 1
              Peças_obtidas1 += 1
              print("\nVocê obteve uma peça adversária. Jogue Novamente!")

            matriz[posição_atual[0]][posição_atual[1]] = " "
            matriz[posição_desejada[0]][posição_desejada[1]] = "&"
            return True

        else:
          return False

  return False

#Verifica se o movimento de uma peça normal desejada (Mover ou capturar) é valido, se sim retorna True, caso contrário, retorna False
def verificar_movimento(posição_atual,posição_desejada,direção,ação,peça,matriz):
  if ação == "M": #Mover sem capturar

    #Verificar movimento de uma peça normal (o) sem capturar peça (Esquerda ou Direita):
    if peça == "o" and matriz[posição_atual[0]][posição_atual[1]] == "o" and posição_desejada[0] == posição_atual[0]+2:
      if posição_desejada[1] == posição_atual[1]+2 or posição_desejada[1] == posição_atual[1]-2:
        return True

    #Verificar movimento de uma peça normal (@) sem capturar peça (Esquerda ou Direita):
    elif peça == "@" and matriz[posição_atual[0]][posição_atual[1]] == "@" and posição_desejada[0] == posição_atual[0]-2:
      if posição_desejada[1] == posição_atual[1]+2 or posição_desejada[1] == posição_atual[1]-2:
        return True
      
    else:
      return False
        
  elif ação == "C": #Mover e capturar

    #Verificar movimento de uma peça normal (o) capturando peça:
    if matriz[posição_atual[0]][posição_atual[1]] == "o" and peça == "o" and matriz[posição_desejada[0]][posição_desejada[1]] == " " and (posição_desejada[0] == posição_atual[0]+4 or posição_desejada[0] == posição_atual[0]-4):
      #Verifica se pode obter a peça pela esquerda:
      if posição_desejada[1] == posição_atual[1]-4:

        if direção == "ET": #Esquerda e p/ trás
          if (matriz[posição_atual[0]-2][posição_atual[1]-2] == "@" or matriz[posição_atual[0]-2][posição_atual[1]-2] == "&") and matriz[posição_atual[0]-2][posição_atual[1]-2] == matriz[posição_desejada[0]+2][posição_desejada[1]+2]:
            return True

        elif direção == "EF": #Esquerda e p/ frente
          if (matriz[posição_atual[0]+2][posição_atual[1]-2] == "@" or matriz[posição_atual[0]+2][posição_atual[1]-2] == "&") and matriz[posição_atual[0]+2][posição_atual[1]-2] == matriz[posição_desejada[0]-2][posição_desejada[1]+2]:
            return True

        else:
          return False
          
      #Verifica se pode obter a peça pela direita:
      elif posição_desejada[1] == posição_atual[1]+4:
        if direção == "DF": #Direita e p/ frente
          if (matriz[posição_atual[0]+2][posição_atual[1]+2] == "@" or matriz[posição_atual[0]+2][posição_atual[1]+2] == "&") and matriz[posição_atual[0]+2][posição_atual[1]+2] == matriz[posição_desejada[0]-2][posição_desejada[1]-2] :
            return True

        elif direção == "DT": #Direita e p/ trás
          if (matriz[posição_atual[0]-2][posição_atual[1]+2] == "@" or matriz[posição_atual[0]-2][posição_atual[1]+2] == "&") and matriz[posição_atual[0]-2][posição_atual[1]+2] == matriz[posição_desejada[0]+2][posição_desejada[1]-2]:
            return True
            
        else:
          return False
      
      else:
        return False

    #Verificar movimento de uma peça normal (@) capturando peça:
    elif matriz[posição_atual[0]][posição_atual[1]] == "@" and peça == "@" and matriz[posição_desejada[0]][posição_desejada[1]] == " " and (posição_desejada[0] == posição_atual[0]+4 or posição_desejada[0] == posição_atual[0]-4): 
      #Verifica se pode obter a peça pela direita:
      if posição_desejada[1] == posição_atual[1]+4:
        
        if direção == "DF": #Direita p/ frente
          if (matriz[posição_atual[0]-2][posição_atual[1]+2] == "o" or matriz[posição_atual[0]-2][posição_atual[1]+2] == "O") and matriz[posição_atual[0]-2][posição_atual[1]+2] == matriz[posição_desejada[0]+2][posição_desejada[1]-2]:
            return True

        elif direção == "DT": #Direita p/ trás
          if (matriz[posição_atual[0]+2][posição_atual[1]+2] == "o" or matriz[posição_atual[0]+2][posição_atual[1]+2] == "O") and matriz[posição_atual[0]+2][posição_atual[1]+2] == matriz[posição_desejada[0]-2][posição_desejada[1]-2]:
            return True
        
        else:
          return False

      #Verifica se pode obter a peça pela esquerda:
      elif posição_desejada[1] == posição_atual[1]-4:
        
        #Esquerda p/ frente
        if direção == "EF":
          if (matriz[posição_atual[0]-2][posição_atual[1]-2] == "o" or matriz[posição_atual[0]-2][posição_atual[1]-2] == "O") and matriz[posição_atual[0]-2][posição_atual[1]-2] == matriz[posição_desejada[0]+2][posição_desejada[1]+2]:
            return True

        #Esquerda p/ trás:
        elif direção == "ET":
          if (matriz[posição_atual[0]+2][posição_atual[1]-2] == "o" or matriz[posição_atual[0]+2][posição_atual[1]-2] == "O") and matriz[posição_atual[0]+2][posição_atual[1]-2] == matriz[posição_desejada[0]-2][posição_desejada[1]+2]:
            return True
        
        else:
          return False
      
      else:
        return False
    
    else:
      return False
  
  return False

#Verifica e transforma a peça caso ela possa virar uma dama (O ou &)
def pode_virar_dama(matriz):
  for i in range(2,20,4):
    if matriz[2][i+2] == "@":
      matriz[2][i+2] = "&"
    if matriz[20][i] == "o":
      matriz[20][i] = "O"

#Verifica o movimento de uma dama (O), retorna True caso seja um movimento válido, retorna a posição da peça adversária caso seja um movimento válido de capturar ou retorna False se o movimento for inválido
def mover_dama0(posição_atual,posição_desejada,matriz):

  num_peças1 = 0
  local_peça1 = []
  aux = 2

  #Se o movimento for para direita (Para trás ou para frente): 
  if posição_desejada[1] > posição_atual[1]:

    #Para frente
    if posição_desejada[0] > posição_atual[0]:
      while (posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]) and (posição_desejada[0] < 21 and posição_desejada[1] < 21 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):
        
        if posição_atual[0]+aux > 20 or posição_atual[1]+aux > 20:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "&":
          num_peças1 += 1
          local_peça1 = [posição_atual[0]+aux,posição_atual[1]+aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "O" or num_peças1 > 1:
          return False


        aux += 2

    #Para Trás 
    elif posição_desejada[0] < posição_atual[0]:
      while (posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]) and (posição_desejada[0] > 1 and posição_desejada[1] < 21 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):

        if posição_atual[0]-aux < 2 or posição_atual[1]+aux > 20:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "&":
          num_peças1 += 1
          local_peça1 = [posição_atual[0]-aux,posição_atual[1]+aux]

          #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "O" or num_peças1 > 1:
          return False
        
        aux += 2

    else:
      return False

    #Verificar se há e pode obter uma peça adversária
    if num_peças1 == 1:
      return local_peça1

    else:
      return True

  #Se o movimento for para esquerda (Para trás ou para frente):
  elif posição_desejada[1] < posição_atual[1]:

    #Para frente
    if posição_desejada[0] > posição_atual[0]:
      while (posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]) and (posição_desejada[0] < 21 and posição_desejada[1] > 1 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):

        if posição_atual[0]+aux > 20 or posição_atual[1]-aux < 2:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "&":
          num_peças1 += 1
          local_peça1 = [posição_atual[0]+aux,posição_atual[1]-aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "O" or num_peças1 > 1:
          return False

        aux += 2

    #Para Trás
    elif posição_desejada[0] < posição_atual[0]:
      while (posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]) and (posição_desejada[0] > 1 and posição_desejada[1] > 1 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):

        if posição_atual[0]-aux < 2 or posição_atual[1]-aux < 2:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "&":
          num_peças1 += 1
          local_peça1 = [posição_atual[0]-aux,posição_atual[1]-aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "O" or num_peças1 > 1:
          return False

        aux += 2

    else:
      return False

    #Verificar se tinha alguma peça adversária obtida ou não
    if num_peças1 == 1:
      return local_peça1
      
    else:
      return True

  else:
    return False

#Verifica o movimento uma dama (&), retorna True caso seja um movimento válido,retorna a posição da peça adversária caso seja um movimento válido de capturar ou retorna False se o movimento for inválido
def mover_dama1(posição_atual,posição_desejada,matriz):

  num_peças2 = 0
  local_peça2 = []
  aux = 2

  global Jogador
  global Peças_obtidas1

  #Se o movimento for para direita (Para trás ou para frente): 
  if posição_desejada[1] > posição_atual[1]:

    #Para Trás
    if posição_desejada[0] > posição_atual[0]:
      while (posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]) and (posição_desejada[0] < 21 and posição_desejada[1] < 21 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):

        if posição_atual[0]+aux > 20 or posição_atual[1]+aux > 20:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "O":
          num_peças2 += 1
          local_peça2 = [posição_atual[0]+aux,posição_atual[1]+aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]+aux] == "&" or num_peças2 > 1:
          return False

        aux += 2

    #Para Frente
    elif posição_desejada[0] < posição_atual[0]:

      while (posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]+aux != posição_desejada[1]) and (posição_desejada[0] > 1 and posição_desejada[1] < 21 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):
        
        if posição_atual[0]-aux < 2 or posição_atual[1]+aux > 20:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "O":
          num_peças2 += 1
          local_peça2 = [posição_atual[0]-aux,posição_atual[1]+aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]+aux] == "&" or num_peças2 > 1:
          return False

        aux += 2

    else:
      return False

    #Verificar se tinha alguma peça adversária obtida ou não
    if num_peças2 == 1:
      return local_peça2
    
    else:
      return True

  #Se o movimento for para esquerda (Para trás ou para frente):
  elif posição_desejada[1] < posição_atual[1]:

    #Para Trás
    if posição_desejada[0] > posição_atual[0]:
      while (posição_atual[0]+aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]) and (posição_desejada[0] < 21 and posição_desejada[1] > 1 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):

        if posição_atual[0]+aux > 20 or posição_atual[1]-aux < 2:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "O":
          num_peças2 += 1
          local_peça2 = [posição_atual[0]+aux,posição_atual[1]-aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]+aux][posição_atual[1]-aux] == "&" or num_peças2 > 1:
          return False


        aux += 2
        
    #Para Frente
    elif posição_desejada[0] < posição_atual[0]:
      while (posição_atual[0]-aux != posição_desejada[0] or posição_atual[1]-aux != posição_desejada[1]) and (posição_desejada[0] > 1 and posição_desejada[1] > 1 and matriz[posição_desejada[0]][posição_desejada[1]] == " "):
        
        if posição_atual[0]-aux < 2 or posição_atual[1]-aux < 2:
          return False

        #Verifica se há alguma peça adversária entre o caminho atual e desejado
        if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "o" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "O":
          num_peças2 += 1
          local_peça2 = [posição_atual[0]-aux,posição_atual[1]-aux]

        #Verifica se há alguma peça aliada entre o caminho atual e desejado e se há mais de uma peça inimiga entre o caminho
        if matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "@" or matriz[posição_atual[0]-aux][posição_atual[1]-aux] == "&" or num_peças2 > 1:
          return False

        aux += 2

    else:
      return False

    #Verificar se tinha alguma peça adversária obtida ou não
    if num_peças2 == 1:
      return local_peça2
    
    else:
      return True
  
  else:
    return False

#Verifica e retorna a posição da peça que deseja mover, se existir
def verificar_posição_atual(coluna_atual,linha_atual,matriz):

  coluna = 2
  linha = 2

  while matriz[0][coluna] != coluna_atual and coluna < 21:
    coluna += 2
  while matriz[linha][0] != linha_atual and linha < 21:
    linha += 2
    
  posição = [linha,coluna]
  if matriz[linha][coluna] == "o" or matriz[linha][coluna] == "O" or matriz[linha][coluna] == "@" or matriz[linha][coluna] == "&":
    return posição

  else:
    return False

#Verifica se existe um espaço vazio válido na posição digitada onde deseja mover,se sim, retorna a posição
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

#Verifica se alguma PEÇA NORMAL pode capturar alguma peça adversária,caso sim, retorna uma lista de movimentos que o jogador será obrigado a escolher, se não, retorna uma lista vazia
def peça_pode_capturar(matriz,Jogador):

  posições = []

  for linha in range(2,22,2):
    for coluna in range(2,22,2):

      posição_atual = [linha,coluna]
      posições_possiveis = [[linha+4,coluna+4],[linha-4,coluna+4],[linha+4,coluna-4],[linha-4,coluna-4]]

      if Jogador%2 == 0 and matriz[linha][coluna] == "o":

          #Verifica se pode capturar alguma peça adversária (@ ou &)
          if linha+4 < 21 and coluna+4 < 21 and verificar_movimento(posição_atual,posições_possiveis[0],"DF","C","o",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[0][1]],matriz[posições_possiveis[0][0]][0]))
              
          if linha-4 > 1 and coluna+4 < 21 and verificar_movimento(posição_atual,posições_possiveis[1],"DT","C","o",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[1][1]],matriz[posições_possiveis[1][0]][0]))
              
          if linha+4 < 21 and coluna-4 > 1 and verificar_movimento(posição_atual,posições_possiveis[2],"EF","C","o",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[2][1]],matriz[posições_possiveis[2][0]][0]))
            
          if linha-4 > 1 and coluna-4 > 1 and verificar_movimento(posição_atual,posições_possiveis[3],"ET","C","o",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[3][1]],matriz[posições_possiveis[3][0]][0]))

      elif Jogador%2 != 0 and matriz[linha][coluna] == "@":
        
          #Verifica se pode capturar alguma peça adversária (o ou O)
          if linha-4 > 1 and coluna+4 < 21 and verificar_movimento(posição_atual,posições_possiveis[1],"DF","C","@",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[1][1]],matriz[posições_possiveis[1][0]][0]))
              
          if linha+4 < 21 and coluna+4 < 21 and verificar_movimento(posição_atual,posições_possiveis[0],"DT","C","@",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[0][1]],matriz[posições_possiveis[0][0]][0]))
              
          if linha-4 > 1 and coluna-4 > 1 and verificar_movimento(posição_atual,posições_possiveis[3],"EF","C","@",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[3][1]],matriz[posições_possiveis[3][0]][0]))
            
          if linha+4 < 21 and coluna-4 > 1 and verificar_movimento(posição_atual,posições_possiveis[2],"ET","C","@",matriz):
            posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]], matriz[posição_atual[0]][0], matriz[0][posições_possiveis[2][1]],matriz[posições_possiveis[2][0]][0]))

  return posições

#Verifica se alguma DAMA pode obter capturar peça adversária,caso sim, retorna uma lista de movimentos que o jogador será obrigado a escolher, se não, retorna uma lista vazia 
def dama_pode_capturar(matriz,Jogador):
  
  posições = []
  aux = 2

  for linha in range(2,22,2):
    for coluna in range(2,22,2):

      posição_atual = [linha,coluna]

      while (linha+aux < 21 or linha-aux > 1) and (coluna+aux < 21 or coluna-aux > 1):

        posições_possiveis = [[linha+aux,coluna+aux],[linha-aux,coluna+aux],[linha+aux,coluna-aux],[linha-aux,coluna-aux]]

        if Jogador%2 == 0 and matriz[linha][coluna] == "O":
          pode_mover0 = mover_dama0(posição_atual,posições_possiveis[0],matriz)
          pode_mover1 = mover_dama0(posição_atual,posições_possiveis[1],matriz)
          pode_mover2 = mover_dama0(posição_atual,posições_possiveis[2],matriz)
          pode_mover3 = mover_dama0(posição_atual,posições_possiveis[3],matriz)

        elif Jogador%2 != 0 and matriz[linha][coluna] == "&":
          pode_mover0 = mover_dama1(posição_atual,posições_possiveis[0],matriz)
          pode_mover1 = mover_dama1(posição_atual,posições_possiveis[1],matriz)
          pode_mover2 = mover_dama1(posição_atual,posições_possiveis[2],matriz)
          pode_mover3 = mover_dama1(posição_atual,posições_possiveis[3],matriz)
          
        else:
          break

        #Verifica se existe alguma peça para ser obtida e retorna o movimento que deve ser feito
        if pode_mover0 != True and pode_mover0 != False:
          posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]],matriz[posição_atual[0]][0],matriz[0][coluna+aux],matriz[linha+aux][0]))
             
        if pode_mover1 != True and pode_mover1 != False:
          posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]],matriz[posição_atual[0]][0],matriz[0][coluna+aux],matriz[linha-aux][0]))

        if pode_mover2 != True and pode_mover2 != False:
          posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]],matriz[posição_atual[0]][0],matriz[0][coluna-aux],matriz[linha+aux][0]))
        
        if pode_mover3 != True and pode_mover3 != False:
          print("entrou pode adicionar")
          posições.append("{}{}--{}{}".format(matriz[0][posição_atual[1]],matriz[posição_atual[0]][0],matriz[0][coluna-aux],matriz[linha-aux][0]))

        if pode_mover0 == False and pode_mover1 == False and pode_mover2 == False and pode_mover3 == False:
          break

        aux += 2

      aux = 2
  return posições

#Verifica se todas as peças estão trancadas, se sim, é considerada derrota
def trancou_peça(matriz):

  global Peças_obtidas0
  global Peças_obtidas1
  peças_trancadas0 = 0
  peças_trancadas1 = 0

  espaços_frente = 0 # Número de espaços na frente e o espaço seguinte da frente da peça
  max_peças_adv = 0 # Numero de peças adversarias que precisam para trancar

  #Percorre o tabuleiro 
  for linha in range(2,21,2):
    for coluna in range(2,21,2):
      
      #Verificar peças (o)
      if matriz[linha][coluna] == "o" or matriz[linha][coluna] == "O":
        for aux in range(2,5,2):
          #Verifica se há espaço na frente e na frente seguinte da peça e se está trancado pela esquerda
          if coluna+aux < 21 and linha+aux < 21:
            max_peças_adv += 1
            if matriz[linha+aux][coluna+aux] == "@" or matriz[linha+aux][coluna+aux] == "&":
              espaços_frente += 1

          #Verifica se há espaço na frente e na frente seguinte da peça e se está trancado pela direita
          if coluna-aux > 1 and linha+aux < 21:
            max_peças_adv += 1
            if matriz[linha+aux][coluna-aux] == "@" or matriz[linha+aux][coluna-aux] == "&":
              espaços_frente += 1
          
          #Verifica os espaços de trás e o seguinte ao de trás (Dama)
          if matriz[linha][coluna] == "O":
            if coluna-aux > 1 and linha-aux > 1:
              max_peças_adv += 1
              if matriz[linha-aux][coluna-aux] == "@" or matriz[linha-aux][coluna-aux] == "&":
                espaços_frente += 1
            
            if coluna+aux < 21 and linha-aux > 1:
              max_peças_adv += 1
              if matriz[linha-aux][coluna+aux] == "@" or matriz[linha-aux][coluna+aux] == "&":
                espaços_frente += 1
        
        #Verifica se o espaço na frente da peça e o espaço seguinte possuem uma peça adversaria (Peça está trancada ou não)
        if espaços_frente == max_peças_adv:
          peças_trancadas0 += 1
        
        espaços_frente = 0
        max_peças_adv = 0

      #Verificar peças (@)
      if matriz[linha][coluna] == "@" or matriz[linha][coluna] == "&":
        for aux in range(2,5,2):

          #Verifica se há espaço na frente e na frente seguinte da peça e se está trancado pela direita
          if coluna+aux < 21 and linha-aux > 1:
            max_peças_adv += 1
            if matriz[linha-aux][coluna+aux] == "o" or matriz[linha-aux][coluna+aux] == "O":
              espaços_frente += 1   

          #Verifica se há espaço na frente e na frente seguinte da peça e se está trancado pela esquerda
          if coluna-aux > 1 and linha-aux > 1:
            max_peças_adv += 1
            if matriz[linha-aux][coluna-aux] == "o" or matriz[linha-aux][coluna-aux] == "O":
              espaços_frente += 1  

          #Verifica os espaços de trás e o seguinte ao de trás (Dama)
          if matriz[linha][coluna] == "&":
            if coluna+aux < 21 and linha+aux < 21:
              max_peças_adv += 1
              if matriz[linha+aux][coluna+aux] == "o" or matriz[linha+aux][coluna+aux] == "O":
                espaços_frente += 1
            
            if coluna-aux > 1 and linha+aux < 21:
              max_peças_adv += 1
              if matriz[linha+aux][coluna-aux] == "o" or matriz[linha+aux][coluna-aux] == "O":
                espaços_frente += 1

        
        #Verifica se o espaço na frente da peça e o espaço seguinte possuem uma peça adversaria (Peça está trancada ou não)
        if espaços_frente == max_peças_adv:
          peças_trancadas1 += 1
        
        espaços_frente = 0
        max_peças_adv = 0
    
  #Verificar quantas peças foram trancadas e se houve derrota por trancar todas as peças adversárias
  if peças_trancadas0 == 15 - Peças_obtidas1 or peças_trancadas1 == 15 - Peças_obtidas0:

    if peças_trancadas0 == 15 - Peças_obtidas1:
      Peças_obtidas1 = 15
      print("Todas as peças do Jogador 0 (o/O) foram trancadas!")
    
    else:
      Peças_obtidas0 = 15
      print("Todas as peças do Jogador 1 (@/&) foram trancadas!")

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
      print("É a vez do jogador de cima (o)!")
    else:
      print("É a vez do jogador de baixo (@)!")
    
    imprimir_tabuleiro(Tabuleiro)
    print("\nPeças obtidas pelo Jogador 0 (o/O) = %d" % Peças_obtidas0)
    print("Peças obtidas pelo Jogador 1 (@/&) = %d\n" % Peças_obtidas1)

    movimento = input("Digite o local da sua peça e para onde deseja mover conforme o exemplo (Ex: A7--B6): ")
    num_possibilidades = peça_pode_capturar(Tabuleiro,Jogador)
    num_possibilidades_dama = dama_pode_capturar(Tabuleiro,Jogador)

    #Verifica se alguma peça ou dama pode capturar uma peça adversária,se sim, o jogador será obrigado a fazer o movimento de captura
    if len(num_possibilidades) != 0 or len(num_possibilidades_dama) != 0:
      print("num possibilidades peça : ",num_possibilidades)
      print("num possibilidades dama : ",num_possibilidades_dama)

      if movimento in num_possibilidades or movimento in num_possibilidades_dama:
        mover_peça = movimento_peça(movimento,Tabuleiro)

      elif len(num_possibilidades) != 0 or len(num_possibilidades_dama) != 0:
        while not movimento in num_possibilidades and not movimento in num_possibilidades_dama:
          movimento = input("\nJogada inválida, é obrigatório capturar a peça adversária! Digite novamente: ")

        mover_peça = movimento_peça(movimento,Tabuleiro)

          

    else:
      mover_peça = movimento_peça(movimento,Tabuleiro)
      
    #Verificar se o movimento foi válido
    while mover_peça == False :
      movimento = input("\nJogada inválida, digite um movimento válido (Ex: A7--B6): ")
      mover_peça = movimento_peça(movimento,Tabuleiro)

    trancou_peça(Tabuleiro)
    
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

    pode_virar_dama(Tabuleiro)
    Jogador += 1

print("\nObrigado por jogar!")