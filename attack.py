import os
import time
import random

def clear_screen():
    os.system('clear')

def print_menu():
    clear_screen()
    print("=====================================")
    print("       MENU HACKER      ")
    print("=====================================")
    print("1. ataque DDoS")
    print("2. varredura de portas")
    print("3. exploit")
    print("4. ataque em redes sociais")
    print("5. ataque redes Wi-Fi")
    print("6. Sair")
    print("=====================================")

def simulate_ddos():
    clear_screen()
    print("Iniciando ataque DDoS...")
    time.sleep(2)
    print("Alvo: 192.168.0.1")
    time.sleep(1)
    print("Enviando pacotes...")
    time.sleep(3)
    print("Ataque DDoS concluído.")
    input("Pressione Enter para voltar ao menu...")

def simulate_port_scan():
    clear_screen()
    print("Iniciando varredura de portas...")
    time.sleep(2)
    print("Alvo: 192.168.0.1")
    time.sleep(1)
    for port in range(20, 25):
        print(f"Porta {port}: aberta")
        time.sleep(0.5)
    print("Varredura de portas concluída.")
    input("Pressione Enter para voltar ao menu...")

def simulate_exploit():
    clear_screen()
    print("Iniciando exploit...")
    time.sleep(2)
    print("Alvo: 192.168.0.1")
    time.sleep(1)
    print("Explorando vulnerabilidade...")
    time.sleep(3)
    print("Exploit concluído.")
    input("Pressione Enter para voltar ao menu...")

def simulate_social_media_attack():
    clear_screen()
    print("Escolha uma rede social para o ataque:")
    print("1. Instagram")
    print("2. Facebook")
    print("3. Twitter")
    print("4. YouTube")
    print("5. WhatsApp")
    print("6. Telegram")

    choice = input("Selecione uma opção: ")
    targets = {
        '1': 'Instagram',
        '2': 'Facebook',
        '3': 'Twitter',
        '4': 'YouTube',
        '5': 'WhatsApp',
        '6': 'Telegram'
    }

    if choice in targets:
        clear_screen()
        user_info = input(f"Digite o nome de usuário, número de telefone ou e-mail para o ataque em {targets[choice]}: ")
        print(f"Iniciando ataque em {targets[choice]}...")
        time.sleep(2)
        print(f"Coletando informações de {user_info} no {targets[choice]}...")
        time.sleep(3)
        print(f"Explorando vulnerabilidades em {user_info} no {targets[choice]}...")
        time.sleep(3)
        print(f"Ataque simulado em {user_info} no {targets[choice]}...")
        time.sleep(2)
        print(f"Obtendo informações de {user_info} no {targets[choice]}...")
        time.sleep(3)

        # Lista de vítimas fictícias
        fake_victims = [
            {
                "Nome Completo": "João Silva",
                "Data de Nascimento": "01/01/1990",
                "Número de Telefone secundário": "+55 11 91234-5678",
                "E-mail": "joao.silva@example.com",
                "Endereço": "Rua Exemplo, 123, São Paulo, SP",
                "Senha": "senha123",
                "Número do Cartão de Crédito": "1234 5678 9012 3456",
                "Data de Expiração": "12/25",
                "CVV": "123"
            },
            {
                "Nome Completo": "Maria Oliveira",
                "Data de Nascimento": "15/05/1985",
                "Número de Telefone secundário": "+55 21 98765-4321",
                "E-mail": "maria.oliveira@example.com",
                "Endereço": "Avenida Central, 456, Rio de Janeiro, RJ",
                "Senha": "minhasenha",
                "Número do Cartão de Crédito": "6543 2109 8765 4321",
                "Data de Expiração": "11/24",
                "CVV": "456"
            },
            {
                "Nome Completo": "Carlos Pereira",
                "Data de Nascimento": "23/03/1975",
                "Número de Telefone secundário": "+55 31 99876-5432",
                "E-mail": "carlos.pereira@example.com",
                "Endereço": "Rua das Flores, 789, Belo Horizonte, MG",
                "Senha": "segredinho",
                "Número do Cartão de Crédito": "1122 3344 5566 7788",
                "Data de Expiração": "10/23",
                "CVV": "789"
            },
            {
                "Nome Completo": "Ana Costa",
                "Data de Nascimento": "30/08/1995",
                "Número de Telefone secundário": "+55 41 92345-6789",
                "E-mail": "ana.costa@example.com",
                "Endereço": "Praça da Liberdade, 101, Curitiba, PR",
                "Senha": "senha789",
                "Número do Cartão de Crédito": "4433 2211 5566 7788",
                "Data de Expiração": "09/26",
                "CVV": "321"
            }
        ]

        # Seleciona uma vítima aleatória
        victim = random.choice(fake_victims)

        for key, value in victim.items():
            print(f"{key}: {value}")
            time.sleep(1)
    else:
        print("Opção inválida!")

    input("Pressione Enter para voltar ao menu...")

def simulate_wifi_attack():
    clear_screen()
    print("Escolha um tipo de ataque em redes Wi-Fi:")
    print("1. Wi-Fi")
    print("2. WPS")
    print("3. WPA")
    print("4. WPA2")
    print("5. Cabo")
    print("6. Wi-Fi Fake")

    choice = input("Selecione uma opção: ")
    attacks = {
        '1': 'Wi-Fi',
        '2': 'WPS',
        '3': 'WPA',
        '4': 'WPA2',
        '5': 'Cabo',
        '6': 'Wi-Fi Fake'
    }

    if choice in attacks:
        clear_screen()
        print(f"Iniciando ataque em rede {attacks[choice]}...")
        time.sleep(2)
        print(f"Escaneando redes ao redor {attacks[choice]} disponíveis...")
        time.sleep(3)
        print(f"Explorando vulnerabilidades em redes {attacks[choice]}...")
        time.sleep(3)
        print(f"Ataque em rede {attacks[choice]} concluído.")
        time.sleep(2)

        # Informações simuladas sobre redes
        fake_networks = [
            {
                "SSID": "Rede_Vizinho",
                "Senha": "senha123",
                "Segurança": "WPA2",
                "Intensidade do Sinal": "-40dBm"
            },
            {
                "SSID": "Café_Aberto",
                "Senha": "cafepublico",
                "Segurança": "WEP",
                "Intensidade do Sinal": "-50dBm"
            },
            {
                "SSID": "Empresa_XYZ",
                "Senha": "corporativo789",
                "Segurança": "WPA",
                "Intensidade do Sinal": "-60dBm"
            },
            {
                "SSID": "Casa_da_Maria",
                "Senha": "minhasenha123",
                "Segurança": "WPA2",
                "Intensidade do Sinal": "-45dBm"
            }
        ]

        # Seleciona uma rede aleatória
        network = random.choice(fake_networks)

        for key, value in network.items():
            print(f"{key}: {value}")
            time.sleep(1)
    else:
        print("Opção inválida!")

    input("Pressione Enter para voltar ao menu...")

def main():
    while True:
        print_menu()
        choice = input("Selecione uma opção: ")
        if choice == '1':
            simulate_ddos()
        elif choice == '2':
            simulate_port_scan()
        elif choice == '3':
            simulate_exploit()
        elif choice == '4':
            simulate_social_media_attack()
        elif choice == '5':
            simulate_wifi_attack()
        elif choice == '6':
            clear_screen()
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    main()
