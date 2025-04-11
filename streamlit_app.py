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
            municipio_partida, rua_partida, numero_partida, destinos, existe_pernoite,
            qtd_pernoite, data_retorno, tipo_veiculo, nome_responsavel, matricula_responsavel,
            email_responsavel
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', dados)
    conn.commit()
    conn.close()

# Lista de municípios do estado do Rio de Janeiro
municipios_rj = [
    "Angra dos Reis", "Aperibé", "Araruama", "Areal", "Armação dos Búzios", "Arraial do Cabo",
    "Barra do Piraí", "Barra Mansa", "Belford Roxo", "Bom Jardim", "Bom Jesus do Itabapoana",
    "Cabo Frio", "Cachoeiras de Macacu", "Cambuci", "Campos dos Goytacazes", "Cantagalo",
    "Carapebus", "Cardoso Moreira", "Carmo", "Casimiro de Abreu", "Comendador Levy Gasparian",
    "Conceição de Macabu", "Cordeiro", "Duas Barras", "Duque de Caxias", "Engenheiro Paulo de Frontin",
    "Guapimirim", "Iguaba Grande", "Itaboraí", "Itaguaí", "Italva", "Itaocara", "Itaperuna",
    "Itatiaia", "Japeri", "Laje do Muriaé", "Macaé", "Macuco", "Magé", "Mangaratiba", "Maricá",
    "Mendes", "Mesquita", "Miguel Pereira", "Miracema", "Natividade", "Nilópolis", "Niterói",
    "Nova Friburgo", "Nova Iguaçu", "Paracambi", "Paraíba do Sul", "Paraty", "Paty do Alferes",
    "Petrópolis", "Pinheiral", "Piraí", "Porciúncula", "Porto Real", "Quatis", "Queimados",
    "Quissamã", "Resende", "Rio Bonito", "Rio Claro", "Rio das Flores", "Rio das Ostras",
    "Rio de Janeiro", "Santa Maria Madalena", "Santo Antônio de Pádua", "São Fidélis",
    "São Francisco de Itabapoana", "São Gonçalo", "São João da Barra", "São João de Meriti",
    "São José de Ubá", "São José do Vale do Rio Preto", "São Pedro da Aldeia", "São Sebastião do Alto",
    "Sapucaia", "Saquarema", "Seropédica", "Silva Jardim", "Sumidouro", "Tanguá",
    "Teresópolis", "Trajano de Moraes", "Três Rios", "Valença", "Varre-Sai", "Vassouras",
    "Volta Redonda"
]

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
    rua_partida = st.text_input("Rua (Endereço de Partida)")
    numero_partida = st.text_input("Número (Endereço de Partida)")

    # Adicionar vários destinos
    st.write("### Destinos")
    destinos = []
    numero_destinos = st.number_input("Quantos destinos deseja adicionar?", min_value=1, max_value=10, step=1)
    for i in range(numero_destinos):
        st.subheader(f"Destino {i + 1}")
        municipio_destino = st.selectbox(f"Município de Destino {i + 1}", municipios_rj, key=f"municipio_destino_{i}")
        rua_destino = st.text_input(f"Rua (Endereço de Destino {i + 1})", key=f"rua_destino_{i}")
        numero_destino = st.text_input(f"Número (Endereço de Destino {i + 1})", key=f"numero_destino_{i}")
        destinos.append({
            "municipio": municipio_destino,
            "rua": rua_destino,
            "numero": numero_destino
        })

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
            # Convertendo os destinos para string para salvar no banco
            destinos_str = str(destinos)
            dados = (
                matricula, nome, telefone, email_logado, email_solicitante, orgao_logado,
                municipio_partida, rua_partida, numero_partida, destinos_str, existe_pernoite,
                qtd_pernoite, str(data_retorno), tipo_veiculo, nome_responsavel, matricula_responsavel,
                email_responsavel
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

    elif menu == "Enviar Novo Formulário":
        exibir_formulario()

# Executa o app
if __name__ == "__main__":
    main()
