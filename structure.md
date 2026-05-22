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

|===###---| Verificar se as citações fazem sentido.

Os sensores ópticos baseados em ressonância plasmônica localizada de superfície, conhecidos como sensores LSPR (Localized Surface Plasmon Resonance), têm recebido grande destaque nas últimas décadas devido à sua elevada sensibilidade, rapidez de resposta e capacidade de detectar substâncias em baixas concentrações. Essas características tornam essa tecnologia especialmente promissora para aplicações em biossensoriamento, monitoramento ambiental e diagnóstico biomédico. Em geral, sensores ópticos destinados à detecção biológica podem ser classificados em metodologias baseadas em ressonâncias internas e metodologias fundamentadas na amplificação de sinais externos. Dentro do primeiro grupo, os dispositivos LSPR se destacam pela eficiência e simplicidade operacional [9,10].

O funcionamento dos sensores LSPR está associado à interação entre a radiação eletromagnética incidente e nanoestruturas metálicas cujas dimensões são menores que o comprimento de onda da luz utilizada na excitação. Quando iluminadas, essas nanoestruturas apresentam um fenômeno de ressonância plasmônica localizada, produzindo um pico característico de absorção no espectro óptico do dispositivo. A posição espectral dessa ressonância é altamente dependente das propriedades dielétricas do meio ao redor da nanoestrutura. Dessa forma, pequenas alterações nas proximidades do sensor, como a presença de moléculas, vírus, bactérias ou biomarcadores, provocam deslocamentos detectáveis na frequência ou no comprimento de onda de ressonância, permitindo a identificação da interação biológica ocorrida [10].

Uma das principais vantagens dos sensores LSPR está relacionada à elevada sensibilidade da ressonância localizada às mudanças no índice de refração do ambiente próximo à superfície metálica. Isso possibilita a detecção de concentrações extremamente baixas de analitos, característica essencial em aplicações biomédicas e diagnósticos precoces. Além disso, a forte localização espacial do campo eletromagnético nas vizinhanças das nanoestruturas metálicas favorece a interação direta com as partículas de interesse, aumentando a eficiência do processo de sensoriamento.

Os sensores LSPR também apresentam vantagens importantes em relação aos sensores SPR convencionais (Surface Plasmon Resonance). Embora ambas as tecnologias sejam fundamentadas em fenôenos plasmônicos e possuam elevada sensibilidade, os dispositivos SPR normalmente requerem configurações ópticas mais complexas, envolvendo prismas e mecanismos de controle angular para o acoplamento da luz incidente. Como consequência, esses sistemas tornam-se mais suscetíveis a variações mecânicas, térmicas e ambientais, como alterações de temperatura, pressão e desalinhamentos ópticos, fatores que podem comprometer a estabilidade e a precisão das medições [12].

Em contraste, os sensores LSPR utilizam nanoestruturas metálicas localizadas, eliminando a necessidade de prismas e sistemas ópticos sofisticados para excitação da ressonância. Essa característica reduz significativamente a complexidade experimental do sistema de medição, tornando os dispositivos mais compactos, robustos e menos sensíveis a perturbações externas. A simplificação da montagem experimental também contribui para a redução de custos e para a possibilidade de miniaturização dos sensores, favorecendo o desenvolvimento de plataformas portáteis e de baixo consumo energético.

Além disso, a resposta espectral dos sensores LSPR depende diretamente de parâmetros como geometria das nanoestruturas, propriedades ópticas dos materiais empregados e condições do meio ao redor do dispositivo. Isso oferece grande flexibilidade de projeto, permitindo a otimização das características do sensor para diferentes aplicações específicas. Dessa forma, a tecnologia LSPR apresenta grande potencial para o desenvolvimento de biossensores altamente sensíveis, compactos e adequados para aplicações em tempo real, consolidando-se como uma alternativa promissora para sistemas avançados de detecção biológica [9,10,12].


Entre as técnicas ópticas baseadas na amplificação de sinais externos, destaca-se a espectroscopia Raman intensificada por superfície, conhecida como SERS (Surface Enhanced Raman Spectroscopy). Essa metodologia é amplamente reconhecida por sua elevada precisão e capacidade de identificação molecular, sendo utilizada em aplicações relacionadas à caracterização química, análise biológica e detecção de substâncias em baixas concentrações [10].

O princípio de funcionamento das medidas SERS baseia-se na interação entre um feixe laser incidente e a amostra analisada. Normalmente, são utilizados lasers com comprimentos de onda na faixa de 633 nm ou 785 nm, capazes de excitar modos vibracionais das moléculas presentes na amostra. Como consequência dessa interação, são gerados sinais ópticos em diferentes comprimentos de onda, formando espectros característicos associados à estrutura molecular do material analisado. Esses espectros funcionam como uma espécie de assinatura óptica da molécula, uma vez que cada substância apresenta padrões espectrais específicos relacionados às suas ligações químicas e propriedades estruturais [16].

Uma das principais vantagens da técnica SERS é sua elevada seletividade. Como os sinais Raman estão diretamente relacionados às vibrações moleculares, a técnica permite identificar substâncias com alto grau de precisão, inclusive fornecendo informações relevantes sobre a composição química e a organização estrutural das moléculas analisadas. Essa característica faz com que a espectroscopia SERS seja considerada uma ferramenta extremamente poderosa para análises qualitativas em aplicações biomédicas, farmacêuticas e químicas [10].

Entretanto, apesar da alta precisão analítica, a utilização de sistemas SERS apresenta limitações importantes quando consideradas aplicações voltadas ao biossensoriamento prático e ao monitoramento quantitativo de analitos. Diferentemente dos sensores LSPR, nos quais o deslocamento espectral da ressonância pode ser diretamente relacionado à concentração do analito, as medidas SERS são predominantemente qualitativas. Dessa forma, embora seja possível identificar a presença de determinadas moléculas com grande confiabilidade, a técnica apresenta dificuldades para realizar medições quantitativas simples e diretas da concentração das substâncias presentes na amostra.

Além disso, os sistemas experimentais empregados em espectroscopia SERS geralmente demandam equipamentos sofisticados e de elevado custo, incluindo fontes laser de alta estabilidade, espectrômetros de precisão e sistemas ópticos complexos para aquisição e processamento dos sinais. A operação desses dispositivos também exige profissionais especializados e condições experimentais cuidadosamente controladas, fatores que dificultam a implementação da técnica em aplicações portáteis, de baixo custo ou voltadas ao uso em larga escala.

Dessa forma, embora a espectroscopia SERS apresente excelente capacidade de identificação molecular e elevada sensibilidade analítica, suas limitações relacionadas à complexidade experimental, ao custo operacional e à dificuldade de obtenção de informações quantitativas tornam essa abordagem menos adequada para aplicações que demandam sensores compactos, simples, rápidos e facilmente integráveis a plataformas de diagnóstico em tempo real [10,16].

Os dispositivos utilizados em sensores LSPR podem ser desenvolvidos em diferentes geometrias e configurações estruturais, sendo que as propriedades ópticas e a sensibilidade do sensor dependem diretamente do formato, das dimensões e da organização das nanoestruturas metálicas empregadas. Entre as geometrias mais exploradas na literatura destacam-se os nano bastões de ouro, conhecidos como gold nanorods, devido à elevada capacidade de confinamento do campo eletromagnético e à grande sensibilidade das suas ressonâncias plasmônicas às alterações no meio ao redor da estrutura [15].

Os nanorods apresentam elevada versatilidade experimental, podendo ser dispersos diretamente em soluções contendo a amostra de interesse. Nessa configuração, as moléculas presentes no meio interagem com a superfície das nanoestruturas metálicas, promovendo alterações no índice de refração local e consequentemente deslocamentos no pico de ressonância plasmônica. Esse deslocamento espectral, frequentemente observado como um redshift da ressonância, constitui o principal mecanismo de detecção do sensor. Trabalhos recentes demonstraram resultados promissores utilizando nanorods para a detecção de antígenos associados a vírus como COVID-19 e dengue, evidenciando o potencial dessa tecnologia em aplicações biomédicas e diagnósticos rápidos [6].

Apesar das vantagens relacionadas à simplicidade de utilização e à alta sensibilidade, os sensores baseados em nanorods dispersos em solução apresentam limitações relacionadas à reutilização do dispositivo. Como as nanoestruturas se encontram dispersas dentro da amostra biológica, todo o material precisa ser descartado após a realização da medida, caracterizando um sistema essencialmente de uso único. Essa característica pode aumentar custos operacionais e dificultar aplicações que demandem múltiplas análises utilizando o mesmo dispositivo.

Em contrapartida, outras arquiteturas de sensores LSPR utilizam nanoestruturas metálicas fixadas sobre substratos sólidos, formando dispositivos mais estáveis e reutilizáveis conhecidos como Metassuperfícies Plasmônicas. Entre essas configurações destacam-se estruturas compostas por nano discos de ouro depositadas sobre substratos metálicos. Nesse tipo de dispositivo, a amostra é posicionada sobre a superfície do sensor e a presença das moléculas alvo provoca alterações locais no índice de refração, produzindo deslocamentos espectrais semelhantes aos observados em sistemas baseados em nanorods. Entretanto, diferentemente dos sensores dispersos em solução, os dispositivos fixos podem ser submetidos a processos de limpeza utilizando solventes apropriados, permitindo sua reutilização em diferentes ciclos de medição.

Além da possibilidade de reutilização, sensores LSPR baseados em substratos fixos apresentam vantagens relacionadas à integração tecnológica. Estudos recentes demonstram que essas plataformas podem ser incorporadas a sistemas microfluídicos, possibilitando o desenvolvimento de dispositivos compactos e automatizados para aplicações em diagnóstico no ponto de atendimento, conhecidos como sistemas point-of-care [9]. Essa integração favorece a miniaturização dos biossensores, reduz o volume de amostra necessário para análise e contribui para a realização de testes rápidos, portáteis e de baixo custo, características particularmente relevantes em aplicações clínicas e monitoramento de doenças infecciosas.

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