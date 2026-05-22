# Task Manager API

## Descrição

Projeto desenvolvido como parte da adoção de boas práticas com Git na empresa fictícia TechNova Solutions.

O sistema simula um gerenciador de tarefas com operações básicas de CRUD:

* Criar tarefas
* Listar tarefas
* Atualizar tarefas
* Deletar tarefas

O foco principal do projeto é a aplicação de um fluxo profissional de versionamento com Git.

---

## Tecnologias utilizadas

* Python (arquivo base `main.py`)
* Git e GitHub

---

## Como executar

1. Clone o repositório:

```
git clone https://github.com/davidemarcos01/task-manager-api.git
```

2. Acesse a pasta:

```
cd task-manager-api
```

3. Execute:

```
python main.py
```

---

## Estratégia de Branches

O projeto segue um modelo inspirado no Git Flow:

* `master` → produção
* `develop` → integração
* `feature/*` → desenvolvimento de funcionalidades
* `hotfix/*` → correções urgentes

---

## Fluxo de Desenvolvimento

1. Criar branch a partir de `develop`
2. Desenvolver funcionalidade
3. Realizar commits semânticos
4. Abrir Pull Request
5. Merge na `develop`
6. Release para `master`

---

## Padrão de Commits

* `feat:` nova funcionalidade
* `fix:` correção de bug
* `docs:` documentação
* `refactor:` melhoria interna

---

## Versionamento

O projeto segue versionamento semântico:

* `v1.0.0` → versão inicial
* `v1.0.1` → correção de bug (hotfix)

---

## Estrutura do Projeto

```
task-manager-api/
│
├── main.py
├── README.md
└── .gitignore
```

---

## Autor

Davi Andrade De Marcos
