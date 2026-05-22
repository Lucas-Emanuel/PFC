# capa
## titulo
    OTIMIZAÇÃO DE BIOSSENSORES FOTÔNICOS BASEADOS EM RESSONÂNCIA PLASMÔNICA DE SUPERFÍCIE LOCALIZADA UTILIZANDO ALGORÍTIMO GENÉTICO E REDES NEURAIS ARTIFICIAIS.
## autor
    Lucas Emanuel Lobo Costa
## orientador
    Jhonattan Córdoba Ramirez
## co-orientador
    Victoria Dala Pegorara Souto

# resumo
O presente trabalho apresenta um estudo de um método de optimização de dispositivos fotônicos baseados em Ressonância Plasmônica de Superfície Localizada (LSPR) visando o aumento de sensibilidade para aplicações de biossensoriamento. Biossensores baseados em LSPR oferecem a vantagem de serem miniaturizáveis e portáteis devido o seu tamanho diminuto sem comprometer a sensibilidade da analise. O método visa maximizar a energia absorvida pelo dispositivo, que representa uma maior interação entre a fonte de luz e os elétrons livres na superfície do material.
Geralmente métodos numéricos de Diferenças Finitas no Domínio do Tempo (FDTD) são utilizados para a simulação da resposta desse tipo de dispositivo. Porém, essa tarefa requer um esforço computacional enorme, demandando em média de 9m e 21s por simulação. Com o objetivo de acelerar o processo de simulação e tornar viável o uso de algorítimos de optimização já conhecidos, este trabalho apresenta uma abordagem de aproximação utilizando Redes Neurais Artificiais (RNA).
O uso dessa abordagem permitiu uma redução de 90% do tempo gasto com simulações numéricas durante o processo de optimização. Permitindo obter dispositivos com resposta X% melhor do que obtida através de exploração aleatória.

# agradecimentos
# sumário
# lista de figuras
# lista de tabelas

# capítulo 1
## introdução
### 1.1 motivação e justificativa
As doenças infecciosas causadas por bactérias e vírus representam um dos maiores desafios contemporâneos para a saúde pública global, afetando diretamente a qualidade de vida da população, a estabilidade econômica e o funcionamento dos sistemas de saúde. A elevada capacidade de disseminação desses agentes patogênicos, associada ao crescimento populacional, à intensa mobilidade humana e às desigualdades no acesso aos serviços médicos, contribui para a ocorrência frequente de surtos, epidemias e pandemias com impactos em escala mundial. Segundo a Organização Mundial da Saúde (OMS), doenças transmissíveis como tuberculose, hepatites virais, HIV/AIDS, malária e outras infecções continuam entre as principais causas de mortalidade e incapacidade, especialmente em países de baixa e média renda. ([Organização Mundial da Saúde][1])

Além dos danos à saúde humana, essas enfermidades produzem consequências sociais profundas. O aumento das taxas de hospitalização e mortalidade compromete a produtividade da população economicamente ativa, intensifica desigualdades sociais e sobrecarrega sistemas públicos de saúde. Em contextos de surtos infecciosos, comunidades inteiras podem sofrer impactos relacionados à interrupção de atividades educacionais, redução da renda familiar e agravamento de vulnerabilidades sociais. A pandemia de COVID-19 evidenciou de maneira clara como doenças virais podem desestruturar cadeias produtivas, afetar relações de trabalho e ampliar problemas associados à pobreza e à exclusão social. ([Springer Nature][2])

Os impactos econômicos associados às doenças infecciosas também são expressivos. De acordo com a OMS, os custos decorrentes de enfermidades incluem não apenas despesas médicas diretas, como internações, medicamentos e tratamentos prolongados, mas também perdas indiretas relacionadas à redução da produtividade, afastamentos laborais e diminuição do crescimento econômico dos países. ([Organização Mundial da Saúde][3]) Em doenças bacterianas, a crescente resistência antimicrobiana agrava ainda mais esse cenário, elevando os custos hospitalares e dificultando tratamentos convencionais. Estudos recentes apontam que infecções bacterianas resistentes representam um enorme ônus econômico global, exigindo investimentos cada vez maiores em estratégias de prevenção, diagnóstico e controle epidemiológico. ([PubMed][4])

Outro fator preocupante é o aumento da frequência e da severidade de surtos infecciosos nas últimas décadas. Relatórios recentes associados à OMS indicam que epidemias provocadas por vírus e bactérias estão se tornando mais frequentes e mais danosas, impulsionadas por fatores como mudanças climáticas, urbanização acelerada, conflitos armados e intensificação da circulação global de pessoas e mercadorias. ([The Guardian][5]) Esse cenário amplia o risco de emergência de novos patógenos e evidencia a necessidade de desenvolvimento de tecnologias capazes de detectar doenças de forma rápida, precisa e acessível.

Além disso, diversas doenças infecciosas possuem elevada capacidade de disseminação silenciosa, especialmente em seus estágios iniciais, dificultando o controle epidemiológico e favorecendo transmissões em larga escala. A OMS destaca que enfermidades transmitidas por alimentos contaminados por bactérias e vírus, por exemplo, afetam milhões de pessoas anualmente e produzem impactos socioeconômicos significativos devido à pressão exercida sobre os sistemas de saúde, às perdas de produtividade e aos prejuízos em setores como comércio e turismo. ([Organização Mundial da Saúde][6]) Dessa forma, o crescente impacto social, econômico e sanitário das doenças infecciosas reforça a necessidade de avanços científicos e tecnológicos voltados ao diagnóstico precoce e ao monitoramento eficiente dessas enfermidades.

[1]: https://www.who.int/our-work/communicable-and-noncommunicable-diseases-and-mental-health?utm_source=chatgpt.com "Our work: communicable and noncommunicable diseases, and mental health"
[2]: https://link.springer.com/article/10.1186/s12879-024-08993-y?utm_source=chatgpt.com "Socioeconomic impacts of airborne and droplet-borne infectious diseases on industries: a systematic review | BMC Infectious Diseases | Springer Nature Link"
[3]: https://www.who.int/publications/i/item/9789241598293?utm_source=chatgpt.com "WHO guide to identifying the economic consequences of disease and injury"
[4]: https://pubmed.ncbi.nlm.nih.gov/40537271/?utm_source=chatgpt.com "The global economic burden of antibiotic-resistant infections and the potential impact of bacterial vaccines: a modelling study - PubMed"
[5]: https://www.theguardian.com/global-development/2026/may/18/infectious-diseases-hantavirus-ebola-more-frequent-damaging-pandemic-outbreak?utm_source=chatgpt.com "Infectious diseases such as hantavirus and Ebola becoming more frequent and damaging, say experts"
[6]: https://www.who.int/es/health-topics/foodborne-diseases?utm_source=chatgpt.com "Enfermedades de transmisión alimentaria"



### 1.2 objetivos do projeto
### 1.3 estrutura da monografia

# capítulo 2
## revisão teórica ou descrição do processo
### 2.1 conceito X
### 2.2 processo X
### 2.3 instrumentação X
### 2.4 resumo do capítulo

# capítulo 3
## etapas preliminares ou metodologia
### 3.1 tecnica X
### 3.2 resumo do capítulo

# capítulo 4
## resultados
### 4.1 atividades do projeto
### 4.2 requisitos do sistema
### 4.3 desenvolvimento e implementação
### 4.4 testes
### 4.5 resumo do capítulo

# capítulo 5
## conclusões
### 5.1 consideraçãoes finais
### 5.2 propostas de continuidade

# referências bibliofráficas

# apêndice