import streamlit as st
import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect('agendamento.db')

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT,
            nome TEXT,
            telefone TEXT,
            email_logado TEXT,
            email_solicitante TEXT,
            orgao_logado TEXT,
            municipio_partida TEXT,
            bairro_partida TEXT,
            rua_partida TEXT,
            numero_partida TEXT,
            destinos TEXT,
            existe_pernoite TEXT,
            qtd_pernoite INTEGER,
            data_retorno TEXT,
            tipo_veiculo TEXT,
            nome_responsavel TEXT,
            matricula_responsavel TEXT,
            email_responsavel TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para salvar os dados no banco
def salvar_dados(dados):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agendamentos (
            matricula, nome, telefone, email_logado, email_solicitante, orgao_logado,
            municipio_partida, bairro_partida, rua_partida, numero_partida, destinos,
            existe_pernoite, qtd_pernoite, data_retorno, tipo_veiculo, nome_responsavel,
            matricula_responsavel, email_responsavel
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', dados)
    conn.commit()
    conn.close()

# Dicionário de municípios e bairros do estado do Rio de Janeiro
municipios_bairros = {
    "Rio de Janeiro": ["Botafogo", "Copacabana", "Ipanema", "Tijuca"],
    "Niterói": ["Icaraí", "Santa Rosa", "Ingá"],
    "Duque de Caxias": ["Centro", "Jardim Gramacho", "Saracuruna"],
    # Adicione mais municípios e seus bairros aqui
}

# Lista de municípios
municipios_rj = list(municipios_bairros.keys())

# Função para exibir o formulário
def exibir_formulario():
    st.write("### Enviar Novo Formulário")

    # Dados do solicitante
    matricula = st.text_input("Matrícula do Solicitante")
    nome = st.text_input("Nome do Solicitante")
    telefone = st.text_input("Telefone do Solicitante")
    email_logado = st.text_input("E-mail Logado (Office)")
    email_solicitante = st.text_input("E-mail do Solicitante")
    orgao_logado = st.text_input("Órgão Usuário Logado")

    # Dados de partida
    municipio_partida = st.selectbox("Município de Partida", municipios_rj)
    bairro_partida = st.selectbox("Bairro de Partida", municipios_bairros.get(municipio_partida, []))
    rua_partida = st.text_input("Rua (Endereço de Partida)")
    numero_partida = st.text_input("Número (Endereço de Partida)")

    # Destinos
    st.write("### Destinos")
    destinos = []
    numero_destinos = st.number_input("Quantos destinos deseja adicionar?", min_value=1, max_value=10, step=1)
    for i in range(numero_destinos):
        st.subheader(f"Destino {i + 1}")
        municipio_destino = st.selectbox(f"Município de Destino {i + 1}", municipios_rj, key=f"municipio_destino_{i}")
        bairro_destino = st.selectbox(f"Bairro de Destino {i + 1}", municipios_bairros.get(municipio_destino, []), key=f"bairro_destino_{i}")
        rua_destino = st.text_input(f"Rua (Endereço de Destino {i + 1})", key=f"rua_destino_{i}")
        numero_destino = st.text_input(f"Número (Endereço de Destino {i + 1})", key=f"numero_destino_{i}")
        destinos.append({
            "municipio": municipio_destino,
            "bairro": bairro_destino,
            "rua": rua_destino,
            "numero": numero_destino
        })

    # Informações adicionais
    existe_pernoite = st.selectbox("Existe Pernoite?", ["Sim", "Não"])
    qtd_pernoite = st.number_input("Quantidade de Pernoites", min_value=0, step=1)
    data_retorno = st.date_input("Data de Retorno do Pernoite")
    tipo_veiculo = st.text_input("Tipo de Veículo")

    # Dados do responsável
    nome_responsavel = st.text_input("Nome do Responsável")
    matricula_responsavel = st.text_input("Matrícula do Responsável")
    email_responsavel = st.text_input("E-mail do Responsável")

    # Enviar formulário
    if st.button("Enviar"):
        if not matricula or not nome or not telefone or not email_logado or not municipio_partida:
            st.error("Por favor, preencha todos os campos obrigatórios!")
        else:
            # Convertendo os destinos para string para salvar no banco
            destinos_str = str(destinos)
            dados = (
                matricula, nome, telefone, email_logado, email_solicitante, orgao_logado,
                municipio_partida, bairro_partida, rua_partida, numero_partida, destinos_str,
                existe_pernoite, qtd_pernoite, str(data_retorno), tipo_veiculo, nome_responsavel,
                matricula_responsavel, email_responsavel
            )
            salvar_dados(dados)
            st.success("Formulário enviado com sucesso e salvo no banco de dados!")

# Função principal para o menu
def main():
    criar_tabela()

    st.title("Sistema de Agendamento")

    menu = st.sidebar.radio("Menu", ["Consultar Dados", "Editar Dados", "Enviar Novo Formulário"])

    if menu == "Consultar Dados":
        dados = buscar_dados()
        if dados:
            st.write("### Registros Salvos")
            st.write(dados)
        else:
            st.warning("Nenhum dado encontrado.")

    elif menu == "Editar Dados":
        editar_dados()

    elif menu == "Enviar Novo

