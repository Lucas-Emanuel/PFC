## Universidade Federal de Minas Gerais Escola de Engenharia Curso de Graduação em Engenharia de Controle e Automação 

# Desenvolvimento de uma plataforma de diagnóstico para a Paracoccidioidomicose 

## Talles Emanuel Moreira Marques Orientador: Prof. Jhonattan Cordoba Ramirez, Dr. Belo Horizonte, janeiro de 2025 Monografia Desenvolvimento de uma plataforma de diagnóstico para a Paracoccidioidomicose 

## Monografia submetida à banca examinadora designada pelo Colegiado Di-dático do Curso de Graduação em Engenharia de Controle e Automação da Universidade Federal de Minas Gerais, como parte dos requisitos para apro-vação na disciplina Projeto Final de Curso II. 

> Belo Horizonte, janeiro de 2025

i

# Resumo 

O presente trabalho descreve o desenvolvimento de uma plataforma para detecção e me-dição da proteína Pb27r, um antígeno presente no fungo Paracoccidioides brasiliensis. Ametodologia emprega sensores LSPR e um sistema óptico de reflexão para realizar medi-ções do deslocamento do pico de absorção causado pela presença da proteína, permitindo estabelecer uma correlação direta entre o deslocamento observado e sua concentração. A plataforma proposta destaca-se por sua simplicidade, acessibilidade e pelas vantagens do sensor, que incluem a reutilização em diferentes medições e a facilidade de fabricação, vi-abilizada pelo uso de moldes. Essas vantagens, em comparação com outras metodologias, tornam a solução uma opção rápida para o diagnóstico precoce da Paracoccidioidomicose, uma micose que afeta milhares de brasileiros, especialmente os de baixa renda, que muitas vezes não possuem recursos para o tratamento da doença. 

Palavras-chave: Localized Surface Plasmon Resonance (LSPR), Detecção de biomolé-culas, Proteína Pb27r, Paracoccidioidomicose (PCM), Sensores ópticos, Doenças negligen-ciadas, Biossensores. iii 

# Agradecimentos 

Primeiramente, quero agradecer ao meu orientador, Jhonattan Cordoba Ramirez, pela orientação e ensino, e pela preocupação em nos formar e nos incentivar a sermos pesquisa-dores e cientistas independentes, capazes de desenvolver suas proprias pesquisas. Mais que um professor, conheci um amigo e companheiro. Quero agradecer também a Clascidia Aparecida Furtado pela supervisão ao longo do projeto, cuja participação foi essencial em todo o projeto. Foi quem me instruiu e tirou minhas dúvidas sobre biologia e o funcionamento da doença estudada, me levando a luz sobre assuntos que eu tinha nenhum domínio e conhecimento. Também agradeço a CDTN e a FINEP, que por meio do projeto 29994*1 forneceu o apoio financeiro necessário para o desenvolvimento deste projeto. Agradeço a minha família que me apoiou e esteve ao meu lado todos os dias nesta jornada acadêmica. Sou grato pelo país que possuo, que sempre demostraram preocupação pelo meu bem-estar, e nunca me deixou faltar nada. Grato também pelo meu irmão que foi meu companheiro e amigo com quem me diverti muito. A minha amiga Jéssica, pela companhia e pelo apoio e incentivo para que eu continuasse sempre estudando. Pelas muitas ajudas nas disciplinas e trabalhos da faculdade e pela auxílio nas montagens realizadas neste projeto. Agradeço também aos meus amigos e amigas que sempre ajudaram uns aos outros em todos os momentos de dificuldade. Também agradeço aos professores que me ensinaram nesta jornada, e os membros do LP2G que me ajudaram a compreender o incrível mundo da fotônica, em especial o Felipe Moreira, cujos trabalhos desenvolvidos foram as bases para este projeto. Por fim, acima de tudo agradeço a Deus, cuja graça tornou tudo isso possível. Sumário 

Resumo iAgradecimentos iii Lista de Figuras viii 1 Introdução 1

1.1 Motivação e Justificativa . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.2 Objetivos do Projeto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41.3 Estrutura da Monografia . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2 Revisão Teórica 7

2.1 Óptica Geométrica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72.1.1 Colimação de feixe . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2.2 Óptica Ondulatória . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2.2.1 Feixe Gaussiano . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 2.2.2 Filtro espacial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2.2.3 Grade de difração . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.3 Plasmônica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.3.1 Acoplamento por grade de difração . . . . . . . . . . . . . . . . . 18 2.3.2 Nanopartículas e Ressonância Localizada de Plásmons de Superfície (LSPR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 2.3.3 Substrato de Nanopirâmides . . . . . . . . . . . . . . . . . . . . . 19 

3 Etapas Preliminares 21 

3.1 Modelagem do nanodispositivo . . . . . . . . . . . . . . . . . . . . . . . . 21 3.1.1 Simulações . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 3.1.2 Otimização do dispositivo . . . . . . . . . . . . . . . . . . . . . . 22 3.1.3 Fabricação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 3.2 Plataforma de Biossensoriamento . . . . . . . . . . . . . . . . . . . . . . . 24 3.2.1 Montagem óptica . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 3.2.2 Procedimentos para caracterização do dispositivo . . . . . . . . . . 27 3.2.3 Procedimentos para medições biológicas . . . . . . . . . . . . . . 29 3.2.4 Processamento dos dados . . . . . . . . . . . . . . . . . . . . . . . 29 vvi 

SUMÁRIO 

4 Resultados 31 

4.1 Montagem óptica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 4.2 Caracterização do dispositivo . . . . . . . . . . . . . . . . . . . . . . . . . 33 4.3 Medidas biológicas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 4.4 Resumo do Capítulo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39 

5 Conclusões 43 

5.1 Considerações Finais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 5.2 Propostas de Continuidade . . . . . . . . . . . . . . . . . . . . . . . . . . 43 

Referências Bibliográficas 45 Apêndices 46 A Imagens da caracterização 47 

A.1 Seção 4.2 medição inicial de todas matrizes . . . . . . . . . . . . . . . . . 47 A.2 Seção 4.2 processamento dos dados para geração de mapas de calor . . . . 49 A.3 Seção 4.2 mapa de calor do dispositivo NP-A2 . . . . . . . . . . . . . . . . 50 Lista de Figuras 

2.1 Refração em uma superfície esférica, por LibreTexts, disponível sob CC BY 4.0. Fonte: link para a imagem. . . . . . . . . . . . . . . . . . . . . . . . . 92.2 Refração em uma lente esférica, por LibreTexts, disponível sob CC BY 4.0. Fonte: link para a imagem. . . . . . . . . . . . . . . . . . . . . . . . . . . 10 2.3 Representação do telescópio Keperiano. . . . . . . . . . . . . . . . . . . . 12 2.4 Convergência de raios de luz paralelos no plano focal. . . . . . . . . . . . . 15 2.5 Etapas do filtro espacial: (a) imagem original, (b) transformada de Fourier, (c) filtro passa baixa no domínio da frequência, e (d) imagem resultante. . . 16 3.1 Dispositivo de nanopirâmides: (a) Ilustração do dispositivo demostrando as dimensões, onde a representa a altura, b é a base e c é a borda das pirâmi-des. (b) Intensidade de campo elétrico normalizada a 633 nm calculada com base nas variações nas dimensões da pirâmide para determinar a combinação mais apropriada de parâmetros que podem ajudar a atingir a maior intensi-dade de campo. (c) Imagem obtida no Centro de Microscopia da UFMG do dispositivo fabricado. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 3.2 Etapas do processo de fabricação do dispositivo de nanopirâmides. . . . . . 23 3.3 Nomes definidos para cada uma das matrizes. Como pode ser observado ao todo são 22 matrizes de nanopiramides. . . . . . . . . . . . . . . . . . . . 24 3.4 Montagem óptica para medidas de reflexão e absorção. . . . . . . . . . . . 27 4.1 Extração dos dispositivos NP-A1, a esquerda encontra o molde de silício, e a direita a lâmina de ouro após o lift-off . . . . . . . . . . . . . . . . . . . . 31 4.2 Caparação entre o spot com e sem o filtro espacial: (a) lentes objetivas sem 

pinhole , (b) lentes objetivas na mesma posição com cavidade pinhole entre elas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 4.3 Diâmetro mínimo do feixe de luz. . . . . . . . . . . . . . . . . . . . . . . 33 4.4 Espectro de emissão da lâmpada halôgena. . . . . . . . . . . . . . . . . . . 34 4.5 Montagem óptica desenvolvida. (a) Visão lateral da montagem e (b) visão superior. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 4.6 Curva de absorbância variando o ângulo de excitação para a matriz 1-2. . . 35 4.7 Mapa de calor para as medidas com ângulo das matrizes 1-2 e 2-1. . . . . . 36 4.8 Comparação entre dados medidos e resultados simulados: (a) medidas expe-rimentais, (b) amostragem das medidas experimentais nos ângulos de 31 ◦ e

41 ◦ e (c) distribuição do campo elétrico na superfície da nanopirâmide em simulação. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 4.9 Mapa de calor para medidas no dispositivo NP-A1 variando o ângulo azimutal. 39 vii viii 

LISTA DE FIGURAS 

4.10 Absorbância antes e depois da aplicação das amostras biológicas, e lavagem do substrato. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40 4.11 Deslocamento no pico de absorção após a aplicação da amostra na concen-tração de 1:32. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40 4.12 Média do deslocamento do pico de absorção para cada concentração. . . . . 41 A.1 Medidas de absorbância do Dispositivo NP-A1 no ângulo de 38 ◦. . . . . . . 47 A.2 Medidas de absorbância do dispositivo NP-A2 no ângulo de 38 ◦. . . . . . . 48 A.3 Resultados das etapas de processamento de dados: (a) dados filtrados em relação ao comprimento de onda, (b) Dados sem tendências e dêsvios, (c) dados filtrados em relação ao ângulo, (d) dados interpolados. . . . . . . . . 49 A.4 Mapa de calor para dispositivo NP-A2 variando o ângulo de incidencia. . . 50 Capítulo 1 Introdução 

# 1.1 Motivação e Justificativa 

Doenças negligenciadas são doenças que se manifestam majoritariamente em meio a locais e populações de mais baixa renda. Não só é consequência da situação em que esse tipo de população está inserida como contribui para a manutenção da desigualdade social ao reduzir a eficiência, ou em alguns casos, provocar o óbito destes trabalhadores [3]. São endêmicas de países tropicas, sobretudo daqueles em desenvolvido. São exemplos de doenças negligen-ciadas: dengue, doença de Chagas, esquistossomose, malária, tuberculose, hanseníase, entre outras. As estimativas mais recentes da Organização de Saúde (OMS) prevem que mais de 1,7 bilhões de pessoas esteja em risco por causa destas doenças, das quais são provocadas aproximadamente 200 mil mortes anualmente. Além disso, são estimados uma perca anual de mais de 19 milhões de anos de vida ajustados por incapacidade (DALYs - Disability Ad-justed Life Years) [11], uma métrica que ajuda a prever quantos anos de vida saudável são perdidos devido a uma doença, lesão ou morte precoce em uma população. É comum não haver grandes investimentos relacionados as doenças negligenciadas, e quando há financiamento para pesquisa o conhecimento produzido não reflete em novos mé-todos de tratamento, fármacos e vacinas ou métodos para o diagnóstico. O Ministério da Saúde aponta que isto ocorre devido ao baixo interesse da indústria farmacêutica nesse tipo de enfermidade, uma vez que os principais afetados são pessoas de baixa renda, que não dispõem de recursos financeiros para o diagnóstico e compra de medicamentos ou tempo para tratamentos [3]. Apesar disso, o Ministério da Saúde e o Ministerio da Ciência e Tec-nologia investe em pesquisas e campanhas no combate das doenças negligenciadas. Desde 2003 já foram investidos mais de R$ 39 milhões em 140 projetos [3]. Contudo, a maioria dos recursos se direcionam a doenças negligenciadas com mais casos, como a dengue e a tuberculose, o que é lógico, uma vez que afeta mais indivíduos por valor investido, porém, deixa de lado outras enfermidades que também merecem igual atenção. A exemplo temos a paracoccidioidomicose (PCM), uma doença pulmonar causada pelo fungo Paracoccidioides brasiliensis que é a micose sistêmica no Brasil com maior número de óbitos [14]. A PCM ocorre exclusivamente em países da América do Sul e Central, sendo mais co-mum no Brasil, Colômbia e Venezuela. É contraída principalmente por trabalhadores da zona rural através da inalação dos esporos do fungo presente na poeira originada de escava-ção do solo, terraplanagem e manipulação de vegetais. Os pacientes infectados pelos esporos da P. brasiliensis normalmente desenvolvem infecção pulmonar que normalmente se mani-12

CAPÍTULO 1. INTRODUÇÃO 

festa como uma pneumonia aguda, dificultando o diagnóstico, uma vez que o diagnóstico prévio pode erroneamente considerar um caso de pneumonia. A PCM pode ainda provocar infecções na pele, principalmente na região do rosto ou atacar órgãos viscerais como fígado e baço, causando inchaço. Mas está é uma condição menos comum que ocorre quando não há tratamento precoce e em pessoas imunocomprometidas, como portadores de AIDS [7]. Atualmente não medidas de controle disponível, sendo a melhor opção o tratamento precoce e correto dos pacientes para limitar a evolução da doença e até mesmo a regredir [14]. En-tretanto, para o sucesso do tratamento é ideal que a contaminação pelo fungo seja detectada antes da evolução da doença e dos sintomas, o que não ocorre. O diagnóstico da PCM é feito por cultura [7], o que é demorado, pois o crescimento do fungo é lento, levando de 2 a 3 semanas para iniciar seu desenvolvimento em ágar. O fungo P. brasiliensis sintetiza inúmeros antígenos que ativam a resposta imunológica no hospedeiro. Conhecer estes antígenos é de suma importância para entender como a reação do paciente a infecção do PCM. Além disso, estes antígenos são essenciais para a formulação de novas vacinas e fornecem um meio pelo qual ensaios para diagnósticos podem ser reali-zados. Diversos antígenos de P. brasiliensis tem sido estudados [1, 4], entre eles se destaca a proteína Pb27 a qual é amplamente estudada e tem demostrado ser um potencial indutor da resposta imune protetora [2], o que é essencial para o desenvolvimento de vacinas. Também, a proteína Pb27 é um promissor marcador para a detecção da PCM. É notável que a área de sensores ópticos tem ganhado bastante atenção nas últimas dé-cadas, em virtude da sua precisão, velocidade e capacidade de realizar medidas em baixa concentrações [10, 9]. Há inúmeras outras metodologias para realizar as medidas biológicas além da apresentada neste trabalho, mas estes podem ser agrupadas em dois grandes grupos: métodos baseados em ressonâncias internadas, e métodos baseados na amplificação de um sinal externo [10]. A exemplo do primeiro caso há os dispositivos LSPR. Estes dispositivos são normalmente excitados com uma fonte de luz branca, e no sinal refletido ou transmitido é percebido um pico de absorção da luz. Essa absorção ocorre na frequência da luz corres-pondente a ressonância do dispositivo, e está ressonância é fortemente sensível a variações no entorno do dispositivo. Por isto, na presença de uma partícula nas proximidades do dispo-sitivo o pico de absorção sofre um deslocamento na frequência, e este deslocamento indica a presença da partícula medida. Outro representante deste método são os sensores baseados em SPR ( Surface Plasmon Resonance ), os quais possuem funcionamento semelhante ao do LSPR. A principal diferença entre ambos, é que na versão localizada são utilizadas nano-estruturas de metal, cuja dimensão são menores que o comprimento de onda de excitação, nesta dimensões ocorre um fenômeno que aprisiona a onda, por isto a ressonância é dita localizada. Os sensores baseados em SPR apresentam boa sensibilidade para biosensoria-mento, mas sua montagem também é sensível a variações no meio em que está construída, comprometendo a qualidade das medições. Tanto para SPR quanto para LSPR a ressonância depende dos materiais, dimensões e as condições externas próximas, contudo, a montagem do sensor SPR é maior e mais delicada, sendo necessário um prisma para direcionar o sinal de excitação. Isto torna a medida sujeita as variações de temperatura e pressão do prisma e do angulo do feixe de excitação [12]. Os sensores baseados em LSPR por sua vez não sofrem deste problema, uma vez que a montagem para medição é muito mais simples, eliminando os possíveis graus de liberdade nos resultados. Para os métodos de medição por amplificação de um sinal externo, o maior representante são as medidas feitas por SERS ( Surface Enhancement Raman Spectroscopy ). Neste tipo 1.1 Motivação 3de medida é utilizado um laser com comprimento de luz de 633 ou 785 nm. Este feixe a entrar em contato com a amostra excita a produção de picos em outros comprimentos de onda. Estes picos constituem um sinal que é próprio da amostra em análise. Isto faz das medidas SERS um das mais precisas [10] uma vez que cada molécula possui sua curva ca-racterística, agindo como uma assinatura da molécula. Cada pico produzido é consequência das ligações atômicas na molécula, o que pode inclusive fornecer pistas da sua composição química da molécula [16]. Contudo, as medidas SERS são apenas qualitativas, não tendo nenhuma informação sobre a concentração do analito, em contrapartida, as medidas LSPR podem ser utilizadas para medir concentrações, pois o deslocamento do pico de ressonância está diretamente relacionado a concentração do analito. Além disso, os equipamentos neces-sário e a montagem para medidas SERS é muito complexa e custosa, além de exigir pessoal especializado para a operação dos equipamentos. Os dispositivos para medidas LSPR são diversos, e apresentam inúmeras geometrias. A geometria mais largamente utilizada é a de nano bastões de ouro ( nanorods ) [15]. Os na-norods são versáteis e podem ser simplesmente adicionados a uma solução com a amostra em análise. Trabalhos e pesquisas recentes conseguiram detectar antígenos de vírus como o COVID e a dengue utilizando estes nanorods [6]. A detecção da molécula com este tipo de dispositivo se dá pelo redshift do pico de ressonância que ocorre devido à presença da molécula na solução. Contudo, uma vez utilizada precisa ser descartado junto a amostra, fazendo deste dispositivo uma solução de uso único. Em contrapartida, outras geometrias utilizam dispositivos fixos a um substrato, como o utilizado neste trabalho. O dispositivo a ser utilizado é formado por nano pirâmides de ouro fixas a um substrato de ouro. Nesta configuração a amostra é depositada sobre o substrato, onde devido à presença da molécula ocorre o redshift da ressonância assim como ocorre com os nanorods . Porém, para os dis-positivos fixos, ao final da medida o substrato pode ser limpo com solvente, permitindo a reutilização para novas medidas. Adicionalmente, estudos recentes demostraram a possibi-lidade de incorporar dispositivos LSPR de substrato fixo em soluções com microfluídica, o que possibilita desenvolver dispositivos para o teste e diagnóstico no ponto de atendimento (Point-of-care ) [9]. Neste contexto o presente trabalho desenvolveu uma plataforma para a detecção do an-tígeno Pb27. Como a proteína Pb27 é de difícil extração, durante o processo de caracteriza-ção, medição e calibragem dos sensores foram utilizadas amostras da proteína Pb27r. Tanto a Pb27 quanto a Pb27r possuem a mesma estrutura, contudo a Pb27r é a versão recombinante da Pb27, ou seja, se trata de uma versão sintetizada artificialmente. A produção da Pb27r é feita inserindo os genes de P. brasiliensis responsável pela sintetização da proteína Pb27 em uma bactéria especial, a qual sintetizará a proteína recombinante. A detecção da proteína foi feita por meio de nanoestruturas LSPR ( Localized Surface Plasmon Resonance ). A escolha por este tipo de dispositivo se dá pelos avanços recentes nesta área na detecção de moléculas, sobretudo moléculas orgânicas [10]. Por sua vez, pes-quisa realizadas na UFMG tem sido bem sucedidas no desenvolvimento de um nanodisposi-tivo otimizado para a amplificação de sinal Raman [8]. Este trabalho documenta o processo simplificado de fabricação do dispositivo e do molde negativo. que é um dos pontos-chave deste trabalho. Sob o molde negativo uma camada de 175 nm de ouro é depositada, e após a extração por Lift-off o molde fica livre para uma nova deposição. Esta reutilização do molde contribui para que a plataforma desenvolvida neste trabalho seja de mais baixo custo, facilitando a adoção da solução. 4

CAPÍTULO 1. INTRODUÇÃO 

Como consequência dos resultados obtidos durante os anos de iniciação científica, desen-volvimento do PFC e pesquisa em parceria com o CDTN/CNEN cinco publicações científi-cas foram escritas e divulgadas, sendo um artigo na revista ACS Applied Optical Materials [8], um tutorial em processo de publicação pela Analytical Chemistry, e três artigos de confe-rência, um para a FiO e dois para a CLEO, duas importantes conferencias para a área óptica. Todos os resultados obtidos foram possíveis devido à colaboração de diversos pesquisadores das mais diferentes áreas. 

# 1.2 Objetivos do Projeto 

Tendo em vista o exposto acima, este projeto tem por objetivos: a. Desenvolver uma montagem óptica para medidas de absorbância para os comprimen-tos do visível e infravermelho próximo; b. Realizar a caracterização óptica da plataforma de nanoestruturas utilizadas, de modo a encontrar os melhores dispositivos e as melhores regiões para realizar as medidas ópticas; c. Realizar as medidas biológicas com a proteína Pb27r em diferentes concentrações e ajustar a curva de calibração e sensibilidade do sensor utilizado; d. Desenvolver o software de tratamento dos dados coletados para posterior utilização por pessoas que não são da área de fotônica. 

# 1.3 Estrutura da Monografia 

Este trabalho está dividido em cinco capítulos, os quais contemplam a presente introdução, a revisão dos conceitos trabalhados, o desenvolvimento do dispositivo utilizado e da plata-forma de medição, a apresentação dos resultados obtidos e por fim a conclusão. No capítulo 2 é realizada uma revisão sobre os principais conceitos e fenômenos trabalha-dos. Conceitos de física clássica e ondulatória são resgatados para explicar os componentes utilizados na montagem óptica. Também é apresentado os efeitos plasmônicos e suas pro-priedades, como o confinamento da luz em dimensões menores que o seu comprimento de onda, e discutido como os elétrons livres na interface entre metal e dielétrico podem acoplar-se com ondas eletromagnéticas, dando origem às ondas de plásmons .No capítulo 3 é apresentado as metodologias empregadas na criação e fabricação do dis-positivo utilizado. Neste capítulo é apresentado a método de otimização do dispositivo, onde através da variação das dimensões das nano pirâmides de ouro a intensidade do campo elé-trico é maximizada para um determinado comprimento de onda. Além disso, é apresentado um método de fabricação baseado na utilização de um molde de silício, que permite a fa-bricação facilitada de vários dispositivos idênticos. Neste capítulo também é apresentada a montagem construída para medição de absorbância por reflexão da luz, incluindo um filtro para lidar com distúrbios na imagem projetada pelo feixe de luz. São descritas as meto-dologias e procedimentos empregados para a realização de cada medida óptica, com e sem uma amostra biológica. Também são descritos os procedimentos utilizados para a limpeza 1.3 Organização do Trabalho 5do substrato e como essa opção permite a reusabilidade de um mesmo dispositivo para dife-rentes medidas. Por fim, é apresentado o software de processamento dos dados e como os resultados são extraídos a partir dos dados brutos. No capítulo 5 são apresentados os resultados experimentais. Neste capítulo está a mon-tagem óptica construída e a demostração do feixe de luz produzido, e através desta mon-tagem as medidas são realizadas produzindo as curvas de absorbância. Pela caracterização do dispositivo a melhor região de trabalho é escolhida, e nesta região é performada diversas medidas com as amostras de Pb27r em diferentes concentrações. Para cada concentração é observado um deslocamento proporcional, de forma que ao final do capítulo é traçada a curva de calibração do sensor, enfatizando sua sensibilidade e capacidade de detectar a proteína. Por fim, no capítulo 6 são tecidas as conclusões e considerações finais sobre o projeto, bem como os próximos passos a serem desenvolvidos. 6

CAPÍTULO 1. INTRODUÇÃO Capítulo 2 Revisão Teórica 

Este capítulo aborda os fundamentos teóricos necessários para o entendimento dos conceitos abordados neste trabalho. A montagem óptica para as medições foi construída utilizando arranjos de lentes, das quais efeitos são explicados pela óptica geométrica. Além disso, para limpar o feixe produzido pela fonte de luz um filtro espacial foi utilizado, seu funciona-mento consiste em implementar um filtro passa baixa no domínio da frequência, contudo, as lente possuem a propriedade de projetar o domínio da frequência no espaço, o que é me-lhor entendido por meio da óptica ondulatória. Por fim, é explicado como o dispositivo de nanoestruturas consegue acoplar com a luz incidida e gerar ressonâncias. 

# 2.1 Óptica Geométrica 

A óptica geométrica é um modelo físico que descreve a propagação da luz em termos de feixes ou raios. Estes raios são abstrações que aproximam o caminho percorrido pela luz, sendo útil para descrever fenômenos simples, como a interação da luz com lentes ou estru-turas e superfícies muito maiores que o comprimento de onda da luz incidente. Este modelo assume que a luz propaga em linha reta em meios homogêneos, e curva na interface onda há mudança no índice de reflação. Ainda nessa interface o raio de luz pode se dividir em dois, onde uma parte é transmitida para o outro meio, e a outra é refletida, permanecendo no meio inicial. Além da transmissão e reflexão, este modelo físico também aceita a absorção do raio de luz. Cada raio de luz é representado por uma linha ou curva que é perpendicular a frente de onda da luz e colinear à direção de sua propagação. Essas linhas obedecem a duas leis fundamentais da ótica. A primeira é a lei da reflexão, que estabelece que o ângulo de reflexão é igual ao ângulo de incidência da luz em relação ao vetor normal da superfície. A segunda é a lei da refração, que relaciona os ângulos formados com os índices de refração dos dois meios envolvidos. O índice de refração ( n) de um meio é a razão entre a velocidade da luz no vácuo ( c) com a velocidade da luz no meio ( v). Quando a luz incide em uma superfície inclinada, ela é refratada conforme a Lei de Snell: 

n1 sin( θ1) = n2 sin( θ2), (2.1) onde n1 e n2 são os índices de refração do meio inicial e do meio onde o raio adentrou, e θ1

e θ2 são os ângulos de incidência e refração respectivamente. O valor do índice de refração 78

CAPÍTULO 2. REVISÃO TEÓRICA 

depende do material utilizado, como exemplo, o vidro possui índice de refração de 1,52, já o quartzo (material muito utilizado para lentes) possui índice de 1,46. A difração é o princípio por trás do funcionamento das lentes, estas estruturas são projeta-das para desviar feixes de luz, podendo convergir ou divergir estes raios. Diversas geometrias são utilizadas na construção de lentes, sendo as categorias mais utilizada as lentes esféricas e as lentes planas. As lentes esféricas são formadas por duas faces curvas, já as lentes planas possuem uma face curva e uma plana. Neste projeto uma lente é utilizada para coletar o feixe refletido pelo sensor, e esta lente é uma plano-convexa, pois o objetivo é convergir o feixe para dentro da abertura da fibra óptica. Toda lente possui como parâmetro sua distância focal, esta grandeza indica a distância entre o centro óptico da lente até o ponto onde os raios de luz paralelos convergem ou pare-cem divergir. Está distância depende tanto da geometria da lente quanto do índice de refração do material utilizado. Para lentes esféricas a distância focal da lente pode ser deduzida a par-tir da Lei de Snell. Para isso é considerada a imagem formada pela primeira superfície da lente, em seguida esta imagem é utilizada como objeto para a segunda superfície da lente. Para uma única superfície de refração, conforme mostra a Figura 2.1, a equação que rela-ciona as distância até o objeto do, a distância até a imagem di e o raio de curvatura R éderivada a partir da Equação 2.1. Considerando a aproximação para ângulos pequenos onde 

sin( θ) ≈ θ, a Lei de Snell pode ser rescrita como: 

n1θ1 ≈ n2θ2. (2.2) Utilizando o teorema que afirma que o ângulo externo de um triângulo é igual à soma dos dois ângulos internos, a partir da geometria da Figura 2.1 as seguintes relações são extraídas: 

θ1 = α + φ, θ2 = φ − β. 

Inserindo estas expressões na Equação 2.2 obtêm-se: 

n1(α + φ) ≈ n2(φ − β). (2.3) Ainda considerando ângulos pequenos, tais que a curvatura se aproxime de um plano, para este caso as regras de geometria de triângulos retângulos pode ser utilizada e as tangen-tes dos ângulos α, β e φ são aproximadas por: 

tan( α) ≈ hdo

,

tan( β) ≈ hdi

,

tan( φ) ≈ hR .

Novamente, pelos ângulos pequenos a tangente pode ser aproximada por tan (θ) ≈ θ:2.1. ÓPTICA GEOMÉTRICA 9

Figura 2.1: Refração em uma superfície esférica, por LibreTexts, disponível sob CC BY 4.0. Fonte: link para a imagem. 

α ≈ hdo

,β ≈ hdi

,φ ≈ hR .

Substituindo estes ângulos na Equação 2.3 obtêm-se: 

n1

( hdo

+ hR

)

= n2

( hR − hdi

,

)

n1

do

+ n1

R = n2

R − n2

di

,n1

do

+ n2

di

= n2 − n1

R . (2.4) A Equação 2.4 relaciona as distâncias entre o objeto e a imagem projetada por meio de uma superfície esférica simples. Uma lente esférica é formada por duas superfícies esféricas, mas apesar disso a solução para lente da distância entre o objeto e a imagem pode ser encon-trada em duas etapas. Como mostrado na Figura 2.2, a primeira superfície curva projeta uma imagem em Q′, sendo formada estendendo os raios no interior da lente até a convergência em um ponto. No caso mostrado pela figura a imagem é virtual, pois nenhum raio passa pelo ponto Q′. O gráfico formado pela Equação 2.4 para a distância até a imagem ( di) variando a distância até o objeto ( do) é uma hipérbole deslocada para o primeiro quadrante. Dessa forma, quando o objeto está muito próximo da lente, a primeira superfície não consegue convergir os raios, e a distância até a imagem assume valores negativos, o que significa que imagem está à esquerda da superfície. Considerando a distância até o objeto do, a distância até a primeira imagem d′ 

> i

e o raio de curvatura da primeira superfície R1, e aplicando estes valores na Equação 2.4, obtêm-se: 10 

CAPÍTULO 2. REVISÃO TEÓRICA 

Figura 2.2: Refração em uma lente esférica, por LibreTexts, disponível sob CC BY 4.0. Fonte: link para a imagem. 

n1

do

+ n2

d′

> i

= n2 − n1

R1

. (2.5) Tomando a imagem formada pela primeira superfície como objeto da segunda superfície, a imagem em Q é formada. Considerando a distância até essa nova imagem como di e a curvatura da segunda superfície como R2 é obtida a seguinte expressão: 

n2

d′

> o

+ n1

di

= n1 − n2

R2

, (2.6) onde d′ 

> o

é a distância entre a segunda superfície até a primeira imagem, equivalendo a soma de d′ 

> i

e a espessura da lente t. Na aproximação de lentes finas a distância até a imagem é muito maior que a espessura, portanto a espessura pode ser desprezada sem muitas perdas na precisão dos resultados. Além disso, no caso demostrado na Figura 2.2 d′ 

> o

é positivo, mas 

d′ 

> i

é negativo, portanto é necessário adicionar o sinal negativo a igualdade: d′ 

> o

= −d′

> i

. Por outro lado, caso a imagem projetada pela primeira superfície fosse real, ou seja, os feixes convergissem do lado direito da imagem, neste caso a imagem da segunda superfície seria virtual. Isso pode ser melhor observado realizando a propagação inversa dos feixes de luz, o que é possível pela Lei da Simetria Temporal. Nesta situação d′ 

> i

será positivo, por ser uma imagem real, e d′ 

> o

negativo, por ser uma imagem virtual. Em ambas as situações d′ 

> i

e d′

> o

possuem sinal oposto. Substituindo d′ 

> o

por −d′ 

> i

na equação 2.6: 

−n2

d′

> i

+ n1

di

= n1 − n2

R2

, (2.7) Por fim, somando as Equações 2.5 e 2.7 é obtida a seguinte equação: 2.1. ÓPTICA GEOMÉTRICA 11 

n1

do

+ n1

di

+ n2

d′

> i

− n2

d′

> i

= ( n2 − n1)

( 1

R1

− 1

R2

)

,n1

do

+ n1

di

= ( n2 − n1)

( 1

R1

− 1

R2

)

,

1

do

+ 1

di

=

(n2

n1

− 1

) ( 1

R1

− 1

R2

)

. (2.8) No caso específico em que a distância do objeto até a lente tende ao infinito, a fração 1

> do

tende a zero, restando apenas a fração 1 

> di

. Neste caso, a distância até imagem é a distância focal ( f ) da lente. Ainda, considerando que a lente esta envolta por ar, nesta situação o índice de refração n1 pode ser aproximado para 1. Incluindo estas alterações na Equação 2.8, a equação resultante torna-se a equação dos Fabricantes de Lentes ( Lensmaker’s Equation ): 

P = 1

f = ( n − 1) 

[ 1

R1

− 1

R2

]

, (2.9) onde: • P é o poder da lente em desviar a trajetória da luz; • f é a distância focal da lente; • n é o índice de refração do material da lente; • R1 é o raio de curvatura da superfície mais próxima da fonte de luz; • R2 é o raio de curvatura da superfície mais longe da fonte de luz. Os sinais de R1 e R2 indicam se a superfície é convexa ou concava. O sinal é positivo caso o centro da curvatura esteja para a direita e negativo quando está para a esquerda. Se a superfície for plana, o raio da curvatura é infinito, de forma que a fração tenda a zero. Como o lado direito da Equação 2.9 é constante independente do objeto ou imagem estiverem no foco, então a sequinte igualdade pode ser tomada: 

1

do

+ 1

di

= 1

f (2.10) Esta igualdade representa a equação de lentes finas ou delgadas, e permite encontrar a distância até a imagem conhecendo apenas a distância focal da lente. 

Lentes Objetivas 

As lentes objetivas são um tipo de lente projetada para amplificar ou reduzir imagens de objetos. São amplamente utilizadas em microscópios, telescópios e câmeras. Podem ser compostas por uma ou mais lentes, e em alguns casos a distância entre estas lentes pode ser alterado para variar a distância focal ou abertura da objetiva. No geral, possuem distância focal muito pequena, tendo apenas alguns milímetros, mas apesar disso são vendidas com base em magnificação e abertura numérica. É possível relacionar a magnificação e aber-tura numérica com a distância focal, mas está relação necessita de informações adicionais relacionadas a montagem da objetiva. 12 

CAPÍTULO 2. REVISÃO TEÓRICA 

Figura 2.3: Representação do telescópio Keperiano. 

Telescópio Kepleriano 

Lentes podem ser combinadas para construir estruturas mais complexas. O telescópio Ke-pleriano é um caso, onde duas lentes são combinadas para reduzir ou amplificar a imagem de um objeto, como representando na Figura 2.3. Apesar do nome, o telescópio Kepleriano é apenas uma montagem, composta por duas lentes convexas. As lentes são posicionadas de forma que a distância entre elas seja igual a soma das distâncias focais das duas lentes. A relação de magnificação desta montagem é dada por: 

M = d2/d 1 = f2/f 1, (2.11) onde, M é a magnificação, f1 e f2 as distâncias focais da primeira e segunda lente e d1 e d2

os diâmetros dos feixes de entrada e saída respectivamente. 

Dispersão da luz 

É importante pontuar que o índice de refração é dependente do comprimento de onda da luz, e essa relação depende do material utilizado. Cada comprimento de onda possui uma velocidade de propagação diferente para cada material, como consequência, na interface do material cada comprimento de onda sai com um ângulo distinto. Em virtude deste efeito, quando a luz branca atravessa um meio transparente, como o vidro, a luz é decomposta em seus diferentes componentes. Este fenômeno óptico de dispersão da luz é a base para o fun-cionamento de estruturas como o prisma. Neste dispositivo a dispersão da luz é controlada e intensificada. Os usos dos prismas são diversos, sendo um deles o uso na espectrometria para a divisão do sinal nas diferentes frequências. O prisma é uma caso onde a dispersão da luz é um fenômeno desejado, mas este efeito também pode surgir indesejadamente em lentes. Como consequência da Equação 2.9 a variação do índice de refração resulta em uma variação na distância focal. Isto provoca o efeito de aberração cromática, que ocorre quando a lente não consegue focalizar todas as cores no mesmo ponto. A aberração cromática re-sulta em uma imagem com bordas coloridas, e pode ter consequências nas medições ópticas em virtude dessa separação espacial das diferentes frequências da luz. Nesse sentido, lentes planas são mais vantajosas, pois elas não alteram a direção dos raios de luz de forma tão significativa, e por este motivo o efeito de aberração cromática é menos pronunciado quando comparado com lentes esféricas. 2.2. ÓPTICA ONDULATÓRIA 13 

## 2.1.1 Colimação de feixe 

Ao decorrer do capítulo foi citado o caso em que os feixes são paralelos entre si, este tipo de feixe é dito colimado. Na ótica geométrica, um feixe colimado é um conjunto de raios de luz paralelos entre si, que viajam em direções paralelas e não se convergem nem se divergente ao longo de seu percurso. Isso ocorre quando a luz é emitida de uma fonte muito distante ou passa por uma lente ou espelho que a torna paralela, de forma que todos os raios do feixe possuem a mesma direção. Um feixe colimado mantém seu diâmetro e intensidade por longas distâncias, facilitando a construção de montagens ópticas. Além disso, um feixe colimado é focalizado com mais facilidade, sendo compatível com qualquer lente. Como observado na Equação 2.10, apenas quando o feixe de entrada está colimado (objeto no infinito) a imagem é projetada no foco da lente, e quando isto ocorre a intensidade é máxima, pois a área do feixe é mínima. Apesar das vantagens de um feixe colimado, alguns formalismos ópticos como a Óptica Ondulatória consideram que um feixe perfeitamente colimado não pode existir. 

# 2.2 Óptica Ondulatória 

A óptica ondulatória é um modelo físico que estuda o comportamento da luz ao considerá-la como um fenômeno ondulatório. Esse formalismo permite explicar fenômenos como interferência, difração e polarização, que não podem ser compreendidos pelas aproximações da óptica geométrica, que trata a luz como raios. Os fundamentos da óptica ondulatória estão nas equações de Maxwell, que, quando resolvidas, descrevem a luz como uma onda eletromagnética formada pela oscilação mutuamente perpendicular dos campos elétrico e magnético, propagando-se no espaço. Neste modelo, quando a luz passa por uma abertura ou contorna algum obstáculo, ela se espalha, desviando da propagação retilínea prevista pela ótica geométrica. Este fenômeno é a difração, e ele ocorre devido à natureza ondulatória da luz, que permite que as frentes de onda se curvem e interfiram entre si, formando padrões característicos de intensidade luminosa, como franjas claras e escuras. As equações de Maxwell prevem este comportamento, e descrevem como as oscilações dos campos elétrico e magnético interagem com as bordas do obstáculo ou abertura. Este efeito também ocorre quando há uma distribuição desigual das intensidades da luz produzida em uma fonte. Em virtude do comportamento ondulatório da luz, esses pontos de maior intensidade espalham-se formando os mesmos padrões de difração se este perfil de luz houvesse sido gerado por um obstáculo. No infinito, em virtude da difração da luz, toda fonte de luz passa a assumir uma distribuição gaussiana de intensidade. Este feixe é naturalmente produzido por algumas fontes de luz, como alguns lasers. 

## 2.2.1 Feixe Gaussiano 

O feixe gaussiano é um modo Eletromagnético Transversal (TEM), um padrão de radiação no plano perpendicular da propagação da onda, onde nem o campo elétrico, nem o magnético possuem componentes na direção de propagação. É um feixe desejado em experimento ópticos por ser estável ao longo de sua propagação, não sofrendo distorção pela difração de seu perfil de intensidade. Além disso, possui concentração de energia em uma região central bem definida. 14 

CAPÍTULO 2. REVISÃO TEÓRICA 

Os feixes gaussianos são soluções naturais das equações de Maxwell que resultam na seguinte expressão para a amplitude do campo elétrico ao longo do sentido de propagação z:

E(r, z ) = E0 ˆx w0

w(z) exp 

(

− r2

w2(z)

)

exp 

(

−i

(

kz + kr 2

2R(z) − ψ(z)

)) 

,

onde: 1. Parâmetros do Feixe Gaussiano: 

• E0: amplitude máxima no centro do feixe no plano focal ( z = 0 ). • ˆx: sentido de polarização, assumindo polarização na direção x.• r: distância radial a partir do eixo do feixe. • z: posição ao longo do eixo de propagação do feixe. 2. Tamanho do Feixe: 

• w(z) = w0

√

1 + 

( zzR

)2

: largura do feixe em função da posição z, onde w0 é o raio na cintura do feixe (ponto mais estreito) e zR é o comprimento de Rayleigh (zR = πw 20 

> λ

). 3. Curvatura da Frente de Onda: 

• R(z) = z

[

1 + (zR

> z

)2]

: raio de curvatura da frente de onda em z.4. Fase de Gouy: 

• ψ(z) = arctan 

( zzR

)

: fase adicional devido à propagação gaussiana. 5. Número de Onda: 

• k = 2πλ : número de onda da luz, onde λ é o comprimento de onda. Da mesma maneira, a expressão para o campo magnético pode ser encontrada, mas como o modo de propagação é TEM, então o sentido de polarização do campo magnético deve ser ortogonal ao de campo elétrico. A relação entre os campos para o feixe gaussiano é dada por: 

H(r, z ) = ˆ y 1

η Ex(r, z )

onde η é a impedância característica do meio no qual o feixe está se propagando. 2.2. ÓPTICA ONDULATÓRIA 15 

Figura 2.4: Convergência de raios de luz paralelos no plano focal. 

## 2.2.2 Filtro espacial 

O filtro espacial é uma construção óptica que permite eliminar ruídos em feixes de luz, e produzir na saída feixes com padrão de intensidade gaussiana. Sua construção em muito se assemelha ao telescópio Kepleriano apresentado na Figura 2.11, com a adição de uma abertura de diâmetro pequeno no foco entre as duas lentes. Seu funcionamento consiste na eliminação dos feixes de luz que não estão colimados na entrada do filtro. A razão para alguns feixes não estarem colimados são diversas, mas três principais podem ser pontuadas. Primeiramente o feixe em si pode não está colimado, ou seja, seus raios não propagam paralelamente entre si. Isto pode ocorrer quando as lentes anteriores ao filtro estão mal posicionadas, ou quando a fonte de luz está próxima. Nesta situação, como prevista pela Equação 2.10, quando a distância até a fonte de luz ( do) não é suficientemente grande, o foco da imagem ocorre após a distância focal da lente. Contudo, na distância focal da primeira lente há uma pequena abertura metálica, conhecida como pinhole . Está abertura bloqueia todos os feixes focalizados após o foco da lente, eliminando a parcela da luz vinda da fonte que não está colimada. Em segundo lugar, a presença de partículas suspensas no ar, e até mesmo as moléculas que compõem o ar, todas elas provocam dispersão da luz. Este efeito é conhecido como dispersão de Rayleigh, e ocorre na presença de partículas muito menores que o comprimento de onda da luz dispersada. A consequência deste efeito é um feixe ruidoso, com pontos escuros que variam de posição e intensidade ao longo do tempo, em decorrência da movimentação das partículas. Cada raio de luz dispersa sai com um ângulo de dispersão θ, e assim como no caso anterior, este raio com ângulo focaliza em uma região fora do ponto focal da lente, sendo bloqueada pela abertura. O funcionamento do filtro espacial também pode ser entendido através da óptica de Fou-rier. Uma lente convexa, converge raios paralelos em um único ponto no plano focal. Cada conjunto de feixes paralelos convergem para um ponto, cuja posição no plano focal depende exclusivamente do ângulo de incidência na lente, em relação ao eixo central da lente, como ilustra a Figura 2.4. Dessa forma a lente mapeia cada conjunto de feixes paralelos em uma posição no plano focal, onde todos os feixes que compartilham a mesma informação são descritos pelo mesmo ponto no plano focal. Esta operação implementa de forma física a transformada de Fourier da imagem coletada pela lente, onde padrões constantes são direcio-nados para as regiões centrais do plano focal, e detalhes como bordas e ruídos são projetados longe do centro. Da mesma forma que a primeira lente consegue realizar a transformação de 16 

CAPÍTULO 2. REVISÃO TEÓRICA 

Figura 2.5: Etapas do filtro espacial: (a) imagem original, (b) transformada de Fourier, (c) filtro passa baixa no domínio da frequência, e (d) imagem resultante. Fourier, a segunda lente a partir da informação presente no plano focal consegue reconstruir a imagem original, implementando a transformação inversa. O padrão de distribuição da intensidade da luz na imagem próxima à primeira lente pode ser representada pela função espacial U (x, y ). No plano focal da primeira lente as com-ponentes de frequência espacial são separadas espacialmente formando a transformada de Fourier F{ U (x, y )}. Para representar este efeito, a Figura 2.5 apresenta as etapas do filtro espacial. Na primeira imagem, está representada a função U (x, y ) de uma fonte de luz no formato de uma linha fina vertical. No plano focal, após à primeira lente é obtida a trans-formada de Fourier demostrada no gráfico da Figura 2.5-b. Para eliminar as componentes de alta frequência uma abertura é posta no plano focal, de forma que apenas uma pequena área circular atravesse. Por fim, a segunda lente realizada a transformada inversa de Fourier utilizando a informação propagada pelo plano focal. O resultado é uma função sinc em duas dimensões. Conforme o diâmetro da abertura diminui, menos oval o feixe se torna, e seu perfil passa a aproximar a uma distribuição gaussiana. Contudo, o diâmetro da abertura deve ser ponderada, pois quando menor a abertura menor a intensidade do feixe passante. Assim como demostrado na Figura 2.5 a depender da fonte de luz utilizada padrões de iluminação podem surgir, principalmente em lâmpadas que fazem o uso de filamentos, onde o filamento gera uma região mais brilhante. O feixe gerado por esta lâmpada pode apresentar distorções em seu formato, tornando o processo de focalização do feixe mais trabalhoso. Este é o terceiro caso onde o filtro espacial pode ser utilizado, onde como foi demostrado, através do filtro espacial é possível aproximar o feixe a um feixe gaussiano, com distribuição uniforme da intensidade da luz. 2.3. PLASMÔNICA 17 Vale ponderar que o filtro espacial pode amplificar as consequências da aberração cromá-tica. Como já demostrado, a distância focal em uma lente é diferente para cada comprimento de onda, e este deslocamento no plano focal pode fazer com que a abertura bloqueie a pas-sagem de alguns comprimentos de onda, realizando uma filtragem na frequência da luz. 

## 2.2.3 Grade de difração 

Uma grade de difração é um dispositivo óptico composto por linhas ou sulcos periódicos. Essas linhas provocam a difração da luz incidente devido a interferências construtivas e des-trutivas, dividindo a luz em suas componentes espectrais. Cada linha da grade pode ser tra-balhada como uma fenda estreita, cada uma agindo como uma fonte secundária de ondas. A difração causada por estas fendas provoca padrões de máxima, quando há interferência cons-trutiva, e padrões de mínima quando há interferência destrutiva. Todas essas interferências dependem tanto do comprimento de onda ( λ) incidido quando da distância entre as linhas da grade ( d). Essa interferência é máxima quando o caminho percorrido por raios difratados de linhas adjacentes são multiplos do comprimento de onda ( λ), o que é representado pela expressão: 

sin( θm) = mλ d (2.12) onde, d é a distância entre as linhas, m um número inteiro e θm o ângulo onde a intensidade medida é máxima para o comprimento de onda λ.A Equação 2.12 indica que o ângulo de intensidade máxima depende do comprimento de onda. Como consequência, a grade de difração possui a capacidade de dispersar a luz assim como os prismas. 

# 2.3 Plasmônica 

A Plasmônica é uma área que estuda os plásmons e seus efeitos em alguns materiais. Plás-mons são oscilações coletivas de elétrons em um material sólido, como metais ou semicon-dutores. Essa oscilação conjunta possui propriedades que se assemelham a de uma partícula, embora não sejam, sendo portanto classificados como quasipartículas. Apesar disso, nada mais são que um plasma oscilante, e ao quantum dessa densidade de carga oscilante é dada o nome de plásmon. Estas oscilações podem estar confinadas em superfícies, na interface entre metal e dielétrico, como o ar. Nesta superfície quando há forte interação com a luz, as ondas eletromagnéticas incidente acoplam com as oscilações de elétrons fazendo surgir os polaritons. Os polaritons também são quasipartículas, que combinam as propriedades da luz e da matéria, permitindo modos únicos de propagação e confinamento óptico. Contudo, estes plásmons não podem ser diretamente exitados por um feixe de luz in-cidido diretamente sobre a superfície. Além disso, para a existência de plásmons em uma superfície é necessária algumas características específicas. A permissividade dos metais para uma frequência óptica pode ser descrita pelo modelo de Drude para uma nuvem de elétrons livres: 

ε(ω) = ε∞ − ω2

> p

ω(ω + iγ ), (2.13) 18 

CAPÍTULO 2. REVISÃO TEÓRICA 

onde ωp é a frequência do plasma, γ o fator de amortecimento, e ε∞ a contribuição de elétrons ligados em altas frequências. Para a plasmônica é necessário que o material tenha: • Parte real negativa para ε(ω): indicando que o material suporta ressonância de plás-mons de superfície (SPR). Isso ocorre porque o campo eletromagnético acopla com a oscilação dos elétrons na superfície, permitindo o confinamento dos campos eletro-magnéticos. • Parte imaginaria pequena para ε(ω): o que indica baixa perda de energia. Dessa forma as ressonâncias plasmônicas não são amortecidas, gerando ressonâncias mais pronun-cias. Na interface plana entre um metal com permissividade εmetal (ω) e um dielétrico com permissividade εdiel (ω) a relação de disperção é dada por: 

kSPP (ω) = k0

√

εmetal (ω)εdiel 

εmetal (ω) + εdiel 

,

onde k0 = ω/c é o vetor de onda no espaço livre, e εmetal (ω) é a permissividade do metal que pode ser calculada pela Equação 2.13. Quando |εmetal (ω)|  εdiel , o vetor de onda kSPP 

excede o vetor de onda da luz no dielétrico, k0

√εdiel . Este desajuste de momento no plano impede que um feixe de luz incidente excite diretamente os SPPs em uma interface plana, pois o momento paralelo da luz k‖ = k0

√εdiel é insuficiente para satisfazer a relação de dispersão dos SPPs. Para superar essa limitação, métodos de acoplamento são utilizados, como: • Prismas (configurações de Kretschmann ou Otto): Adicionam momento extra via reflexão interna. • Grades de difração: Introduzem componentes adicionais de momento ao longo do plano. • Rugosidades ou nanopartículas: Quebras de simetria locais fornecem o momento necessário. 

## 2.3.1 Acoplamento por grade de difração 

Uma grade de difração introduz uma modulação periódica, seja na superfície metálica em si ou em uma camada dielétrica adjacente, de período d. Para uma grade unidimensional (1D), a magnitude do vetor de rede recíproca é: 

G = 2πd

Quando um feixe de luz atinge a interface em um ângulo θ, o acoplamento ocorre quando o momento paralelo do feixe incidente na interface metálica-dielétrica ( k‖), somado ou sub-traído por múltiplos inteiros de G, iguala o vetor de onda dos SPPs kSPP . Essa condição é expressa como: 

kSPP = k‖ + mG = k0

√εdiel sin( θ) + mG =, (m ∈ Z).2.3. PLASMÔNICA 19 Nos ângulos θres específicos em que essa igualdade é verdadeira, o momento no plano corresponde exatamente a kSPP , permitindo a excitação direta dos SPP. 

## 2.3.2 Nanopartículas e Ressonância Localizada de Plásmons de Super-fície (LSPR) 

Em contraste com os SPPs em interfaces metal-dielétrico extensas, as Ressonâncias de Plás-mon de Superfície Localizado (LSPRs) ocorrem em partículas metálicas ou nanoestruturas de dimensão subcomprimento de onda. Em certas frequências, os elétrons de condução dentro dessas nanoestruturas oscilam coletivamente, produzindo uma resposta ressonante conhecida como plásmon de superfície localizado. Como a estrutura é muito menor que o comprimento de onda da luz incidente, os campos ao redor da partícula apresentam amplifi-cação localizada, também chamados de hot spots .Se uma pequena esfera metálica (ou outra forma) for iluminada por um campo eletro-magnético externo, os elétrons livres são induzidos a oscilar em relação ao retículo carregado positivamente. Em uma frequência específica ωLSPR , a força restauradora da nuvem eletrô-nica se iguala à força impulsionadora do campo elétrico, resultando em uma ressonância forte. Isso leva a campos significativamente amplificados na superfície do metal. Para uma nanopartícula metálica cujas dimensões são muito menores que o comprimento de onda incidente, a aproximação quasiestática considera o campo elétrico como uniforme em todo o volume da partícula. No caso mais simples de uma nanopartícula esférica com raio 

a  λ0 em um ambiente homogêneo com permissividade εenv , encontramos uma ressonância quando: Re [ εmetal (ωLSPR )] ≈ − α ε env , (2.14) onde α depende do formato da partícula (para uma esfera perfeita, α = 2 ). Se εmetal (ω)

for suficientemente negativo, os elétrons de condução respondem fortemente ao campo ex-terno em ωLSPR , produzindo uma oscilação de carga localizada. Para partículas não esféricas ou mais complexas, a frequência LSPR pode se dividir ou deslocar com base na razão de aspecto, nitidez das extremidades e outros fatores geomé-tricos. Bastões, elipsoides e nanoestruturas não convencionais podem suportar múltiplas ressonâncias (por exemplo, modos longitudinais e transversais). Mesmo pequenas variações no tamanho ou formato podem causar deslocamentos perceptíveis em ωLSPR .

## 2.3.3 Substrato de Nanopirâmides 

O dispositivo utilizado neste trabalho é constituído por nanopirâmides de ouro distribuídas periodicamente ao longo de uma superfície de ouro. Essa superfície em virtude da periodici-dade possui propriedades de uma grade de difração, e em virtude das nanoestruturas também apresentam propriedades de um nanopartícula LSPR. Pela periodicidade da estrutura há a excitação de modos SPP, conforme será mostrado nos resultados. Por outro lado, em virtude das nanoestruturas piramidais também há a excitação de uma ressonância estável, sendo fortemente dependente das mudanças na permissividade do meio externo εenv . Esta sensibi-lidade ao meio externo é o funcionamento por trás da detecção de moléculas e proteínas no entorno do dispositivo. Como o dispositivo está envolto por ar (cuja permissividade é pró-xima ao do vácuo), a presença de qualquer corpo externo aumenta a permissividade do meio 20 

CAPÍTULO 2. REVISÃO TEÓRICA 

externo, e para que a igualdade na Equação 2.14 seja mantida a frequência de ressonância deve diminuir, segundo a Equação 2.13. Dessa forma, o valor de ressonância passar por um 

redshift , o que é observado como um deslocamento do pico de ressonância em direção ao infravermelho. Capítulo 3 Etapas Preliminares 

# 3.1 Modelagem do nanodispositivo 

Esta seção abordara o processo de desenvolvimento do sensor LSPR utilizado neste traba-lho. O texto aborda o método empregado para a simulação do dispositivo, o processo de otimização das dimensões das pirâmides e o procedimento empregado para a fabricação. Os resultados são fruto de trabalhos posteriores desenvolvidos na UFMG [8] e estão descritos neste capítulo como uma revisão das metodologias empregadas, as quais foram retomadas para justificar os resultados encontrados. O dispositivo utilizado é constituído por nanopirâmides, tendo sido desenvolvido e oti-mizado para medidas SERS. Seu objetivo inicial era amplificar o sinal recebido pelo laser de emissão e direcionar o campo eletromagnético para a amostra em análise. O funcionamento do SERS necessita que a amostra interaja com o campo eletromagnético de excitação, con-tudo as taxas de interação normalmente não são altas. Como resultado, o sinal gerado pelo efeito Raman é baixo. Neste sentido, as nanopirâmides agem como antenas que concentram o campo eletromagnético e transporta para sua ponta, onde a intensidade é máxima. Com este campo eletromagnético mais intenso, a interações com as moléculas ocorrem com mais frequência, produzindo uma amplificação no sinal produzido. Estudos posteriores realizados nestes mesmos dispositivos, observaram a presença de modos de energia LSPR. Devido à geometria utilizada, modos de ressonâncias surgem em decorrência da presença de campo elétrico. Está propriedade se mostrou útil para o uso do dispositivo em outros métodos de medições além do SERS. Neste sentido, o presente trabalho utilizou do dispositivo já desenvolvido e fabricado para realizar medidas biológicas em uma montagem mais simples que a necessária para medidas SERS. 

## 3.1.1 Simulações 

As simulações foram feitas para uma matriz regularmente espaçada de pirâmides. Foi utili-zado o Método dos Elementos Finitos 3D (3D-FEM) no software COMSOL Multiphysics . O domínio computacional foi simplificado usando a simetria geométrica, de modo que apenas uma célula unitária da matriz precisasse ser simulada. Sendo essa célula unitária uma pirâ-mide quadrada de ouro no centro, com todas as arestas de mesmo comprimento (L), sob um substrato de ouro, e com ar cobrindo o topo da pirâmide e o substrato exposto. Como variá-veis dessa simulação, além do comprimento das arestas da pirâmide (L) também era possível 21 22 

CAPÍTULO 3. ETAPAS PRELIMINARES 

Figura 3.1: Dispositivo de nanopirâmides: (a) Ilustração do dispositivo demostrando as di-mensões, onde a representa a altura, b é a base e c é a borda das pirâmides. (b) Intensidade de campo elétrico normalizada a 633 nm calculada com base nas variações nas dimensões da pirâmide para determinar a combinação mais apropriada de parâmetros que podem ajudar a atingir a maior intensidade de campo. (c) Imagem obtida no Centro de Microscopia da UFMG do dispositivo fabricado. alterar o espaçamento entre pirâmides (D) que corresponde a distância entre as arestas de pirâmides adjacentes. Estes parâmetros foram utilizados para otimizar o dispositivo [8]. As condições de contorno utilizadas foram: Condutor Elétrico Perfeito (PEC) sob o substrato de ouro, Condições de Contorno Periódicas (PBC) nos quatro lados laterais da célula unitária, e uma porta de entrada no lado superior da célula, onde ocorre a excitação por onda plana. A Figura 3.1-a demostra visualmente o modelo utilizado nas simulações. As simulações foram inicialmente utilizadas para a criação e otimização dos dispositivos. Mas neste trabalho, as mesmas forma retomadas para a investigação dos resultados obtidos, sendo usadas para confirmar e entender os efeitos observados. 

## 3.1.2 Otimização do dispositivo 

A otimização do dispositivo se deu pela variação do tamanho das bases das pirâmides e o espaçamento entre elas. A métrica utilizada foi a intensidade do campo elétrico na superfície do dispositivo. Através destas variações e com uma onda planta de excitação a 633 nm o gráfico presente na Figura 3.1-b foi gerado. Este gráfico apresenta o valor máximo da intensidade do campo elétrico obtido no dispositivo neste comprimento de onda para cada dispositivo simulado. É possível observar na Figura 3.1-b uma região mais escura, onde a intensidade do campo elétrico é maior. Esta região é chada de iso-pitch , e ela representa uma combinação de parâmetros (L) e (D) em que o dispositivo apresentara o melhor desempenho enquanto possui uma grande margem de erro. Mantendo uma mesma periodicidade entre as pirâmides, o aumento da base das pirâmides (L) causa uma diminuição no espaçamento entre as base (D). As variações podem aparecer em virtude de erro de fabricação, mas esta variação mantém o dispositivo na linha do iso-pitch , apenas a percorrendo. Como a linha de iso-pitch mostrada na Figura 3.1-b é longa, isto garante uma maior margem de variação e erro na fabricação. 3.1. MODELAGEM DO NANODISPOSITIVO 23 

Figura 3.2: Etapas do processo de fabricação do dispositivo de nanopirâmides. 

## 3.1.3 Fabricação 

Seguindo a região de iso-pitch o dispositivo NP-A1 foi fabricado, com base 330 nm e espaça-mento de 290 nm, resultando em uma periodicidade de 620 nm. Para comparar os resultados, outro dispositivo foi fabricado em uma região não tão otimizada, o dispositivo NP-A2, com 420 nm de base e 40 nm de espaçamento. A Figura 3.1-c mostra o dispositivo NP-A1 após a fabricação. O processo de fabricação da matriz de nanopartículas piramidais consiste em várias eta-pas bem definidas, conforme ilustradas na Figura 3.2. Inicialmente uma lâmina de silício com orientação cristalográfica (100) é revestida com uma camada uniforme de 40 nm de cromo (Cr) usando a técnica de evaporação térmica. Para gerar uma máscara contendo uma matriz de janelas circulares com diâmetro de 150 nm, o substrato é revestido com uma ca-mada de resina PMMA (poli(metil metacrilato)) por meio de um processo de spin-coating. Essa máscara é fabricada utilizando o sistema de litografia por feixe de elétrons Raith e-LiNe Plus de 30 kV, que estrategicamente mantém a camada de Cr exposta após o desenvolvi-mento. Uma etapa de ataque químico direcionada ao Cr é realizada para revelar o substrato de silício sob a máscara litográfica circular, sendo então imersa em uma solução de hidróxido de potássio (KOH). Essa imersão cria uma estrutura distinta em forma de matriz piramidal na superfície do substrato. Devido à orientação escolhida da lâmina e às características anisotrópicas do processo de ataque químico, a estrutura resultante é uma matriz de cavidades piramidais sob cada janela circular. A máscara de cromo pode ser removida, e o resultado corresponde a um molde de silício para a matriz de nanopartículas piramidais. Em seguida, uma camada de ouro de 175 nm de espessura é evaporada termicamente para preencher cada cavidade e cobrir o substrato de silício. Finalmente, um substrato de vidro é colado ao ouro. Como ouro e silício não aderem bem, a camada de ouro conformada ao molde pode ser extraída. O molde de 24 

CAPÍTULO 3. ETAPAS PRELIMINARES 

Figura 3.3: Nomes definidos para cada uma das matrizes. Como pode ser observado ao todo são 22 matrizes de nanopiramides. silício permanece intacto nessa etapa, permitindo sua reutilização em futuros processos de evaporação. A estrutura final corresponde a uma matriz de nanopartículas piramidais sobre um substrato de ouro em um substrato de vidro, como mostrado na Figura 3.1-c. Na litografia é realizado o teste de dose, onde são testados diferentes valores de tempo e potência para o feixe de revelação. Com isso, em uma mesma fabricação combinações diferentes são testadas para lidar com variáveis não controladas, como qualidade do fotore-sist , temperatura do ambiente, rugosidades, todas que podem de alguma maneira afetar no processo de litografia. Como resultado, o dispositivo fabricado é um conjunto de diferentes matrizes de nanopirâmides. Para evitar confusão o seguinte sistema de nomes foi utilizado: cada matriz é chamada por x-y, onde x é a linha e y a coluna que a matriz se encontra. A Figura 3.3 demostra os nomes utilizados para o dispositivo NP-A1 utilizado. 

# 3.2 Plataforma de Biossensoriamento 

Esta seção trata da integração do sensor LSPR com a montagem óptica desenvolvida para as medidas de biosensoriamento. Na primeira parte é descrita a montagem óptica para me-dições de absorbância, contendo 4 graus de liberdade: translação em x e z e rotação em z e azimutal. A segunda parte trata do processo de caracterização do sensor LSPR com o foco de encontrar o pico de ressonância mais adequado para as medidas, e as melhores configurações de ângulo. Em seguida é descrito o método utilizado para realizar as medidas biológicas e os cuidados tomados. Por fim, é apresentado os cálculos que compõem o software de tra-tamento dos dados, e como os resultados gerados são utilizados para detectar a presença da proteína Pb27r. 

## 3.2.1 Montagem óptica 

Nesta plataforma de sensoriamento o resultado é expresso como o deslocamento do pico de absorção entre duas medidas, uma antes e outra após a deposição da amostra. Sendo assim, para a realização destas medidas é necessário antes construir uma montagem óptica 3.2. PLATAFORMA DE BIOSSENSORIAMENTO 25 para medidas de absorção. Para cada medida de absorção é necessário duas curvas de in-tensidade, sendo a primeira a intensidade da fonte de luz ( Ilamp ) e a segunda a intensidade refletida ou transmitida pela amostra ( Iamostra ). Neste caso, a absorbância é calculada por: 

A = −log (Iamostra /I lamp ), ou A = −10 log (Iamostra /I lamp ) quando expressa em dB (deci-bel). Contudo, o objetivo é medir a absorção advinda apenas dos efeitos e ressonâncias nas nanoestruturas de ouro, mas isto não é possível de ser medido diretamente, pois as nanoes-truturas estão sob uma lâmina de ouro. Portanto, seriam necessárias duas medidas, uma com a luz refletida pelo dispositivo e ouro por uma lâmina simples de ouro com igual espessura, todas em relação a mesma fonte de luz. Como a absorbância medida pela reflexão do dispo-sitivo é a soma dos efeitos da lâmina de ouro e das nanoestruturas, a seguinte expressão pode ser montada: 

Atotal = Aouro + Anano ,

onde Aouro é a contribuição da lâmina de ouro na absorção, Anano é a contribuição das nanoestruturas para a absorção e Atotal a absorção observada entre a intensidade emitida pela lâmpada e a refletida pelo dispositivo. No entanto, esta expressão pode ser reorganizada e simplificada utilizando as propriedades dos logaritmos: 

Anano = Atotal − Aouro 

= − log 

( Idisp 

Ilamp 

)

−

(

− log 

( Iouro 

Ilamp 

)) 

= − log 

( Idisp 

> Ilamp

)( Iouro 

> Ilamp

)

= − log 

( Idisp 

Iouro 

)

, (3.1) onde Idisp é a intensidade refletida pelo dispositivo, Iouro a intensidade refletida pela lâ-mina de ouro e Ilamp a intensidade refletida pela lâmpada. Pela Equação 3.1 a absorção dos nanodispositivos pode ser calculada utilizando apenas duas medidas, dispensando a neces-sidade de medir a lâmpada diretamente. Isolar os efeitos dos nanodispositivos é vantajoso porque torna o resultado independente dos efeitos da lâmina de ouro, como a absorção ine-rente do material e o ângulo de excitação do campo eletromagnético na lâmina. Isto também é vantajoso porque simplificar a montagem, não sendo necessário realizar desvios da luz da fonte para medição no espectrômetro. Além disso, toda fabricação do dispositivo pos-sui uma margem ao redor dos nanodispositivos a qual a superfície é grande e afastada o suficiente para ser utilizada como a lâmina de ouro de referência. Para medidas biológicas é comum a utilização da faixa do espectro visível e infraverme-lho próximo, e a lâmpada que melhor atende esta faixa são as lâmpadas halógenas. Este tipo de lâmpada possui distribuição uniforme no espectro de emissão, e se aproxima ao espectro de um corpo negro. Além disso, apresenta espectro de emissão cuja maior parte da energia de emissão está na faixa de interesse. A lâmpada utilizada é uma tubular halógena de 500W alimentada com tensão de 220V. A lâmpada tubular emite luz para todas as direções em um formato cilíndrico ao redor de seu eixo. Contudo, para a realização das medidas é necessário um feixe colimado com 26 

CAPÍTULO 3. ETAPAS PRELIMINARES 

diâmetro próximo ao do dispositivo. Um feixe colimado é um feixe de luz cujo diâmetro é constante durante toda a propagação. Devido a efeitos de difração não é possível manter o diâmetro constante, mas para curtas distâncias, como é o caso desta plataforma, pode se considerar constante. Mas antes, para melhora a qualidade das medidas, uma caixa foi cons-truída para cobrir a lampada e evitar vazamentos de luz para o ambiente. A luz no ambiente atrapalha as medidas adicionando ruídos e sinais de background . Além da caixa, todas as medidas foram realizadas em uma salada escura, própria para medidas ópticas, onde a luz de ambiente já é devidamente controlada. Estas precauções auxiliam na qualidade das me-didas ao aumentar a sensibilidade e diminuir o tempo de captura do sinal. A caixa também foi recoberta internamente com folhas de alumínio para refletir a luz não utilizada pela lam-pada, diminuir a quantidade absorvida pela caixa, reduzindo o aquecimento da mesma. Em uma das paredes da caixa há um furo de 1 polegada (2,54 cm) onde um tubo de 20 cm de comprimento está inserido. Este tubo permite que uma pequena quantidade da luz emitida pela lampada saía pela caixa. A relação entre o diâmetro e o comprimento do tubo tam-bém contribue para reduzir o ângulo de abertura da luz. Como o diâmetro é de 2,54 cm e o comprimento é de 20 cm, o ângulo máximo de saída da luz seria: arctan(2 , 54 /20) ≈ 7.2◦.Por fim, para colimar o feixe de luz que sai do tubo, um filtro óptico espacial foi cons-truído. Este filtro possui duas funções, a primeira é eliminar a parte da luz vinda da lâmpada que não está colimada, ou seja, está em ângulo com o sentido de propagação do feixe, e o segundo é retirar a influência do formato da lâmpada na imagem gerada pelo feixe. Sem o filtro espacial no foco a imagem projetada é uma linha vertical, pois a lâmpada é tubular e está posicionada na vertical. O filtro espacial é composto de duas lente e uma abertura metálica que fica entre as lentes. Quando um feixe de luz atravessa uma lente, cada ponto da entrada atua como uma fonte de ondas esféricas, que ao passarem pela lente são direciona-das de forma que interferem construtivamente no plano focal. A lente realiza uma integração angular dessas ondas, mapeando as frequências espaciais da luz para diferentes posições no plano focal. Assim, detalhes finos da luz aparecem afastados do centro, enquanto padrões amplos aparecem próximos ao centro. Esse processo transforma a distribuição espacial da luz em uma representação de suas componentes de frequência, realizando uma transformada de Fourier óptica. Esta transformada é realizada pela primeira lente. Para limpar a imagem projetada no feixe colimado, deseja-se que haja predominância de baixas frequências espa-ciais na imagem projetada, ou seja, que a luz seja distribuída de maneira suave e uniforme, o que corresponde a um feixe com perfil gaussiano. Para isto é utilizada uma abertura metálica (pinhole ) de 100 micrômetros posta no plano focal da primeira lente, onde há a transfor-mada de Fourier. Neste plano a luz próxima ao centro corresponde as componentes de baixa frequência e apenas estas que a abertura permite a passagem, efetivamente agindo como um filtro passa-baixa espacial. Quando menor a abertura mais limpa a imagem projetada pelo feixe, contudo menor a intensidade da luz, por isto deve ser escolhida a abertura mais ade-quada para cada situação. Após a filtragem, pelo efeito da difração, a abertura metálica age como uma fonte pontual de luz, portanto é necessária uma segunda lente para direcionar e colimar o feixe de luz. A segunda lente é fixada respeitando sua distância focal, e a relação entre a distância focal da primeira e a segunda lente influência diretamente do diâmetro do feixe colimado da saída. A relação de redução é dada por: M = f1/f 2, onde f1 e f2 são as distâncias focais da primeira e segunda lente respectivamente, e M a magnificação, que neste caso deve ser menor que 1. Nesta montagem foram utilizadas como lentes duas lentes objetivas, a primeira com abertura de 0,40 mm e amplificação de 20x e a segunda de 0,20 3.2. PLATAFORMA DE BIOSSENSORIAMENTO 27 

Figura 3.4: Montagem óptica para medidas de reflexão e absorção. mm e amplificação de 8x. As lentes são ajustadas pelas suas distâncias focais, e o substrato de medição é posto no foco da segunda lente (onde o feixe colimado possui menor diâmetro). O substrato é fixado em um conjunto de estágios de translação e rotação, os quais permitem a movimentação em x e z do dispositivo e a rotação em z e azimutal (rotação normal a superfície). Os movimentos de translação permitem a centralização do dispositivo na região de interesse, como na melhor matriz de nanoestruturas, ou até na borda para medidas da lâmina de ouro necessária para o cálculo de absorbância. Já os movimentos de rotação permitem posicionar o substrato no modo em que as ressonâncias são melhor exitadas. O feixe de luz incidido sob o substrato de ouro reflete em ângulo para uma lente plano-convexo que focaliza o feixe refletido para a entrada de uma fibra óptica. Esta fibra transmite o feixe refletido para a entrada de um espectrômetro CCD que faz a leitura do sinal de intensidade para cada comprimento de onda. O modelo do espectrômetro utilizado é o Thorlabs CCS200/M, que realiza medidas de intensidade na faixa de 200 a 1000 nm. A Figura 3.4 apresenta um esquemático da montagem óptica construída. 

## 3.2.2 Procedimentos para caracterização do dispositivo 

O processo de caracterização do dispositivo tem como finalidade investigar as posições do dispositivo onde a ressonância é mais pronunciada, bem como definir os valores iniciais, os quais são utilizados para calcular o deslocamento do pico de ressonância. Visando investigar todas as possibilidades do dispositivo, duas medidas de varredura são realizadas, um para o ângulo de incidência da luz na amostra e outro para o ângulo azimutal da amostra. No caso do ângulo azimutal este é realizado no ângulo de incidência que apresentou o melhor resultado, pois esta ultima medida é apenas um ajuste fino na performasse das medições. Em cada um das medidas inicialmente são configurados os ângulos de incidência e azimutal, em seguida com os micrômetros dos estágios de movimentação x e z o dispositivo é centralizado na região de interesse. Caso a montagem não esteja corretamente centralizada, os movimen-tos de rotação sempre iram deslocar o ponto onde o feixe de luz atinge o dispositivo, por isso sempre é necessário centralizar o dispositivo com os estágios de translação. Além disso, quando o ângulo de incidência é alterado o ângulo de reflexão também é, por isso a fibra óp-tica do espectrômetro e a lente que captura a luz refletida devem ser movimentados também, 28 

CAPÍTULO 3. ETAPAS PRELIMINARES 

mantendo sempre a mesma distância entre a lente e o dispositivo. Ainda, no caso do dispo-sitivo utilizado, uma mesma lâmina comporta diferentes tipos de nanodispositivos, cada um deste agrupado em uma matriz isolada. Neste caso, idealmente a varredura deveria ser feita para cada uma das matrizes, mas isto levaria muito tempo, sendo assim algumas medidas simples são realizadas em ângulos entre 30 e 40 graus. A partir das curvas de absorção de cada uma das matrizes, os que apresentam melhores resultados e picos mais prominentes são escolhidos para o estudo por varredura dos ângulos. A caracterização do dispositivo é realizada na montagem óptica construída com o subs-trato limpo. Para a limpeza do substrato é utilizada água deionizada, álcool isopropanol, e acetona pura. Todas substancias são aplicadas com o auxílio de uma garrafa de lavagem, sendo primeiro aplicada a acetona para limpeza de matéria orgânica, em seguida o álcool para diluição e retirada da acetona e por fim a água deionizada para a retirada do álcool. A lamina é seca com jato de nitrogênio para retirada de umidade e evaporação do álcool rema-nescente. Esta limpeza é realizada com menos frequência, sendo utilizada apenas antes da caracterização do dispositivo e após varias medidas biológicas, quando o pico de ressonância não retorna ao seu valor original. Com o dispositivo limpo e já posicionado no ângulo e matriz de interesse as medições pode ser realizadas. O processo de medição consiste em posicionar o feixe de luz na lâmina de ouro ao redor do dispositivo, neste local a curva de intensidade é capturada e armaze-nada. Em seguida, o feixe é posicionado no dispositivo ou matriz de interesse, e em seguida outra curva de intensidade é capturada e armazenada. Estas duas curvas capturadas são en-viadas para o software de processamento de dados onde a curva de absorbância pode ser representada graficamente. Cada medida de intensidade necessita que o parâmetro tempo de integração seja configurado. Este informa ao espectrômetro por quanto tempo o sensor es-tará exposto à luz, capturando energia para os sensores. Quanto maior o tempo de integração maior a intensidade medida, contudo mais ruído também, pois a medida estará exposta por mais tempo a possíveis ruídos. Além disso, se o tempo for grande demais os sensores do espectrômetro podem ser danificados, mas antes disso é possível observar as medidas serem saturadas. O espectrômetro utilizada faz medidas de intensidade e expressa em valores de 0 a 1, sendo 1 o valor máximo. Em cada medição deve ser escolhido atentamente o tempo de integração para obter dados com a maior intensidade possível, mantendo uma margem de segurança para não haver saturação. O valor escolhido depende de muitas variáveis, mas na montagem construída esse período é normalmente de 7 segundos por medida. Vale informar que, para o cálculo de absorbância, a curva de referência e a curva analisada ambas deve estar no mesmo tempo de integração para que as diferenças de intensidade seja apenas em virtude da presença das nanoestruturas. Para melhorar a qualidade dos resultados há algumas recomendações: a primeira é sobre a luz de fundo ( background ), esse ruído é sempre estático em um ambiente controlado como a sala escura utilizada. Portanto, antes de realizar a primeira medida, é capturada uma curva de intensidade, bloqueando o feixe de luz com algum obstaculo preto logo após a saída do filtro espacial. Fazendo isso, o sinal medido será da intensidade da luz gerada por fontes não desejadas. Esta curva passa a ser o zero de qualquer medida, portanto a final cada medida deve ser subtraída por essa curva de background . O software do espectrômetro utilizado possui essa função automatizada, sendo assim, quando habilitada toda nova medida já é subtraída pelo valor de background . O segundo tipo de ruído é dinâmico e não é eliminado com a retirada de background , mas este ruído possui distribuição gaussiana e média zero. 3.2. PLATAFORMA DE BIOSSENSORIAMENTO 29 Para reduzir esse tipo de ruído é inicialmente utilizada a média de várias medidas. Devido ao tempo de cada medida, para cada curva de intensidade apenas 5 ou 10 são capturadas, sendo que o resultado é a média entre elas. O software de processamento dos dados também utilizada filtros para remover este tipo de ruído, os quais comparam valores vizinhos para definir o valor de intensidade em cada comprimento de onda. 

## 3.2.3 Procedimentos para medições biológicas 

Para este projeto foi fornecida uma amostra da proteína Pb27r diluída em água a uma con-centração de 0,5 mg/mL. Outras concentrações são necessárias para ser possível realizar a calibração do sensor e traçar a curva de sensibilidade. Portanto, a amostra inicial de Pb27r foi diluída em outras concentrações menores: 15,62, 7,81, 3,90, e 1,95 μg/mL, sendo que todas as diluições foram realizadas com água deionizada. Quando não utilizados, a amostra original e suas diluições foram armazenadas em tubos Eppendorf de 1,5 mL em geladeira resfriada a 4◦C. Para cada medida biológica, no substrato limpo é aplicada uma gota de 0,5 

μL. A gota é deixada para secar pelo período de 10 minutos. A aplicação da gota e a medida é realizada em um ambiente resfriado a 16 ◦C por ar-condicionado. Como o ar-condicionado atua retirando a umidade do ambiente, isto contribui para a evaporação da água. Após a secagem da gota sob o substrato, o dispositivo é colocado e fixado na plataforma de medição. O processo de medida com a amostra biológica se dá mesma forma que no processo de caraterização, contudo, neste não há a necessidade de realizar a varredura em todos os ângulos, pois os melhores ângulos já podem ser escolhidos. Duas medidas de inten-sidade devem ser obtidas para o cálculo da absorbância, uma da lâmina de ouro e outra do dispositivo após a aplicação da amostra. Ao final da medida o substrato deve ser limpo com água deionizada para a retirada do material biológico. Realizando esta limpeza o substrato se encontra pronto para uma nova medida biológica. Esta limpeza é menos efetiva que a feita com acetona, mas é normalmente o suficiente para trazer o pico de ressonância para próximo do valor original, permitindo que novas medidas sejam feitas. Como o pico pode apresentar diferenças com seu valor original, é recomendável caracterizar novamente o dis-positivo realizando apenas uma medida de absorção para registrar em que comprimento de onda se encontra o novo pico. Após a realização de várias medidas a limpeza com água deio-nizada não será mais capaz de limpar o dispositivo, sendo então necessário realizar a limpeza com acetona pura. Também é recomendável realizar a limpeza com acetona ao final do dia, pois com o passar dos dias os resquícios das amostras biológicas tornam-se mais difíceis de retirar. 

## 3.2.4 Processamento dos dados 

O processamento dos dados é feito em Python com o auxílio das bibliotecas NumPy, SciPy e Pandas para processamento dos dados e a Matplotlib para representação gráfica. Inicialmente os dados são extraídos do software da Thorlabs - ThorSpectra, o qual faz comunicação com o espectrômetro. Durante as medições os dados são salvos em arquivos com formato spf2 , mas para o processamento de dados estes arquivos são exportados no formato txt , onde os dados ficam dispostos em colunas separadas por ponto e vírgula (;). A biblioteca Pandas é utilizada para fazer a leitura dos arquivos txt e a conversão para o formato de arrays do NumPy. Os dados recebidos possuem um vetor de comprimento de onda e outro vetor com a intensidade 30 

CAPÍTULO 3. ETAPAS PRELIMINARES 

de luz medida para cada comprimento de onda. Inicialmente os dados são cortados, retirando os comprimentos de onda mais altos e mais baixos onde a intensidade de luz é baixa. Nestas regiões os resultados são muito ruidosos, sendo impossível tirar alguma informação. Para a lâmpada utilizada a região útil é de 550 a 950 nm. Seguindo a Equação 3.1 as curvas de absorbância são calculadas para cada dado de in-tensidade nos dispositivos, todos com relação a mesma lâmina de ouro nos mesmos ângulos. Estes dados de absorbância são então filtrados utilizando o filtro SavitzkyGolay, com largura de janela de 10 e polinômio de grau 1. Este filtro possui grande adoção na área de proces-samento de sinais, sendo utilizado para a suavização de dados. Diferente de outros filtros que podem atenuar picos, ele suaviza ruídos enquanto mantém a integridade dos sinais [13]. Após a suavização das curvas, alguns gráficos são gerados pelo script para observação dos dados. Para a medida biológica a informação necessária são as posições dos picos de ressonân-cia. Para extrair melhor este dado, algumas outras modificações são realizadas nas curvas de absorbância. A primeira é a retirada de tendências e desvios nos dados. Para isso, é realizada uma regressão linear de cada curva para extrair os valores médios de inclinação ( a) e desvio (b). Com estes dados uma curva de primeiro grau é gerada e o dado de absorbância é sub-traído por essa curva, retirando a tendência e desvios de cada medida. Essa alteração coloca todas as medidas em um mesmo patamar, de forma que medidas de diferentes ângulos ou dis-positivos possam ser melhor comparadas. Isto também planifica a curva enfatizando melhor os picos. Neste processo informações da absorção são perdidos, mas não há consequência nisto já que o comprimento de onda dos picos de ressonância são mantidos. Após este pro-cessamento o script gera gráficos com a absorbância após o tratamento, e alguns comparando diferentes medidas de absorbância, o que é útil para a escolha dos melhores dispositivos ou ângulos. É gerado também um mapa de calor demostrando como a absorbância é alterada com a mudança de ângulo. Como medidas de ângulo são custosas, geralmente poucos da-dos são gerados, produzindo um mapa de calor muito quadriculado. Para isso o software de processamento de dados realiza algumas filtragem e interpolações para preencher os dados faltantes. Os dados são agrupados em uma matriz de 2 dimensões, e nesta matriz é utilizado um filtro gaussiano. Este filtro é utilizado em imagens para realizar a suavização de deta-lhes, no caso do mapa de calor é esperado que não haja mudanças bruscas entre medidas vizinhas, nesse sentido o filtro gaussiano age homogenizando os dados. Por fim, para não haver variações em degrau na imagem do mapa de calor é realizada a interpolação dos dados linear, formando uma matriz quadrada, ou seja, há a mesma quantidade de dados em x e y (comprimento de onda e ângulo). Capítulo 4 Resultados 

Este capitulo pretende apresentar os resultados obtidos ao longo do projeto. Nele é apre-sentado o dispositivo utilizado e os resultados de sua caracterização, a escolha do melhor dispositivo e dos ângulos para a realização das medidas. Também é apresentado os resul-tados das medições biológicas e o processo de calibração do sensor para correlacionar o deslocamento do pico de ressonância com a concentração da proteína Pb27r. Seguindo os parâmetros do dispositivo NP-A1 uma fabricação foi realizada. A Figura 4.1 apresenta o dispositivo utilizado logo após a extração do molde. É possível observar que a coluna 5 e 6 entre a 2 a e 5 a linha possui nenhuma matriz de nanoestruturas, sendo está a região utilizada para medidas de lâmina de ouro. Além da fabricação do dispositivo NP-A1 também foi fornecido um dispositivo NP-A2 para análise. 

# 4.1 Montagem óptica 

A montagem óptica foi realizada no laboratório OptMa na UFMG, onde foram fornecidos os equipamentos, lentes e estágios para a montagem na sala escura. Todas as lentes foram ajus-tadas respeitando suas distâncias focais. Como explicado no capítulo 3.2.1 o filtro espacial é fundamental para haver um feixe de luz homogêneo e colimado. A Figura 2.5 representa a situação enfrentada nesta montagem e a Figura 4.2 demostra o efeito prático do filtro espacial na imagem projetada pelo feixe. Nos dois casos demostrados pela imagem, as mesmas len-tes objetivas foram utilizadas. No primeiro caso, contudo, foi retirado o pinhole , retirando o 

Figura 4.1: Extração dos dispositivos NP-A1, a esquerda encontra o molde de silício, e a direita a lâmina de ouro após o lift-off .31 32 

CAPÍTULO 4. RESULTADOS 

Figura 4.2: Caparação entre o spot com e sem o filtro espacial: (a) lentes objetivas sem 

pinhole , (b) lentes objetivas na mesma posição com cavidade pinhole entre elas. efeito de filtragem. Pode ser observado que o diâmetro do feixe é maior e é possível enxergar a projeção do filamento vertical da lâmpada por trás do tubo. As lentes foram ajustas até a formação da imagem no aparato branco, como a lâmpada está próxima seu feixe projeta uma imagem, como é previsto pela Equação 2.10. A formação da imagem ocorre após o plano focal da lente, e neste plano a imagem sofre uma redução que não é mínima, em virtude disto o feixe apresenta um diâmetro maior que o presente na Figura 4.2-b. Por outro lado, na segunda imagem o diâmetro do feixe é menor e controlado, e o perfil de distribuição da intensidade da luz se aproxima a distribuição gaussiana. Como explicado, quanto menor a abertura do pinhole melhor a qualidade da filtragem, mas menor a intensi-dade do feixe. O pinhole utilizado é o que apresentou a melhor relação entre intensidade e distribuição de intensidade. Como a intensidade da luz foi priorizada é possível perceber na imagem projeta na Figura 4.2-b que o círculo apresenta uma leve ovulação. Quando as lentes são corretamente reguladas e o substrato é posto no foco do feixe, o spot da Figura 4.3 é obtido. Este é o menor diâmetro conseguido com está montagem, sendo um diâmetro de aproximadamente 1 mm. Valores menores foram obtidos utilizando 

pinholes menores, mas nestes casos a intensidade do feixe de luz não foi suficiente para as medidas. O diâmetro obtido foi suficiente para analisar cada matriz do dispositivo NP-A1 individualmente, sem haver a ativação de outra matriz simultaneamente. O espectro de emissão do feixe foi medido diretamente utilizando o espectrômetro, e o espectro de emissão da Figura 4.4 foi obtido. Esta lâmpada possui espectro com intensidade suficiente para realizar medidas entre 550 e 950 nm, fora desta região foi percebido que as medidas possuíam muito ruído e resultados não eram confiáveis. Por fim, a montagem final é mostrada na Figura 4.5. 4.2. CARACTERIZAÇÃO DO DISPOSITIVO 33 

Figura 4.3: Diâmetro mínimo do feixe de luz. 

# 4.2 Caracterização do dispositivo 

Conforme instruído no capítulo 3.2.2, o primeiro conjunto medidas realizas foram feitas para conhecer o dispositivo e escolher os melhores. Medidas previas em uma das matrizes, mostraram a presença de pico de absorção pronunciados na região entre 30 ◦ e 40 ◦. Portanto, como ponto de partida o suporte de amostras foi fixado no ângulo de 38 ◦ e então medidas de absorbância foram realizadas em todas as matrizes. As Figuras em apêndice A.1 e A.2 mostram os resultados obtidos para cada matriz dos dispositivos NP-A1 e NP-A2 respectivamente. A primeira observação que pode ser feita en-tre as imagens é que no dispositivo NP-A2 não há nenhuma ressonância, há apenas os efeitos da absorção inerentes do ouro e da grade de difração. Como informado, o dispositivo NP-A2 foi produzido com parâmetros que o colocam fora da região mais otimizada, e, como espe-rado, este apresentou qualidade de sinal inferior. Por outro lado, as matrizes do dispositivo NP-A1 apresentou picos de ressonância bem definidos, sendo os mais intensos os três picos encontrados na região entre 600 e 900 nm. Também pode ser observado que mesmo no dis-positivo NP-A1, algumas matrizes não apresentaram bom desempenho, como a matriz 1-1 e 2-2 quando comparado com o dispositivo 3-3, por exemplo. Utilizando estes parâmetros, os melhores dispositivos foram escolhidos e ranqueados para uso na caracterização e medidas biológicas. As matrizes 1-2 e 2-1 foram escolhidas para o estudo do dispositivo. Neste foram reali-zadas medidas variando o ângulo 1◦ por vez, de 15 ◦ a 55 ◦. Abaixo de 15 ◦ não foi possível realizar medidas, pois o feixe refletia em um ângulo pequeno, nesta situação o feixe muitas vezes colida com as estruturas, ou não era possível aproximar as lentes se haver sobrepo-sição. Para ângulos maiores que 55 ◦ o feixe atingia o substrato de rasante, provocando um padrão de iluminação elíptico. No limite desse ângulo a elipse alargava e iluminava duas matrizes do dispositivo ao mesmo tempo. A Figura 4.6 apresenta a curva de absorbância para alguns dos ângulos medidos, onde todas as curvas mostradas foram processadas utilizando o software desenvolvido. É possível 34 

CAPÍTULO 4. RESULTADOS 

Figura 4.4: Espectro de emissão da lâmpada halôgena. 

Figura 4.5: Montagem óptica desenvolvida. (a) Visão lateral da montagem e (b) visão supe-rior. 4.2. CARACTERIZAÇÃO DO DISPOSITIVO 35 

Figura 4.6: Curva de absorbância variando o ângulo de excitação para a matriz 1-2. 36 

CAPÍTULO 4. RESULTADOS 

Figura 4.7: Mapa de calor para as medidas com ângulo das matrizes 1-2 e 2-1. notar a presença de diferentes picos de ressonância e como eles são afetados pelo ângulo de incidência da luz. Também é possível observar que alguns picos apresentam intensidade maior para alguns ângulos, enquanto outros parecem se mover. A existência destes modos de ressonância se dá pela presença das nanoestruturas otimizadas. A geometria única das na-nopirâmides suporta modos de oscilações únicos, que dependem dos materiais e dimensões utilizadas. Nesse sentido, seria possível observar ressonâncias fixas, como o pico observado em 850 nm. Este modo de energia se mantém praticamente estático independente do ângulo de incidência, sendo o ângulo de incidência apenas um fator de intensidade que representa o quanto a luz conseguiu excitar a estrutura. Porém, o mesmo não ocorre com os outros modos de energia, sendo um comportamento diferente do esperado. Para melhor observação, os dados podem ser representados em um mapa de calor, e isto é feito na Figura 4.7. Para demostrar a influência dos processos de tratamento de dados, a Figura A.3 apresenta 4 versões dos dados demostrando a evolução dos resultados conforme os algoritmos do software fazem os processamentos dos dados. No primeiro gráfico os dados de absorbância estão apenas filtrados, já no segundo gráfico é feito o tratamento para retirada de tendência e desvios, com isso os dados passam a estar no mesmo patamar, permitindo a comparação entre diferentes ângulos. No terceiro gráfico é realizada a filtragem 2D com o filtro gaussiano para retirar variações bruscas entre dados vizinhos. Por fim, no quarto gráfico é realizada a interpolação dos dados para eliminar as variações em degrau presente entre os diferentes ângulos. Os gráficos apresentados na Figura 4.7 demostra visualmente o deslocamento de alguns picos de ressonância. Para ângulos abaixo de 15 ◦ apenas um pico é observado entre 750 e 800 nm. Conforme o ângulo aumenta, outros dois picos distintos surgem em comprimentos de onda menores. Conforme o ângulo varia, o pico central em 725 nm permanece quase constante, enquanto os picos ao lado se aproximam e depois afastam. Com a variação do ângulo outros modos de energia surgem, como o pico em 850 nm. Este pico apresenta a propriedade de permanecer quase constante por quase todo o gráfico, o que é de interesse para as medidas biológicas, porque garante que qualquer deslocamento do pico ocorre em 4.3. MEDIDAS BIOLÓGICAS 37 virtude de fatores externos. Neste dispositivo ocorre que em determinados ângulos a interação entre o campo magné-tico incidente e a superfície induz de forma mais significativa o movimento de cargas livres. Para compreender os fenômenos relatados o dispositivo NP-A1 foi simulado em dois ângulos distintos: 31 ◦ e 41 ◦. Estes ângulos são notáveis por capturarem o momento em que todos os picos coexistem ao mesmo tempo, e o momento em que a ressonância em 850 nm é máxima. Na Figura 4.8-a os gráficos das Figuras 4.2 e 4.7 foram reunidos para auxiliar na visualiza-ção dos picos. Neste gráfico duas regiões estão marcadas: em azul a medida realizada em 

31 ◦ e em verde a medida em 41 ◦. Estas mesmas duas curvas estão apresentadas no gráfico da Figura 4.8-b, onde cada pico é numerado em ordem crescente. O resultado das simula-ções apresentou os mesmo 9 picos de ressonância, e a distribuição do campo elétrico para cada frequência de ressonância está demostrada no Figura 4.8-c. Pode ser observado que a exceção dos modos 3 e 7, os restantes possuem distribuição semelhante, com alta concentra-ção do campo elétrico na ponta da pirâmide. Este comportamento é conhecido e representa ressonâncias localizadas (LSPR). Por outro lado, os modos em 3 e 7 representam ondas de elétrons, conhecidas como Surface Plasmon Polaritons (SPP) [8]. Além das simulações, uma evidência forte para a presença de modos SPP é a interação que este modo teve com os picos 2 e 4. Do ângulo de 17 ◦ a 35 ◦ ocorre o fenômeno de anti-cruzamento ( anticrossing ) o qual é bastante comum na literatura quando é observado o acoplamento de modos SPP. Con-tudo, este acoplamente sempre é dado em função da variação das dimensões da geometria [5], mas o resultado obtido demostra o mesmo efeito em função do ângulo de incidência do campo elétrico. Apesar dos efeitos observados, o modo mais vantajoso para as medidas biológicas é o localizado em 850 nm, devido a sua estabilidade. Para este modo o ângulo de excitação demostrou ser um parâmetro de otimização, permitindo intensificar a absorção. O valor má-ximo do pico foi obtido no ângulo de 41 ◦, sendo este o utilizado para as medidas biológicas. Além destas medidas também foi realizada a varredura em ângulo do dispositivo NP-A2. Este por sua vez, não apresentou nenhum pico de ressonância distinto, apenas um platô de absorção que cresce com o ângulo, conforme a Figura A.4 mostra. Também foram realizadas medidas variando o ângulo azimutal no dispositivo NP-A1. Como pode ser observado na Figura 4.9 os resultados são simétricos e periódicos, se repe-tindo a cada 90 ◦. Isso se deve pela geometria quadrada da pirâmide, e as maiores intensidades observadas foram nos ângulos no qual a luz incidiu diretamente sobre a face das piramides, ou seja, nos ângulos 0◦, 90 ◦ e múltiplos de 90 ◦.

# 4.3 Medidas biológicas 

Como informado, as medidas biológicas foram realizadas no dispositivo NP-A1 com o ân-gulo de incidência de 41 ◦ e azimutal de 0◦. Todas as diluições citadas na Seção 3.2.3 foram feitas utilizando água deionizada, e devidamente armazenadas sob refrigeração. Sempre após a aplicação da gota contendo a proteína Pb27r 10 minutos foram esperados antes da realiza-ção das medidas, e ao final da medida o substrato foi limpo com água deionizada. Em todas as aplicações da amostra foi tomado o cuidado de cronometrar o tempo até a secagem. Foi observado que se o tempo até a secagem for longo a medida em geral não funciona ou apre-senta um deslocamento incoerente do pico de absorção. Isso ocorre devido ao efeito da borda de café ( Coffee ring effect ), nesse fenômeno o analito em meio aquoso tende a se concentrar 38 

CAPÍTULO 4. RESULTADOS 

Figura 4.8: Comparação entre dados medidos e resultados simulados: (a) medidas experi-mentais, (b) amostragem das medidas experimentais nos ângulos de 31 ◦ e 41 ◦ e (c) distribui-ção do campo elétrico na superfície da nanopirâmide em simulação. 4.4. RESUMO DO CAPÍTULO 39 

Figura 4.9: Mapa de calor para medidas no dispositivo NP-A1 variando o ângulo azimutal. nas bordas, criando uma distribuição não uniforme da proteína sobre as nanoestruturas. Para evitar este efeito, gotas menores são utilizadas, e as amostras são sempre diluídas em água deioniza, por possuir tempo de secagem mais rápido do que para diluições com água apenas destilada. Na Figura 4.10 é possível perceber o deslocamento do pico de absorção em direção ao infravermelho. Também é possível observar que após a limpeza do substrato com água o pico retorna para a posição inicial, mas podem apresentar algumas pequenas variações. Por isto, o deslocamento do pico sempre é comparado com relação a última lavagem do substrato. As diluições foram feitas em série, para produzir amostras com metade da concentração anterior. Dessa forma, foram produzidas as concentrações de 1:32, 1:64, 1:128 e 1:256 rela-tivas à concentração original de 0,5 mg/mL. A concentração mais alta utilizada nas medidas foi de 1:32, pois concentrações maiores não apresentaram resultados em virtude de terem saturado o sensor. Por outro lado, a menor concentração que o sensor conseguiu detectar dentro de sua margem de erro foi de 1:256. A Figura 4.11 apresenta o deslocamento do pico de absorção para a concentração relativa de 1:32. Nesta medida o pico inicial está próxima a 860 nm em virtude de resquícios de medidas anteriores. Este pico é deslocado para 885 nm após a aplicação da amostra, resultando em um deslocamento de aproximadamente 25 nm. Para cada concentração 3 medidas foram realizadas, realizando entre as medidas a lim-peza por água deionizada, ou quando necessária, a limpeza com acetona. A Figura 4.12 resume os resultados obtidos para cada uma das concentrações. Para cada concentração o gráfico apresenta a média e o desvio padrão das medidas. Sobre esses dados foi realizada uma regressão linear para encontrar a curva de calibração do sensor, correlacionando a con-centração do analito em μg/mL com o deslocamento do pico em nanômetros. Os parâmetros da reta gerada foram: inclinação de 1,546 nm/ μg/mL, e desvio de 10,38 nm. 

# 4.4 Resumo do Capítulo 

Neste capítulo foi apresentado os resultados gerados ao decorrer do projeto desenvolvido. Foi apresentada a estrutura de medição óptica construída e como os ajustes realizados me-40 

CAPÍTULO 4. RESULTADOS 

Figura 4.10: Absorbância antes e depois da aplicação das amostras biológicas, e lavagem do substrato. 

Figura 4.11: Deslocamento no pico de absorção após a aplicação da amostra na concentração de 1:32. 4.4 Metodologia 41 

Figura 4.12: Média do deslocamento do pico de absorção para cada concentração. lhoraram o feixe produzido. Com esta estrutura, medidas foram realizadas para conhecer o dispositivo utilizado, e alguns dispositivos se destacaram. Ainda, foi observada a relação en-tre os picos gerados e o ângulo de excitação da amostra, e como isto pode ser utilizado para maximizar a intensidade dos picos gerados. Por fim, o melhor pico de absorção foi escolhido e utilizado nas medidas biológicas, onde foi possível relacionar o deslocamento do pico com a concentração da amostra. 42 

CAPÍTULO 4. RESULTADOS Capítulo 5 Conclusões 

# 5.1 Considerações Finais 

Os resultados obtidos são fruto de um projeto de 3 anos, sendo os resultados mostrados consequência do primeiro ano de pesquisas. O projeto visa desenvolver uma plataforma para o diagnóstico da PCM (Paracoccidioidomicose). Está doença aflige milhares de pessoas no Brasil, mas apesar disso recebe pouco investimento para pesquisa e desenvolvimento de métodos de diagnóstico e tratamento. A existência de uma plataforma acessível que fornecesse diagnostico rápido a PCM auxiliaria no tratamento precoce da doença, evitando o desenvolvimento de sintomas graves e complicações nas pessoas contaminadas. Os resultados prévios de medidas com amostras puras de Pb27r demostraram a capaci-dade do dispositivo e da plataforma construída em detectar a presença da proteína, até mesmo em concentrações baixas. Além disso, foi possível correlacionar o deslocamento do pico de absorção com a concentração da proteína, sendo gerada uma curva de calibração. A plataforma desenvolvida também se demostrou vantajosa, quando comparada a outros métodos de medição. O sensor utilizado permite a otimização em variais camadas, desde a escolha das dimensões das nanoestruturas, até o uso do ângulo de incidência para maximi-zar a absorção no pico de ressonância. Isto permite uma regulagem fina dos resultados, e demostra tolerância a erros de fabricação. Também permite que o dispositivo seja otimizado para outros usos, possibilitando que a plataforma seja utilizada na detecção de outras doen-ças ou moléculas. Além disso, a fabricação por molde utilizada tende a reduzir os custos de fabricação conforme novos dispositivos são produzidos a partir de um mesmo molde. Ainda, o trabalho demostrou que um mesmo dispositivo pode ser reutilizado diversas vezes para diferentes medidas biológicas, sendo reutilizável após a lavagem. 

# 5.2 Propostas de Continuidade 

Há muito trabalho a ser desenvolvido nesta plataforma. Como um projeto de 3 anos, outras pessoas continuaram a estar envolvidas no desenvolvimento. Um dos próximos pontos a ser trabalhado é a bio funcionalização do sensor. Este processo tem como objetivo imobili-zar anticorpos na superfície das nanoestruturas, de forma que esses anticorpos capturem as proteínas de Pb27r diluídas na amostra. Dessa forma a medida se torna seletiva, pois cada anticorpo se liga a apenas um tipo de antígeno. O sensor como foi utilizado não discrimina 43 44 

CAPÍTULO 5. CONCLUSÕES 

a molécula que está em sua superfície, sendo assim, uma amostra do paciente, como muco ou escarro, geraria deslocamento do pico de ressonância em virtude de todas as moléculas presentes. Caso o dispositivo estivesse bio funcionalizado, com a aplicação da amostra os antígenos contendo Pb27r seriam capturados pelos anticorpos, e após a lavagem do substrato apenas as proteínas Pb27r seriam mantidas no substrato. Dessa forma, o deslocamento do pico de ressonância seria consequência unicamente da presença da proteína Pb27r. Neste trabalho não foi realizada a bio funcionalização, contudo, todas medidas foram realizadas com amostras puras de Pb27r, o que garante que nenhuma outra molécula está presente in-terferindo as medidas. Referências Bibliográficas 

[1] A. Bozzi, B. S. Reis, F. L. S. Prado, E. P. Pedroso, M. F. Leite, and A. M. Goes. Modulation of cd28 and cd86 expression in patients with paracoccidioidomycosis in different periods of treatment. Scandinavian Journal of Immunology , 60(5):500505, November 2004. [2] M. M. Correa, A. M. Bedoya, M. P. Guerrero, J. Méndez, A. Restrepo, and J. G. McEwen. Diagnosis of paracoccidioidomycosis by a dot blot assay using a recombinant paracoccidioides brasiliensis p27 protein. Mycoses , 50(1):4147, December 2006. [3] DEFINIÇÃO DE PRIORIDADES. Doenças negligenciadas: estratégias do ministério da saúde. 

Rev Saúde Pública , 44(1):200–2, 2010. [4] S.N. Diniz, B.S. Reis, T.S. Goes, C.S. Zouain, M.F. Leite, and A.M. Goes. Protective immunity induced in mice by f0 and fii antigens purified from paracoccidioides brasiliensis. Vaccine ,22(34):485492, January 2004. [5] Amitabh Ghoshal, Ivan Divliansky, and Pieter G. Kik. Experimental observation of mode-selective anticrossing in surface-plasmon-coupled metal nanoparticle arrays. Applied Physics Letters , 94(17), April 2009. [6] Gabriel L. Machado, Felipe M. F. Teixeira, Gabriel S. C. Ferreira, Alice F. Versiani, Lidia M. Andrade, Luiz O. Ladeira, Flávio G. da Fonseca, and Jhonattan C. Ramirez. Computational guided method applied to lsprbased biosensor for specific detection of the fourserotypes of dengue virus in seropositive patients. Particle amp; Particle Systems Characterization , 39(3), February 2022. [7] Manual MSD. Paracoccidioidomicose, 2024. Accessed: 2024-12-31. [8] Talles E. M. Marques, Yuri H. Isayama, Felipe M. F. Teixeira, Fabiano C. Santana, Rafael S. Gonçalves, Aline Rocha, Bruna P. Dias, Lidia M. Andrade, Estefânia M. N. Martins, Ronaldo A. P. Nagem, Clascidia A. Furtado, Miguel A. G. Balanta, Jorge Ricardo Mejía-Salazar, Paulo S. S. Guimarães, Wagner N. Rodrigues, and Jhonattan C. Ramirez. Tunable surface plasmon-polaritons interaction in all-metal pyramidal metasurfaces: Unveiling principles and significance for biosensing applications. ACS Applied Optical Materials , 2(7):13741381, July 2024. [9] J. R. Mejía-Salazar and Osvaldo N. Oliveira. Plasmonic biosensing: Focus review. Chemical Reviews , 118(20):1061710625, September 2018. [10] Antonio Minopoli, Adriano Acunzo, Bartolomeo Della Ventura, and Raffaele Velotta. Nanos-tructured surfaces as plasmonic biosensors: A review. Advanced Materials Interfaces , 9(2), November 2021. [11] World Health Organization. Neglected tropical diseases, 2024. Accessed: 2024-12-31. 

45 46 

REFERÊNCIAS BIBLIOGRÁFICAS 

[12] Marek Piliarik, Hana Vaisocherová, and Jií Homola. Surface Plasmon Resonance Biosensing ,page 6588. Humana Press, 2009. [13] Abraham. Savitzky and M. J. E. Golay. Smoothing and differentiation of data by simplified least squares procedures. Analytical Chemistry , 36(8):16271639, July 1964. [14] Wanderley de Souza et al. Doenças neglicenciadas. 2012. [15] Xuejing Wang, Junho Choi, Juncheng Liu, Oana Malis, Xiaoqin Li, Peter Bermel, Xinghang Zhang, and Haiyan Wang. 3d hybrid trilayer heterostructure: Tunable au nanorods and optical properties. ACS Applied Materials amp; Interfaces , 12(40):4501545022, September 2020. [16] Yingrui Zhang, Ziwei Ye, Chunchun Li, Qinglu Chen, Wafaa Aljuhani, Yiming Huang, Xin Xu, Chunfei Wu, Steven E. J. Bell, and Yikai Xu. General approach to surface-accessible plasmonic pickering emulsions for sers sensing and interfacial catalysis. Nature Communications , 14(1), March 2023. Apêndice A Imagens da caracterização 

# A.1 Seção 4.2 medição inicial de todas matrizes 

Figura A.1: Medidas de absorbância do Dispositivo NP-A1 no ângulo de 38 ◦.47 48 

APÊNDICE A. IMAGENS DA CARACTERIZAÇÃO 

Figura A.2: Medidas de absorbância do dispositivo NP-A2 no ângulo de 38 ◦.A.2. SEÇÃO 4.2 PROCESSAMENTO DOS DADOS PARA GERAÇÃO DE MAPAS DE CALOR 49 

# A.2 Seção 4.2 processamento dos dados para geração de mapas de calor 

Figura A.3: Resultados das etapas de processamento de dados: (a) dados filtrados em relação ao comprimento de onda, (b) Dados sem tendências e dêsvios, (c) dados filtrados em relação ao ângulo, (d) dados interpolados. 50 

APÊNDICE A. IMAGENS DA CARACTERIZAÇÃO 

# A.3 Seção 4.2 mapa de calor do dispositivo NP-A2 

Figura A.4: Mapa de calor para dispositivo NP-A2 variando o ângulo de incidencia.