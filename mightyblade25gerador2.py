import random

def dado(lados):
    return random.randint(1, lados)
    
def raça_dado(dado1):
    if dado1 == 1:
        return Humano
    elif dado1 == 2:
        return Anão
    elif dado1 == 3:
        return Elfo
    elif dado1 == 4:    
        return Halfling
    elif dado1 == 5:
        return Orc
    else:
        return Faen
        
def classe_dado(dado2):
    if dado2 == 1:
        return Espadachim
    elif dado2 == 2:
        return Guerreiro
    elif dado2 == 3:
        return Bárbaro
    elif dado2 == 4:    
        return Paladino
    elif dado2 == 5:
        return Ranger
    elif dado2 == 6:
        return Ladrão
    elif dado2 == 7:
        return Feiticeiro
    else:
        return Sacerdote
        
def classe_comum(JogadorRaça): 
    if JogadorRaça == Humano:
        def humano_dado(dado3):
            if dado3 == 1:
                return Espadachim
            elif dado3 == 2:
                return Guerreiro
            elif dado3 == 3:
                return Bárbaro
            elif dado3 == 4:    
                return Paladino
            elif dado3 == 5:
                return Ranger
            elif dado3 == 6:
                return Ladrão
            elif dado3 == 7:
                return Feiticeiro
            else:
                return Sacerdote
        return humano_dado(dado(8)) 
        
    elif JogadorRaça == Anão:
        def anão_dado(dado4):
            if dado4 == 1:
                return Guerreiro
            elif dado4 == 2:
                return Paladino
            else:
                return Sacerdote
        return anão_dado(dado(3))
        
    elif JogadorRaça == Elfo:
        def elfo_dado(dado5):
            if dado5 == 1:
                return Ranger
            elif dado5 == 2:
                return Espadachim
            elif dado5 == 3:
                return Ladrão
            else:
                return Feiticeiro
        return elfo_dado(dado(4))
        
    elif JogadorRaça == Halfling:
        return Ladrão
        
    elif JogadorRaça == Orc:
        return Bárbaro
        
    elif JogadorRaça == Faen:
        return Feiticeiro  
        
class Raça:
    def __init__(self, Nome, Força, Agilidade, Inteligência, Vontade, Bônus):
        self.Nome = Nome
        self.Força = Força
        self.Agilidade = Agilidade
        self.Inteligência = Inteligência
        self.Vontade = Vontade
        self.Bônus = Bônus
        
class Classe:
    def __init__(self, Nome, Força, Agilidade, Inteligência, Vontade, Proficiência):
        self.Nome = Nome
        self.Força = Força
        self.Agilidade = Agilidade
        self.Inteligência = Inteligência
        self.Vontade = Vontade
        self.Proficiência = Proficiência

#Raças
Humano = Raça('Humano ', 3, 3, 3, 3, '+1 em atributo à sua escolha')
Anão = Raça('Anão ', 4 , 2, 3, 3, 'Vigor da Montanha: Você é imune a venenos e pode rolar 3d6 quando fizer testes de Força para resitir à fadiga.')
Elfo = Raça('Elfo ', 2, 4, 3 , 3, 'Sentidos Apurados: Você pode rolar 3d6 quando fizer testes de Inteligência que envolve percepção e os cinco sentidos.')
Halfling = Raça('Halfling ', 2, 4, 3, 3, 'Tamanho Pequeno: Você pode rolar 3d6 quando fizer testes de Agilidade para se esconder e mover em silêncio; você também ganha Defesa +1.')
Orc = Raça('Orc ', 4, 3, 2, 3, 'Sangue Orc: Você possui +10 pontos de vida.')
Faen = Raça('Faen ', 2, 3, 4, 3, 'Asas Rápidas: Suas pequenas asas podem bater bem rápido, lhe dando grande mobilidade no ar. Você pode voar para qualquer direção e parar no ar, porém, este bater de asas cansa, limitando-se a voar por no máximo 1 hora. Não é possivel voar enquanto carrega coisas muito pesadas.')

#Classes
Espadachim = Classe('Espadachim', 1, 1, 0, 0, 'Usar Armas Simples e Complexas.')
Guerreiro = Classe('Guerreiro', 1, 1, 0, 0, 'Usar Armas Simples e Complexas.')
Bárbaro = Classe('Bárbaro', 1, 1, 0, 0, 'Usar Armas Simples e Complexas.')
Paladino = Classe('Paladino', 1, 0, 0, 1, 'Usar Armas Simples e Complexas.')
Ranger = Classe('Ranger', 0, 1, 1, 0, 'Usar Armas Simples e Complexas.')
Ladrão = Classe('Ladrão', 0, 1, 1, 0, 'Usar Armas Simples e Futar Bolsos.')
Feiticeiro = Classe('Feiticeiro', 0, 0, 1, 1, 'Usar Armas Simples e Ler Escritas Mágicas.')
Sacerdote = Classe('Sacerdote', 0, 0, 1, 1, 'Usar Armas Simples e Ler Escritas Mágicas.')

while True:
    print('Digite: ')
    print('1- Caso queira um personagem totalmente aleatório')
    print('2- Caso queira um personagem com classe e raça comuns')
    print('Ou aperte Ctrl+C para cancelar o script')
    Escolha = input()
    print('')
    if Escolha == '1':
        JogadorRaça = raça_dado(dado(6))
        JogadorClasse = classe_dado(dado(8))
        print(JogadorRaça.Nome + JogadorClasse.Nome)
        print('Bônus: ' + str(JogadorRaça.Bônus))
        print('Proficiências: ' + str(JogadorClasse.Proficiência))
        print('Força:' + str(JogadorRaça.Força + JogadorClasse.Força))
        print('Agilidade:' + str(JogadorRaça.Agilidade + JogadorClasse.Agilidade))
        print('Inteligência:' + str(JogadorRaça.Inteligência + JogadorClasse.Inteligência))
        print('Vontade:' + str(JogadorRaça.Vontade + JogadorClasse.Vontade))
        print('')

    elif Escolha == '2':
        JogadorRaça = raça_dado(dado(6))
        JogadorClasse = classe_comum(JogadorRaça)
        print(JogadorRaça.Nome + JogadorClasse.Nome)
        print('Bônus: ' + str(JogadorRaça.Bônus))
        print('Proficiências: ' + str(JogadorClasse.Proficiência))
        print('Força:' + str(JogadorRaça.Força + JogadorClasse.Força))
        print('Agilidade:' + str(JogadorRaça.Agilidade + JogadorClasse.Agilidade))
        print('Inteligência:' + str(JogadorRaça.Inteligência + JogadorClasse.Inteligência))
        print('Vontade:' + str(JogadorRaça.Vontade + JogadorClasse.Vontade))
        print('')