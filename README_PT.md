# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator é um script Python projetado para gerar dados simulados para os atributos de Usuário e Grupo do Active Directory. Ele visa facilitar os testes e a demonstração dos processos de extração de dados, ao mesmo tempo que mantém a confidencialidade usando dados simulados em vez de informações reais do usuário.

## Pré-requisitos

Para funcionar corretamente, este script requer os seguintes pré-requisitos:
1. Python estar instalado na máquina que o executa. A versão usada para desenvolver este script é a 3.12.2. Recomenda-se usar uma versão a partir da 3.6.
2. Os seguintes módulos devem estar instalados:
    a. pandas:
        Esta biblioteca fornece estruturas de dados e ferramentas de análise de dados.
    b. configparser:
        Este módulo permite trabalhar com arquivos de configuração no formato INI.
    c. Faker:
        Esta biblioteca gera dados falsos, como nomes, endereços, números de telefone, etc.
    d. random ou random2:
        Estes módulos fornecem funções para gerar números aleatórios.
    e. math:
        Este módulo fornece um conjunto de funções matemáticas padrão, como funções trigonométricas, exponenciais, logarítmicas, etc.
    f. unidecode:
        Este módulo permite a transliteração de strings Unidecode em ASCII.

Os módulos configparser, random e math normalmente são incluídos no Python.
Os módulos pandas, Faker e unidecode são pacotes externos.

## Recursos

- Gera dados aleatórios para simular a extração de atributos de contas do Active Directory (AD).
- Ajuda a demonstrar os processos de extração de dados sem revelar informações reais do usuário.
- Permite testar e verificar a coerência dos dados entre as contas do AD e as extrações de recursos humanos (RH).
- Destaca anomalias e sugere modificações para melhorar a segurança no servidor ADUC.

## Uso

1. Clone ou baixe o repositório para a sua máquina local.
2. Duplique o arquivo parameters_[XX].ini correspondente ao seu idioma e renomeie-o simplesmente para parameters.ini.
3. Personalize o arquivo parameters.ini para definir configurações específicas para o processo de geração de dados.
4. Execute o script HR-ADUC-Datasimulator.py para gerar dados simulados.
5. Analise a saída e use-a para fins de teste, demonstração ou melhoria da segurança.

## Licença

HR-ADUC-Datasimulator está licenciado sob a GNU Lesser General Public License v3.0 (LGPL-3.0). Você pode usar, modificar e distribuir este script de acordo com os termos da licença.

Para mais detalhes, consulte o arquivo [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE).

## Contribuições

Contribuições para este projeto são bem-vindas. Se você encontrar problemas, tiver sugestões para melhorias ou quiser contribuir com novos recursos, abra um problema ou envie uma solicitação de pull no GitHub.

## Aviso Legal

Este script é fornecido "no estado em que se encontra", sem qualquer garantia ou garantia de qualquer tipo. Use por sua própria conta e risco.

## Autor

Stéphane-Hervé

## Contato

Para perguntas, feedback ou suporte, entre em contato com https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues.
