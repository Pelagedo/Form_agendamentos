import streamlit as st
import sqlite3

# Função para criar o banco de dados e a tabela
def criar_tabela():
    conn = sqlite3.connect('agendamento.db')
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
            municipio_destino TEXT,
            bairro_destino TEXT,
            rua_destino TEXT,
            numero_destino TEXT,
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

# Função para salvar os dados no banco de dados
def salvar_dados(dados):
    conn = sqlite3.connect('agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agendamentos (
            matricula, nome, telefone, email_logado, email_solicitante, orgao_logado,
            municipio_partida, bairro_partida, rua_partida, numero_partida,
            municipio_destino, bairro_destino, rua_destino, numero_destino,
            existe_pernoite, qtd_pernoite, data_retorno, tipo_veiculo,
            nome_responsavel, matricula_responsavel, email_responsavel
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', dados)
    conn.commit()
    conn.close()

# Criação da tabela no banco de dados
criar_tabela()

# Título do Formulário
st.title("Formulário de Agendamento de Veículos")

# Campos do Solicitante
st.header("Dados do Solicitante")
matricula = st.text_input("Matrícula do Solicitante")
nome = st.text_input("Nome do Solicitante")
telefone = st.text_input("Telefone do Solicitante")
email_logado = st.text_input("E-mail Logado (Office)")
email_solicitante = st.text_input("E-mail do Solicitante")
orgao_logado = st.text_input("Órgão Usuário Logado")

# Campos da Partida
st.header("Dados da Partida")
municipio_partida = st.text_input("Município de Partida")
bairro_partida = st.text_input("Bairro de Partida")
rua_partida = st.text_input("Rua (Endereço de Partida)")
numero_partida = st.text_input("Número (Endereço de Partida)")

# Campos do Destino
st.header("Dados do Destino")
municipio_destino = st.text_input("Município de Destino")
bairro_destino = st.text_input("Bairro de Destino")
rua_destino = st.text_input("Rua (Endereço de Destino)")
numero_destino = st.text_input("Número (Endereço de Destino)")

# Informações Adicionais
st.header("Informações Adicionais")
existe_pernoite = st.selectbox("Existe Pernoite?", ["Sim", "Não"])
qtd_pernoite = st.number_input("Quantidade de Pernoites", min_value=0, step=1)
data_retorno = st.date_input("Data de Retorno do Pernoite")
tipo_veiculo = st.text_input("Tipo de Veículo")

# Dados do Responsável
st.header("Dados do Responsável")
nome_responsavel = st.text_input("Nome do Responsável")
matricula_responsavel = st.text_input("Matrícula do Responsável")
email_responsavel = st.text_input("E-mail do Responsável")

# Botão para Enviar
if st.button("Enviar"):
    if not matricula or not nome or not telefone or not email_logado or not municipio_partida:
        st.error("Por favor, preencha todos os campos obrigatórios!")
    else:
        # Preparar os dados para salvar no banco
        dados = (
            matricula, nome, telefone, email_logado, email_solicitante, orgao_logado,
            municipio_partida, bairro_partida, rua_partida, numero_partida,
            municipio_destino, bairro_destino, rua_destino, numero_destino,
            existe_pernoite, qtd_pernoite, str(data_retorno), tipo_veiculo,
            nome_responsavel, matricula_responsavel, email_responsavel
        )
        salvar_dados(dados)
        st.success("Formulário enviado com sucesso e salvo no banco de dados!")
