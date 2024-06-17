#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random

def sms_spam():
    print("\n=== SMS Spam ===")
    numero_alvo = input("Digite o número do alvo (com código do país): ")
    quantidade = int(input("Digite a quantidade de SMS a enviar: "))
    mensagem = input("Digite a mensagem a ser enviada: ")

    print(f"\nEnviando {quantidade} SMS para {numero_alvo}...")
    print(f"'{mensagem}'\n")

    # Simulação do envio dos SMS (pode ser implementado de fato se necessário)
    for _ in range(quantidade):
        print(f"Enviando SMS para {numero_alvo}...")
        # Aqui você pode adicionar a lógica para simular o envio de SMS

    input("\nPressione Enter para continuar.")

def link_phishing():
    print("\n=== Verificação de Link Phishing ===")
    url = input("Digite a URL a verificar: ")

    # Simulação de verificação se o site é malicioso ou limpo
    if random.random() < 0.5:
        print(f"\nO site '{url}' é considerado MALICIOSO!")
    else:
        print(f"\nO site '{url}' é considerado LIMPO.")

    input("\nPressione Enter para continuar.")

def quebra_senha():
    print("\n=== Quebra de Senha por Força Bruta ===")
    print("Conecte o cabo USB ao dispositivo alvo...")
    input("Pressione Enter quando estiver pronto para continuar...")

    # Simulação de quebra de senha (dados simulados)
    print("\nQuebrando senha...")
    print("Dados do usuário obtidos:")
    print("Username: johndoe")
    print("Password: ********")  # Aqui você pode simular a senha obtida

    input("\nPressione Enter para continuar.")

def menu():
    while True:
        # Limpar a tela
        os.system('clear')

        # Exibir o menu
        print("=== Simulador Hacker ===")
        print("1. SMS Spam")
        print("2. Link Phishing")
        print("3. Quebra de Senha por Força Bruta")
        print("0. Sair")

        # Obter a escolha do usuário
        escolha = input("\nEscolha uma opção: ")

        # Executar a opção escolhida
        if escolha == '1':
            sms_spam()
        elif escolha == '2':
            link_phishing()
        elif escolha == '3':
            quebra_senha()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            input("Opção inválida! Pressione Enter para continuar...")

# Executar o menu principal
if __name__ == "__main__":
    menu()
