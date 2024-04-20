

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

Curupira = ""

Lobisomem = ""

Zumbi_dos_Palmares = ""

Dandara = ""

Tiradentes = ""

Dom_Pedro1 = ""

Irmã_Dulce = ""


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