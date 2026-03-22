Projeto de Integração Contínua


Descrição

Este projeto implementa uma API em Python/Flask para cálculo de custos de impressão.

O objetivo principal é demonstrar o uso de Integração Contínua (CI) com testes automatizados, análise de código e empacotamento.


Execução Local

pip install -r requirements.txt

python -m src.api

python -m pytest --cov=src


Pipeline CI/CD

O pipeline automatizado no GitHub Actions executa:

Lint (flake8)

Testes (pytest)

Cobertura de código (pytest-cov)

Segurança (bandit)

Build do pacote (setup.py)


A construção deste projeto buscou simular um fluxo real de Integração Contínua (CI) em um ambiente de desenvolvimento de software. A decisão de separar os testes em três níveis — unitários, integração e fluxo completo — foi essencial para garantir que cada parte da aplicação fosse validada de forma independente. Os testes unitários asseguram que funções isoladas, como cálculos, retornem resultados consistentes; os testes de integração verificam se os diferentes módulos da aplicação se comunicam corretamente, como a API respondendo às requisições; e os testes de fluxo completo simulam o uso real do sistema, garantindo que o comportamento geral seja coerente e confiável.

A ausência de testes nesse tipo de projeto poderia resultar em erros silenciosos, como cálculos incorretos de preço ou falhas de endpoint, que só seriam percebidos em produção. Isso comprometeria tanto a confiabilidade quanto a credibilidade da solução. Ao incluir ferramentas de lint e análise de segurança, mitigamos riscos adicionais: desde problemas de estilo e manutenção até vulnerabilidades básicas que poderiam ser exploradas.

O uso do setup.py e do empacotamento do projeto reforça a ideia de que a aplicação pode evoluir para um produto distribuível, não apenas um protótipo acadêmico. Além disso, o pipeline no GitHub Actions garante que cada alteração seja automaticamente validada, criando um ambiente de desenvolvimento mais seguro e previsível.

Pensando em evolução, este projeto poderia ser expandido para Entrega Contínua (CD), com deploy automático em containers Docker ou ambientes de staging. Isso permitiria que novas versões fossem disponibilizadas rapidamente, sem intervenção manual. Em resumo, o projeto demonstra como práticas de CI/CD reduzem riscos, aumentam a qualidade e aproximam o desenvolvimento acadêmico da realidade profissional.