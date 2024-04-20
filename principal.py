

import PySimpleGUI as psg

Yara = '''A Iara, também conhecida como “mãe d'agua”, é uma entidade que faz parte do folclore brasileiro, sendo muito conhecida, principalmente na região Norte do Brasil. Na lenda, diz-se que a Iara é uma sereia, sendo parte mulher e parte peixe. Ela mora dentro de um rio e possui grande beleza física, uma bela voz e muitas riquezas.

A lenda conta que Iara usa esses atributos (a beleza, a voz e a riqueza) para seduzir homens que estão navegando no rio ou que estão às margens dele. Os homens, encantados, vão para junto de Iara, que os leva para sua residência debaixo d'água. Aqueles que são seduzidos não são vistos novamente.

De acordo com a narrativa, ela era filha de um pajé e possuía grandes habilidades como guerreira. Essas habilidades eram motivo de inveja para os irmãos dela, que decidiram se reunir para matá-la em certa ocasião, mas ela resistiu, lutou e matou todos eles.

Temerosa da reação do seu pai, ela fugiu, mas foi encontrada, e seu pai decidiu lançá-la entre os rios Negro e Solimões. Ela teria sido salva pelos peixes e se transformado em Iara durante uma noite de lua cheia. O termo “Iara” tem origem no idioma tupi, sendo a mistura 
de duas palavras: ig, que significa “água”, e iara, que significa “senhor”. Iara, portanto, seria a senhora das águas.

Nesse jogo, a Yara é um ser místico que utiliza do seu canto para atormentar e causar forte dano nos inimigos.'''

Jaci = """Jaci, na mitologia tupi-guarani, é a deusa da Lua, protetora das plantas, dos amantes e da reprodução. Seu nome deriva da palavra tupi Iacy, que significa “Mãe dos Frutos”.

Segundo a tradição, Guaraci, o deus do Sol, um dia cansou-se de seu ofício eterno e precisou dormir. Quando fechou os olhos, o mundo caiu em trevas. Para iluminar a escuridão enquanto dormia, Nhanderu criou Jaci, a lua. Porém, Guaraci e Jaci foram raptados por onças, mas conseguiram escapar. Acredita-se que quando ocorre um eclipse, é porque as onças os raptaram novamente e os uniram.

Guaraci pediu a Nhanderu que criasse Rudá, o amor e seu mensageiro, para conquistar um de seus amores. O amor não conhecia luz ou escuridão, podendo uni-los na alvorada.

Mitologicamente, Jaci é identificada com Diana dos romanos, Xochiquetzal dos aztecas, Chandra dos hindus e Ísis dos antigos egípcios."""

Saci = """O Saci é retratado como um menino negro, pré-adolescente, com cerca de 11 anos. Ele possui apenas uma perna e veste um gorro vermelho que lhe confere poderes mágicos. Suas principais travessuras incluem trançar o rabo dos animais durante a noite, esconder objetos como dedais de costureiras, assobiar estridentemente para assustar viajantes, trocar o recipiente de sal pelo de açúcar e distrair cozinheiras para queimarem a comida. Além disso, o Saci é o guardião das ervas e plantas medicinais, confundindo quem tenta pegá-las sem autorização."""

Curupira = """O Curupira é retratado frequentemente como um anão que possui os cabelos vermelhos e os pés ao contrário (com os calcanhares para frente). É importante reforçar que a descrição física do Curupira pode variar de acordo com o local em que a lenda é reproduzida. Em certos locais, o Curupira é careca; em outros, tem o corpo cabeludo e dentes verdes. De toda forma, as características que se sobressaem são as citadas: baixa estatura, cabelos vermelhos e pés ao contrário. Além disso, destaca-se sua grande força física."""

Lobisomem = """O lobisomem, uma das lendas mais conhecidas em todo o mundo, fala de homens que têm a capacidade de transformar-se em lobos. Essa prática era considerada uma maldição, chamada de licantropia, e a primeira menção a ela foi registrada na mitologia grega.

A origem da lenda do lobisomem é europeia e provavelmente se disseminou a partir do século XVI. Entretanto, ela aparece em alguns mitos gregos, como em Licaão e Damarco. Reza a lenda que, inicialmente, um homem foi mordido por um lobo e ficou enfeitiçado. Assim, nas noites de lua cheia, ele se transformava, adquirindo garras de lobo e um corpo coberto de pelos, e saía uivando em busca de seu alimento predileto: sangue."""

Zumbi_dos_Palmares = """Zumbi dos Palmares (1655-1695) foi o último líder do Quilombo dos Palmares e também o de maior relevância histórica. Ele ganhou respeito e admiração de seus compatriotas quilombolas devido às suas habilidades como guerreiro, que lhe conferiam coragem, liderança e conhecimentos de estratégia militar.

Zumbi dos Palmares é um símbolo pela liberdade dos negros na história brasileira e sua morte é celebrada como o Dia da Consciência Negra no Brasil
"""

Dandara = """Dandara dos Palmares foi uma das grandes personalidades do Quilombo dos Palmares. Ela era uma mulher guerreira e liderou tropas na luta dos palmaristas contra os portugueses. Infelizmente, os historiadores sabem muito pouco sobre sua vida, mas há alguns destaques importantes"""

Tiradentes = """Tiradentes, cujo nome completo era Joaquim José da Silva Xavier, foi um dos líderes da Inconfidência Mineira, um movimento que buscava a independência do Brasil em relação a Portugal. Sua história é marcada por coragem, idealismo e sacrifício."""

Dom_Pedro1 = """Dom Pedro I é um dos grandes nomes da história do Brasil. Foi um dos condutores do processo de independência, além de ter sido imperador brasileiro de 1822 a 1831. Filho de D. João VI, rei de Portugal, Dom Pedro I ficou conhecido ao longo de sua vida por ser impulsivo e mulherengo.
Durante seu reinado sobre o Brasil, a sua grande marca foi o autoritarismo e, por esse motivo, sua relação com as elites do Brasil desgastou-se ao ponto de D. Pedro renunciar ao trono, em 1831. Depois disso, retornou a Portugal, onde lutou na Guerra Civil Portuguesa, em defesa do direito de sua filha d. Maria assumir o trono português."""

Irmã_Dulce = """Irmã Dulce (1914-1992) foi uma religiosa católica brasileira que dedicou a sua vida a ajudar os doentes e os mais necessitados.
Irmã Dulce foi beatificada pelo Papa Bento XVI, no dia 10 de dezembro de 2010, passando a ser reconhecida com o título de "Bem-aventurada Dulce dos Pobres". Foi declarada santa pelo Papa Francisco em uma celebração no Vaticano no dia 13 de outubro de 2019.
Maria Rita de Souza Brito Lopes Pontes nasceu em Salvador, Bahia, no dia 26 de maio de 1914. Filha de Augusto Lopes Pontes, dentista e professor da Universidade Federal da Bahia, e de Dulce Maria de Souza Brito Lopes Pontes.
Desde criança, Irmã Dulce desejava seguir a vida religiosa e, rezava muito, pedindo algum sinal que mostrasse se deveria ou não seguir esse caminho.
Ainda na adolescência, começou a desenvolver a sua missão de ajudar os mendigos, carentes e enfermos."""


cor_bt = "black"
cor_ft = "black"
posicao1 = "right"



layout1 = [
    [psg.Text(f'Escolha a história a ser contada:', justification='center', expand_x= True, text_color= "yellow", font=("arial", 24), background_color= "black")],
    [psg.Column([
        [psg.Button('Yara', button_color=cor_bt, size=(15, 1), border_width= 0), psg.Button('Zumbi dos Palmares', button_color=cor_bt, size=(15, 1), border_width= 0)],
        [psg.Button('Jaci', button_color=cor_bt, size=(15, 1), border_width= 0), psg.Button('Dandara', button_color=cor_bt, size=(15, 1), border_width= 0)],
        [psg.Button('Saci', button_color=cor_bt, size=(15, 1), border_width= 0), psg.Button('Tiradentes', button_color=cor_bt, size=(15, 1), border_width= 0)],
        [psg.Button('Curupira', button_color=cor_bt, size=(15, 1), border_width= 0), psg.Button('D. Pedro I', button_color=cor_bt, size=(15, 1), border_width= 0)],
        [psg.Button('Lobisomem', button_color=cor_bt, size=(15, 1), border_width= 0), psg.Button('Irmã Dulce', button_color=cor_bt, size=(15, 1), border_width= 0)]],
    element_justification='center', expand_x= True, background_color= 'black')],
]

janela = psg.Window("Histórias", layout1, size= (500, 300), background_color= "black")

while True:
    event, values = janela.read()
    if event == psg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == "Yara":
        psg.popup("Yara",
                  Yara,
                  background_color= cor_bt)
    elif event == "Jaci":
        psg.popup("Jaci",
                  Jaci,
                  background_color= cor_bt)
    elif event == "Saci":
        psg.popup("Saci",
                  Saci,
                  background_color= cor_bt)
    elif event == "Curupira":
        psg.popup("Curupira",
                  Curupira,
                  background_color= cor_bt)
    elif event == "Lobisomem":
        psg.popup("Lobisomem",
                  Lobisomem,
                  background_color= cor_bt)
    elif event == "Zumbi dos Palmares":
        psg.popup("Zumbi dos Palmares",
                  Zumbi_dos_Palmares,
                  background_color= cor_bt)
    elif event == "Dandara":
        psg.popup("Dandara",
                  Dandara,
                  background_color= cor_bt)
    elif event == "Tiradentes":
        psg.popup("Tiradentes",
                  Tiradentes,
                  background_color= cor_bt)
    elif event == "D. Pedro I":
        psg.popup("D. Pedro I",
                  Dom_Pedro1,
                  background_color= cor_bt,)
    elif event == "Irmã Dulce":
        psg.popup("Irmã Dulce",
                  Irmã_Dulce,
                  background_color= cor_bt)

janela.close()