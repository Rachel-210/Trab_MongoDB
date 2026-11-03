import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conectando ao MongoDB Atlas 
MONGO_URI = "mongodb+srv://liastudy12_db_user:PaPBKGVs6ncdXjfl@cluster0.xs7cwtn.mongodb.net"

try:
    client = MongoClient(MONGO_URI)
    db = client["ifood_db"]
    collection = db["cardapio"]
    client.admin.command('ping')
    print(" Conexão com o MongoDB Atlas estabelecida com sucesso!\n")
except Exception as e:
    print(f" Erro ao conectar ao MongoDB: {e}")
    exit()

# --- 1. CREATE (Cadastrar Registro) ---
def cadastrar_prato():
    print("\n--- CADASTRAR NOVO PRATO ---")
    nome = input("Nome do prato/lanche: ")
    restaurante = input("Nome do restaurante: ")
    categoria = input("Categoria (ex: Lanches, Pizza, Japonesa, Sobremesa): ")
    preco = float(input("Preço (R$): "))
    disponivel = input("Disponível agora? (s/n): ").lower() == 's'

    documento = {
        "nome": nome,
        "restaurante": restaurante,
        "categoria": categoria,
        "preco": preco,
        "disponivel": disponivel
    }

    resultado = collection.insert_one(documento)
    print(f" Prato cadastrado com sucesso! ID: {resultado.inserted_id}")

# --- 2. READ (Consultar Registros e Filtros) ---
def consultar_pratos():
    print("\n--- CONSULTAR CARDÁPIO ---")
    print("1. Listar todos os pratos")
    print("2. Filtrar por Categoria")
    print("3. Filtrar por Preço Máximo")
    opcao = input("Escolha uma opção de consulta: ")

    query = {}
    if opcao == '2':
        cat = input("Digite a categoria desejada: ")
        query = {"categoria": {"$regex": cat, "$options": "i"}} 
    elif opcao == '3':
        max_preco = float(input("Digite o preço máximo (R$): "))
        query = {"preco": {"$lte": max_preco}}
    elif opcao != '1':
        print("Opção inválida. Mostrando todos:")

    pratos = list(collection.find(query))
    
    if not pratos:
        print("\n Nenhum prato encontrado.")
        return

    print(f"\n--- ENCONTRADOS {len(pratos)} ITEM(NS) ---")
    for p in pratos:
        status_txt = "Disponível" if p.get('disponivel', True) else "Indisponível"
        print(f"ID: {p['_id']} | {p['nome']} ({p['restaurante']}) - Cat: {p['categoria']} | R$ {p['preco']:.2f} [{status_txt}]")

# --- 3. UPDATE (Atualizar Registro) ---
def atualizar_prato():
    print("\n--- ATUALIZAR PRATO ---")
    consultar_pratos()
    
    id_str = input("\nDigite o ID do prato que deseja atualizar: ")
    try:
        obj_id = ObjectId(id_str)
    except:
        print(" ID inválido.")
        return

    prato = collection.find_one({"_id": obj_id})
    if not prato:
        print(" Prato não encontrado.")
        return

    print(f"Editando: {prato['nome']} (Deixe em branco para manter o valor atual)")
    
    novo_nome = input(f"Novo nome [{prato['nome']}]: ") or prato['nome']
    novo_preco_str = input(f"Novo preço [R$ {prato['preco']}]: ")
    novo_preco = float(novo_preco_str) if novo_preco_str else prato['preco']
    
    nova_disp_str = input("Disponível? (s/n, deixe em branco para manter): ").lower()
    if nova_disp_str == 's':
        nova_disp = True
    elif nova_disp_str == 'n':
        nova_disp = False
    else:
        nova_disp = prato.get('disponivel', True)

    collection.update_one(
        {"_id": obj_id},
        {"$set": {
            "nome": novo_nome,
            "preco": novo_preco,
            "disponivel": nova_disp
        }}
    )
    print(" Prato atualizado com sucesso!")

# --- 4. DELETE (Excluir Registro) ---
def deletar_prato():
    print("\n--- EXCLUIR PRATO ---")
    consultar_pratos()
    
    id_str = input("\nDigite o ID do prato que deseja remover: ")
    try:
        obj_id = ObjectId(id_str)
    except:
        print(" ID inválido.")
        return

    resultado = collection.delete_one({"_id": obj_id})
    if resultado.deleted_count > 0:
        print(" Prato removido do cardápio com sucesso!")
    else:
        print(" Prato não encontrado.")

# --- MENU PRINCIPAL ---
def main():
    while True:
        print("\n==============================")
        print("   SISTEMA DE DELIVERY  ")
        print("==============================")
        print("1. Cadastrar novo prato")
        print("2. Consultar cardápio / Filtros")
        print("3. Atualizar prato")
        print("4. Excluir prato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_prato()
        elif opcao == '2':
            consultar_pratos()
        elif opcao == '3':
            atualizar_prato()
        elif opcao == '4':
            deletar_prato()
        elif opcao == '5':
            print("\n Saindo do sistema. Até logo!")
            break
        else:
            print(" Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()