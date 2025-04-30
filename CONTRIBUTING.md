# 🤝 Guia de Contribuição para o ENP

Obrigado por considerar contribuir com o ENP! Este guia fornecerá as informações necessárias para você começar a contribuir com o projeto.

## 📋 Sumário
- [Código de Conduta](#código-de-conduta)
- [Como Contribuir](#como-contribuir)
  - [Reportando Problemas](#reportando-problemas)
  - [Sugerindo Melhorias](#sugerindo-melhorias)
  - [Enviando Pull Requests](#enviando-pull-requests)
- [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
- [Padrões de Código](#padrões-de-código)
- [Recursos Úteis](#recursos-úteis)
- [Agradecimentos](#agradecimentos)

## 📜 Código de Conduta

Este projeto adota um [Código de Conduta](CODE_OF_CONDUCT.md) para garantir um ambiente aberto e acolhedor. Ao participar, você concorda em respeitar este código.

## 🚀 Como Contribuir

### 🐛 Reportando Problemas

Se você encontrar um bug ou tiver uma sugestão, por favor, abra uma [issue](https://github.com/SpecterLTDA/ENP/issues) com:
- Descrição clara e concisa do problema.
- Passos para reproduzir o problema.
- Comportamento esperado.
- Capturas de tela ou logs, se aplicável.

### 💡 Sugerindo Melhorias

Para sugerir uma nova funcionalidade ou melhoria:
- Verifique se já existe uma issue semelhante.
- Descreva a motivação e os benefícios da sugestão.
- Forneça exemplos de uso, se possível.

### 🔧 Enviando Pull Requests

1. **Fork** o repositório e clone-o localmente.
2. Crie uma branch para sua contribuição:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Faça suas alterações com testes e documentação apropriados.
4. Commit suas alterações com mensagens claras:
   ```bash
   git commit -m "Descrição clara da alteração"
   ```
5. Push para o seu fork:
   ```bash
   git push origin minha-contribuicao
   ```
6. Abra um Pull Request no repositório original.

## 🛠️ Configuração do Ambiente de Desenvolvimento

1. Clone o repositório:
   ```bash
   git clone https://github.com/SpecterLTDA/ENP.git
   cd ENP
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🧹 Padrões de Código

- Siga o PEP 8 para estilo de código Python.
- Utilize docstrings para documentar funções e classes.
- Escreva testes para novas funcionalidades.
- Mantenha o código limpo e bem organizado.

## 📚 Recursos Úteis

- [Documentação Oficial do Python](https://docs.python.org/pt-br/3/)
- [Guia de Estilo PEP 8](https://pep8.org/)
- [pytest - Framework de Testes](https://docs.pytest.org/)

## 🙌 Agradecimentos

Agradecemos a todos os colaboradores que dedicam seu tempo e esforço para melhorar o ENP. Seu trabalho é fundamental para o sucesso do projeto!
