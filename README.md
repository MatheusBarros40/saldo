# Controle de Gastos

## Sobre o Projeto

O Controle de Gastos é um aplicativo web projetado para ajudar os usuários a gerenciar suas finanças pessoais de maneira eficiente e intuitiva. Com uma interface de usuário amigável, o aplicativo permite que os usuários acompanhem suas receitas e despesas, organizem transações por categorias e visualizem o saldo atual de suas contas.

## Funcionalidades

- **Cadastro de Categorias:** Crie e gerencie categorias para organizar suas transações, como "Aluguel", "Salário", "Alimentação", etc.
- **Registro de Transações:** Adicione suas receitas e despesas, associando-as às categorias correspondentes.
- **Edição e Exclusão:** Atualize ou remova categorias e transações conforme necessário.
- **Visualização de Saldo:** Veja o saldo atualizado automaticamente à medida que transações são adicionadas ou modificadas.
- **Filtragem:** Filtre transações por categoria para uma análise mais detalhada de seus gastos.
- **Paginação:** Navegue por suas categorias e transações de forma paginada para melhor organização e visualização.

## Tecnologias Utilizadas

- **Frontend:**
  - [React](https://reactjs.org/): Uma biblioteca JavaScript para construir interfaces de usuário.
  - [Bootstrap](https://getbootstrap.com/): Um framework front-end para desenvolvimento de aplicações web responsivas e mobile-first.
  - [Axios](https://axios-http.com/): Um cliente HTTP baseado em promessas para o navegador e Node.js.
  - [Date-fns](https://date-fns.org/): Biblioteca moderna de manipulação de datas para JavaScript.
  - [React Number Format](https://www.npmjs.com/package/react-number-format): Componente para formatar números em campos de entrada no React.

- **Backend:**
  - [Django](https://www.djangoproject.com/): Um framework web de alto nível para desenvolvimento rápido em Python.
  - [Django REST Framework](https://www.django-rest-framework.org/): Um poderoso e flexível kit de ferramentas para construir APIs web.
  - [PostgreSQL](https://www.postgresql.org/): Um sistema de gerenciamento de banco de dados relacional poderoso e de código aberto.
  - [Gunicorn](https://gunicorn.org/): Um servidor HTTP WSGI para UNIX.

- **Infraestrutura:**
  - [Docker](https://www.docker.com/): Plataforma para desenvolver, enviar e executar aplicações em contêineres.
  - [Docker Compose](https://docs.docker.com/compose/): Ferramenta para definir e executar aplicações Docker multi-contêiner.

## Como Executar

Para executar o Controle de Gastos localmente, siga estas etapas:

1. Clone o repositório para a sua máquina local.
2. Navegue até o diretório do projeto.
3. Execute `docker-compose up` para iniciar os serviços definidos no `docker-compose.yml`.
4. Acesse `http://localhost:3000` no seu navegador para usar o aplicativo.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Matheus Barros - [matheus40melo@gmail.com](mailto:matheus40melo@gmail.com)
