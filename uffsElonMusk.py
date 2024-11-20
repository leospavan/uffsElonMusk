def resumo():
    mensagem = "Elon Musk é um empresário e inovador conhecido por fundar e liderar empresas revolucionárias como Tesla, SpaceX, Neuralink e The Boring Company. Ele é um defensor da energia sustentável, exploração espacial e avanços em inteligência artificial e transporte. Musk é uma figura influente no mundo da tecnologia e empreendedorismo, constantemente impulsionando os limites da inovação."
    return mensagem


def doutorado():
    mensagem = "Elon Musk possui graduação em Economia e Física, mas não concluiu o doutorado porque se dedicou ao empreendedorismo no campo da internet e tecnologia."
    return mensagem


def contribuicoes():
    mensagem = """A Neuralink, fundada por Elon Musk, desenvolve tecnologias de interface cérebro-computador, permitindo a comunicação direta entre o cérebro humano e dispositivos. A empresa busca tratar condições neurológicas e, no longo prazo, possibilitar uma simbiose entre humanos e máquinas. Seu impacto pode revolucionar a forma como interagimos com a tecnologia, avançando na neurociência e na inteligência artificial. 
    Tesla Como CEO da Tesla, Musk tem desempenhado um papel importante na integração de inteligência artificial (IA) e aprendizado de máquina em veículos autônomos. A Tesla usa algoritmos complexos para suas funções de direção autônoma, como o sistema Autopilot. Musk tem defendido publicamente o uso da IA para criar veículos mais seguros, enquanto também levantou preocupações sobre o controle ético da IA."""
    return mensagem


def artigos():
    mensagem = """" - Hyperloops: Em 2013, Musk publicou um artigo descrevendo o Hyperloop, uma proposta de transporte terrestre que seria mais rápido, prático e sustentável do que o metrô. O Hyperloop funcionaria dentro de um tubo com baixa pressão e levitação magnética, permitindo que os veículos alcançassem altas velocidades.
    - Inteligência artificial: Musk acredita que a inteligência artificial com capacidade humana vai acontecer antes do que se imagina e defende uma legislação específica para regular os sistemas de IA."""
    return mensagem


def citacoes():
    mensagem = """ - Quando Ford fez carros baratos e confiáveis, disseram: 'O que há de errado com um cavalo?' Foi uma grande aposta e funcionou.
    - O primeiro passo é estabelecer que algo é possível; então a probabilidade acontecerá.
    - Acho que é possível para pessoas comuns escolherem ser extraordinárias. """
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
