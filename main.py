import networkx as nx 
import matplotlib.pyplot as plt

# Definindo os valores de D1 a D6
D1 = 5
D2 = 1
D3 = 0
D4 = 2
D5 = 6
D6 = 8

# Criando o grafo
G = nx.Graph()

# Definição de nós e arestas com pesos baseados nos valores de D1 a D6
arestas = [
    ("S0","S1", (10+(D6%5))),
    ("S0","S2", (15+(D5%7))),
    ("S1","S2", (8+(D4%4))),
    ("S1","S3", (12+(D3%6))),
    ("S2","S4", (14+(D2%5))),
    ("S2","S5", (9+(D1%6))),
    ("S3","S4", (7+(D5+D6)%5)),
    ("S3","S6", (11+(D4+D5)%6)),
    ("S4","S5", (6+(D3+D4)%4)),
    ("S4","S7", (16+(D2+D3)%7)),
    ("S5","S7", (18+(D1+D2)%8)),
    ("S6","S7", (9+(D5+D1)%5)),
    ("S1","S4", (20+(D6%4))),
]

# Adicionando as arestas ao grafo com pesos
G.add_weighted_edges_from(arestas)

# Confirmação de Arestas e Grafos 
print ("Nós:", list(G.nodes))
print ("")
print ("Arestas:", list(G.edges(data=True)))
print ("")

# Visualização do grafo (Removido da Referência, mas foi importante para o entendimento de alterações de layout)
#elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
#esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

# Definindo a posição dos nós para visualização
pos = nx.spring_layout(G, seed=7)

# nós
nx.draw_networkx_nodes(G, pos, node_color="lightgrey", node_size=700)
nx.draw_networkx_nodes(G, pos,nodelist=["S7"] , node_color="lightcoral",node_size=700)
nx.draw_networkx_nodes(G, pos,nodelist=["S0"] , node_color="lightblue", node_size=700)


# Vértices
nx.draw_networkx_edges(G, pos, width=2)

# Nomeação das Arestas
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
# Nomeação dos Pesos das Arestas
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

# Origem e destino
ORIGEM = "S0"
DESTINO = "S7"

# Verificando pesos negativos
for u, v, dados in G.edges(data=True):
    if dados["weight"] < 0:
        print("Peso negativo encontrado")

# Matriz de adjacência com pesos
nos = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7"]

print("Matriz de adjacência:")
print("    ", nos)

for u in nos:
    linha = []

    for v in nos:
        if G.has_edge(u, v):
            linha.append(G[u][v]["weight"])
        else:
            linha.append(None)

    print(u, linha)

print("")

# Dijkstra
custo, rota = nx.single_source_dijkstra(G, ORIGEM, DESTINO, weight="weight")
dist = nx.single_source_dijkstra_path_length(G, ORIGEM, weight="weight")

print("Custo mínimo:", custo)
print("Rota ótima:", rota)
print("Distâncias:", dist)
print("")

# Prim
arvore_prim = nx.minimum_spanning_tree(G, algorithm="prim", weight="weight")

print("Arestas da árvore de Prim:")
print(list(arvore_prim.edges(data=True)))