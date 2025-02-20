import time
import os
from datetime import datetime

# Nome do arquivo que armazenará os tempos de estudo
FILE_NAME = "registro_estudo.txt"

def carregar_sessoes():
    """
    Carrega todas as sessões de estudo salvas no arquivo.
    Retorna uma lista de tuplas no formato (data_hora, duracao).
    """
    sessoes = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                try:
                    data_hora, duracao = line.strip().split(" | ")
                    sessoes.append((data_hora, float(duracao)))
                except ValueError:
                    continue
    return sessoes

def salvar_sessao(data_hora, duracao):
    """
    Salva a data/hora de início e a duração da sessão no arquivo.
    """
    with open(FILE_NAME, "a") as file:
        file.write(f"{data_hora} | {duracao}\n")

def limpar_historico():
    """
    Remove todos os registros de sessões de estudo.
    """
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("Histórico de tempo de estudo apagado com sucesso!")
    else:
        print("Não há histórico para apagar.")

def formatar_tempo(segundos):
    """
    Converte segundos em uma string formatada como:
    'X horas, Y minutos e Z segundos'.
    """
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)
    return f"{horas} horas, {minutos} minutos e {segs} segundos"

def iniciar_sessao():
    """
    Inicia uma sessão de estudo e registra a data/hora de início.
    Retorna a data/hora de início e a duração da sessão em segundos.
    """
    input("Pressione ENTER para iniciar a sessão de estudo...")
    inicio = time.time()
    data_hora_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    print(f"Sessão iniciada em {data_hora_inicio}. Bom estudo!")
    input("Pressione ENTER para finalizar a sessão de estudo...")
    
    fim = time.time()
    duracao = fim - inicio
    print(f"Sessão finalizada. Você estudou por {formatar_tempo(duracao)}.")
    
    return data_hora_inicio, duracao

def main():
    while True:
        print("\n=== Monitor de Tempo de Estudo em Python ===")
        print("1. Iniciar sessão de estudo")
        print("2. Mostrar tempo total de estudo")
        print("3. Limpar histórico de estudo")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            data_hora, duracao = iniciar_sessao()
            salvar_sessao(data_hora, duracao)
        
        elif escolha == "2":
            sessoes = carregar_sessoes()
            if sessoes:
                total = sum(sessao[1] for sessao in sessoes)
                print("\nSessões de estudo:")
                for i, (data_hora, duracao) in enumerate(sessoes, 1):
                    print(f" Sessão {i}: {data_hora} - {formatar_tempo(duracao)}")
                print(f"\nTempo total de estudo: {formatar_tempo(total)}")
            else:
                print("Nenhuma sessão de estudo registrada.")
        
        elif escolha == "3":
            limpar_historico()
        
        elif escolha == "4":
            print("Saindo do monitor. Bom aprendizado!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
