import json


STOCK_FILE = "stock.json"
COINS = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

def carregar_stock():
        with open(STOCK_FILE, "r", encoding="utf-8") as f: #utf-8 só para ter a certeza que ele lê caracteres especiais; f é uma variável que representa o ficheiro aberto e é garantido que o ficheiro fecha corretamente
            return json.load(f) # lÊ o json e transforma para um dicionário em Python
   

def salvar_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f)

def listar_stock(stock):
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for p in stock:
        print(f"{p['cod']} {p['nome']} {p['quant']} {p['preco']}")

def converter_moeda(lista_moedas):
    saldo = 0
    for m in lista_moedas:
       
        if m in COINS:
            saldo += COINS[m]
        else:
            print(f"Moeda inválida: {m}")
    return saldo

def calcular_troco(saldo):
    moedas = list(COINS.items())
    moedas.sort(key=lambda item: item[1], reverse=True) # lista de pares com o nome da moeda e o seu valor em centimos; 
    troco = {}
    restante = saldo
    for nome, valor in moedas:
        if restante >= valor:
            qtd = restante // valor
            troco[nome] = qtd
            restante -= valor * qtd
    return troco

def main():
    stock = carregar_stock()
    print(f" Stock carregado")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    saldo = 0
    
    while True:
        comando = input(">> ").strip().upper()
        
        if comando == "LISTAR":
            listar_stock(stock)
        
        elif comando.startswith("MOEDA"):
            moedas = comando[5:].split(",")
            saldo += converter_moeda(moedas)
            print(f"maq: Saldo = {saldo}c")
        
        elif comando.startswith("SELECIONAR"):
            codigo = comando[9:].strip()
            produto = next((p for p in stock if p["cod"] == codigo), None)
            if produto is None:
                print("maq: Produto inexistente")
                continue
            preco_c = int(produto["preco"] * 100)
            if produto["quant"] <= 0:
                print("maq: Produto esgotado")
                continue
            if saldo >= preco_c:
                saldo -= preco_c
                produto["quant"] -= 1
                print(f'maq: Pode retirar "{produto["nome"]}"')
                print(f"maq: Saldo = {saldo}c")
            else:
                print(f"maq: Saldo insuficiente")
                print(f"maq: Saldo = {saldo}c; Pedido = {preco_c}c")
        
        elif comando == "SAIR":
            if saldo > 0:
                troco = calcular_troco(saldo)
                troco_str = ", ".join(f"{v}x {k}" for k, v in troco.items() if v > 0)
                print(f"maq: Pode retirar o troco: {troco_str}.")
            print("maq: Até à próxima")
            break
        
        else:
            print("maq: Comando inválido")
    
    salvar_stock(stock)

if __name__ == "__main__":
    main()
