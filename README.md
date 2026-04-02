# 🏨 RAITEis Hotel — Sistema de Gerenciamento de Hospedagem

Sistema de gerenciamento hoteleiro desenvolvido em Python com interface textual (CLI), criado como desafio prático do processo seletivo **RAITec 2026.1** da Universidade Federal do Ceará (UFC).

---

## 👥 Equipe

| Nome | Responsabilidade |
|------|-----------------|
| noah Martins | Clientes — cadastro e validação |
| Dvar beriti | Quartos — cadastro e validação |
| ian torquato | Reservas — associar clientes e quartos |
| Jeovani alves | Fluxo do sistema — CLI, login, check-in/out |

---

## 📋 Funcionalidades

- Painel duplo de usuário: **Cliente** e **Funcionário** (acesso por senha)
- Cadastro de clientes e quartos
- Registro e consulta de reservas
- Check-in e check-out
- Controle de status dos quartos (disponível / reservado / ocupado)
- Cálculo automático do valor total da hospedagem
- Base pré-cadastrada com 20+ clientes
- Validação de erros em todas as entradas

---

## 🗂️ Estrutura do Projeto

```
raiteis-grupo-3/
├── main.py        # Entry point e menu principal
├── dados.py       # Estrutura de dados central (compartilhado)
├── clientes.py    # Cadastro e base de clientes
├── quartos.py     # Cadastro e controle de quartos
├── reservas.py    # Lógica de reservas, check-in e check-out
├── interface.py   # Menus CLI e painéis de usuário
└── README.md
```

---

## ▶️ Como executar

**Pré-requisito:** Python 3.8 ou superior instalado.

```bash
# Clone o repositório
git clone https://github.com/Noah-Martins/raiteis-grupo-3.git
cd raiteis-grupo-3

# Execute o sistema
python main.py
```

---

## 🔐 Acesso Funcionário

Para acessar o painel de funcionário, utilize a senha definida pela equipe no arquivo `dados.py`.

---

## 🛠️ Tecnologias

- Python 3
- Estruturas nativas: `dict` e `list`
- Interface: CLI (terminal)

---

> Desafio Prático — RAITec 2026.1 · UFC · Fortaleza, CE