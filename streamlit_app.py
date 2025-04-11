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

# Função para salvar os dados no banco
def salvar_dados(dados):
    conn = conectar_banco()
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

# Função para buscar dados do banco
def buscar_dados():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentos")
    dados = cursor.fetchall()
    conn.close()
    return dados

# Função para atualizar dados no banco
def atualizar_dados(id, campo, novo_valor):
    conn = conectar_banco()
    cursor = conn.cursor()
    consulta = f"UPDATE agendamentos SET {campo} = ? WHERE id = ?"
    cursor.execute(consulta, (novo_valor, id))
    conn.commit()
    conn.close()

# Função para exibir os registros em formato de tabela
def exibir_dados():
    dados = buscar_dados()
    if dados:
        st.write("### Registros Salvos")
        colunas = [
            "ID", "Matrícula", "Nome", "Telefone", "Email Logado", "Email Solicitante",
            "Órgão", "Município Partida", "Bairro Partida", "Rua Partida", "Número Partida",
            "Município Destino", "Bairro Destino", "Rua Destino", "Número Destino",
            "Existe Pernoite", "Qtd Pernoite", "Data Retorno", "Tipo Veículo",
            "Nome Responsável", "Matrícula Responsável", "Email Responsável"
        ]
        st.dataframe(
            [{col: valor for col, valor in zip(colunas, linha)} for linha in dados],
            use_container_width=True
        )
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

# Função para editar um registro
def editar_dados():
    dados = buscar_dados()
    if dados:
        st.write("### Editar Registro")
        ids = [linha[0] for linha in dados]
        id_selecionado = st.selectbox("Selecione o ID do registro para editar", ids)

        if id_selecionado:
            registro = next((linha for linha in dados if linha[0] == id_selecionado), None)
            if registro:
                campo_selecionado = st.selectbox(
                    "Selecione o campo para editar",
                    [
                        "matricula", "nome", "telefone", "email_logado", "email_solicitante",
                        "orgao_logado", "municipio_partida", "bairro_partida", "rua_partida",
                        "numero_partida", "municipio_destino", "bairro_destino", "rua_destino",
                        "numero_destino", "existe_pernoite", "qtd_pernoite", "data_retorno",
                        "tipo_veiculo", "nome_responsavel", "matricula_responsavel", "email_responsavel"
                    ]
                )
                novo_valor = st.text_input(f"Novo valor para {campo_selecionado}")
                if st.button("Salvar Alteração"):
                    atualizar_dados(id_selecionado, campo_selecionado, novo_valor)
                    st.success("Registro atualizado com sucesso!")
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

# Dicionário de municípios e bairros (simplificado; adicione mais conforme necessário)
municipios_bairros = {
    "Rio de Janeiro": ["Botafogo", "Copacabana", "Ipanema", "Tijuca"],
    "Niterói": ["Icaraí", "Santa Rosa", "Ingá"],
    "Duque de Caxias": ["Centro", "Jardim Gramacho", "Saracuruna"],
    # Adicione outros municípios e bairros aqui
}

# Lista de municípios
municipios_rj = list(municipios_bairros.keys())

# Função para exibir o formulário
def exibir_formulario():
    st.write("### Enviar Novo Formulário")

    matricula = st.text_input("Matrícula do Solicitante")
    nome = st.text_input("Nome do Solicitante")
    telefone = st.text_input("Telefone do Solicitante")
    email_logado = st.text_input("E-mail Logado (Office)")
    email_solicitante = st.text_input("E-mail do Solicitante")
    orgao_logado = st.text_input("Órgão Usuário Logado")

    municipio_partida = st.selectbox("Município de Partida", municipios_rj)
    bairro_partida = st.selectbox("Bairro de Partida", municipios_bairros.get(municipio_partida, []))
    rua_partida = st.text_input("Rua (Endereço de Partida)")
    numero_partida = st.text_input("Número (Endereço de Partida)")

    municipio_destino = st.selectbox("Município de Destino", municipios_rj)
    bairro_destino = st.selectbox("Bairro de Destino", municipios_bairros.get(municipio_destino, []))
    rua_destino = st.text_input("Rua (Endereço de Destino)")
    numero_destino = st.text_input("Número (Endereço de Destino)")

    existe_pernoite = st.selectbox("Existe Pernoite?", ["Sim", "Não"])
    qtd_pernoite = st.number_input("Quantidade de Pernoites", min_value=0, step=1)
    data_retorno = st.date_input("Data de Retorno do Pernoite")
    tipo_veiculo = st.text_input("Tipo de Veículo")

    nome_responsavel = st.text_input("Nome do Responsável")
    matricula_responsavel = st.text_input("Matrícula do Responsável")
    email_responsavel = st.text_input("E-mail do Responsável")

    if st.button("Enviar"):
        if not matricula or not nome or not telefone or not email_logado or not municipio_partida:
            st.error("Por favor, preencha todos os campos obrigatórios!")
        else:
            dados = (
                matricula, nome, telefone, email_logado, email_solicitante, orgao_logado,
                municipio_partida, bairro_partida, rua_partida, numero_partida,
                municipio_destino, bairro_destino, rua_destino, numero_destino,
                existe_pernoite, qtd_pernoite, str(data_retorno), tipo_veiculo,
                nome_responsavel, matricula_responsavel, email_responsavel
            )
            salvar_dados(dados)
            st.success("Formulário enviado com sucesso e salvo no banco de dados!")

# Função principal para o menu
def main():
    criar_tabela()

    st.title("Sistema de Agendamento")

    menu = st.sidebar.radio("Menu", ["Consultar Dados", "Editar Dados", "Enviar Novo Formulário"])

    if menu == "Consultar Dados":
        exibir_dados()

    elif menu == "Editar Dados":
        editar_dados()

    elif menu == "Enviar Novo Formulário":
        exibir_formulario()

# Executa o app
if __name__ == "__main__":
    main()
