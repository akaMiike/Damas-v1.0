# Damas-v1.0
Um simples jogo de Damas.

Esse foi um dos meus primeiros programas "grandes" que tive que fazer no início do curso, porém não havia concluido.
Então resolvi refazer depois de um ano para ver como eu evoluí.


!!! LEIA AS REGRAS ABAIXO PARA ENTENDER O FUNCIONAMENTO DO PROGRAMA, CASO DESEJE JOGAR !!!

MODO USUÁRIO CONTRA USUÁRIO:

U.1. Na vez de cada usuário, uma jogada deverá ser entrada. Cada
jogada é composta da posição inicial e da posição final de uma peça,
no modo “COLUNA_INICIAL/LINHA_INICIAL>--
COLUNA_FINAL/LINHA_FINAL”, conforme mapeado no exemplo
da Figura 1, sem nenhum espaço entre os caracteres da jogada. São
exemplos de jogadas: “B0--C1”, “I7--H6”.

U.2. As peças podem ser de dois tipos: normais (“@” ou “o”) ou damas (“&” ou “O”). As peças normais só
podem caminhar na diagonal, um salto por vez, sempre para a frente. Uma dama pode caminhar na
diagonal, um ou mais saltos por vez, para frente ou para trás, desde que o caminho esteja livre.

U.3. Uma peça normal se torna dama quando esta chega ao outro extremo do tabuleiro. Isto é, para o
jogador de cima, quando a peça atinge a linha 9, e para o jogador de baixo, quando atinge a linha 0.

U.4. Uma peça normal pode “comer” uma peça adversária saltando para a posição seguinte à peça
adversária, que deve ser retirada do tabuleiro e contabilizada para o usuário que fez a jogada.

U.5. Apenas na ocasião de “comer” uma peça adversária, uma peça normal pode fazer um movimento para trás (“comer para trás”).

U.6. Uma dama pode “comer” apenas uma peça de cada vez, que esteja em uma de suas diagonais. O
caminho até a peça a ser comida deve estar livre e deve haver pelo menos um espaço livre após a
peça comida. A dama não é obrigada a parar na casa logo após a peça comida, desde que ainda haja
posições livres na mesma diagonal.

U.7. O usuário que comer uma peça adversária deverá jogar novamente logo em seguida.

U.8. O programa deverá verificar a validade da jogada entrada. Caso a jogada seja inválida, o programa
deverá mostrar uma mensagem “Jogada Inválida”, e deverá solicitar uma nova jogada do mesmo
jogador;

U.9. São jogadas inválidas:
a. Quando o usuário entra as coordenadas de uma posição inicial que não tem nenhuma peça, ou tem
uma peça que não é sua;
b. Quando o usuário indica um movimento de mais de um salto para peças normais (excetuando-se o
movimento de “comer” uma peça);
c. Quando o usuário indica um movimento que não é em diagonal;
d. Quando o usuário indica um movimento onde a posição final da peça já está ocupada;
e. Quando o usuário indica um movimento de uma peça normal onde a posição final fica para trás;
f. Quando o usuário indica um movimento de comer peça que não é válido, segundo os requisitos
listados acima.

U.10. Quando um usuário se deparar com uma situação onde alguma das peças dele puder comer uma
peça adversária, ele deverá obrigatoriamente realizar esta jogada de comer a peça adversária. Caso
haja mais de uma possibilidade como esta em uma jogada, o usuário poderá escolher qual comerá
primeiro.

U.11. Quando todas as peças de um jogador são comidas, o programa deve contabilizar a vitória do
oponente e perguntar se o usuário gostaria de recomeçar o jogo.