from colorama import Fore, Style

Temperatura_Semanas = {"Segunda": (0, 0), "Terça": (0, 0), "Quarta": (0, 0), "Quinta": (0, 0), "Sexta": (0, 0), "Sabado": (0, 0), "Domingo": (0, 0)}

def AdicionarTemperaturas():
    global Temperatura_Semanas

    try:
        for c, (min, max) in Temperatura_Semanas.items():
            print(f"{Fore.CYAN}{c.upper()}{Style.RESET_ALL}")
            min = float(input(f"Digita a temperatura minima no dia {c}: "))
            max = float(input(f"Digita a temperatura maxima no dia {c}: "))

            if min > max: 
                print(f"\n{Fore.RED}Não é possivel a temperatura minima ser maior do que a temperatura maxima. Tente novamente.{Style.RESET_ALL}")
                raise ValueError

            Temperatura_Semanas[c] = (min, max)
            print("\n")
    
    except ValueError:
        print(f"\n {Fore.RED}Valor errado, tente novamente{Style.RESET_ALL}\n")
        Main()

def CalcularMedia():
    global Temperatura_Semanas

    soma = 0
    
    for _, (min, max) in Temperatura_Semanas.items():
        soma += (max + min)

    return soma / 14

def AnalisarDias():
    global Temperatura_Semanas

    lista_acima_media = []
    lista_abaixo_media = []

    media_semana = CalcularMedia()

    for c, (min, max) in Temperatura_Semanas.items():
        media_dia = (min + max) / 2

        if media_dia > media_semana:
            lista_acima_media.append(c)
        else:
            lista_abaixo_media.append(c)

    return lista_acima_media, lista_abaixo_media

def ExibirResultados(media_semana, semana_acima_media, semana_abaixo_media):
    global Temperatura_Semanas

    texto_semanas = f"\n{Fore.LIGHTCYAN_EX}=== TEMPERATURA DOS DIAS DA SEMANA ==={Style.RESET_ALL}\n"

    for c, (min, max) in Temperatura_Semanas.items():
        texto_semanas += f"{c} --> Mín: {min}°C | Max: {max}°C\n"

    print(texto_semanas, "\n =================================================================\n")

    print(f"Media da temperatura da semana: {media_semana}°C\n")

    texto_semanas_acima_media = f"{Fore.LIGHTYELLOW_EX}=== DIAS ACIMA DA MEDIA ==={Style.RESET_ALL}\n"
    texto_semanas_abaixo_media = f"{Fore.LIGHTYELLOW_EX}=== DIAS ABAIXO DA MEDIA ==={Style.RESET_ALL}\n"

    for i in semana_acima_media:
        texto_semanas_acima_media += f"- {i}\n"

    for i in semana_abaixo_media:
        texto_semanas_abaixo_media += f"- {i}\n"

    print(texto_semanas_acima_media, "\n")
    print(texto_semanas_abaixo_media, "\n")

def Main():
    AdicionarTemperaturas()
    media_semana = CalcularMedia()
    semanas_media_acima, semanas_media_abaixo = AnalisarDias()
    ExibirResultados(media_semana, semanas_media_acima, semanas_media_abaixo)

Main()
