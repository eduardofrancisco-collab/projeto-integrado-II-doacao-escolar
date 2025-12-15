# Projeto-integrado-II-doacao-escolar
Plataforma web de doação e reaproveitamento de materiais escolares

Conectando Livros e Sonhos
Uma plataforma para transformar material escolar parado em futuro para estudantes.

📖 Sobre o Projeto
Todos nós temos aquele livro didático na estante ou uma mochila usada que não serve mais, mas que está em ótimas condições. Do outro lado, existem milhares de estudantes que precisam exatamente desses itens para continuar seus estudos.

O Projeto nasceu para ser a ponte entre esses dois mundos. Não é apenas um software de gerenciamento; é uma ferramenta de impacto social que utiliza tecnologia para democratizar o acesso à educação e promover a sustentabilidade através do reuso.

Como funciona? 
Desenvolveremos este sistema utilizando Python, focando em escrever um código limpo e organizado. Para garantir que o sistema cresça de forma saudável, adotamos o paradigma de Orientação a Objetos (POO).

Imagine o sistema como uma escola real:

Abstração: Simplificamos o mundo real. No código, não precisamos saber a cor dos olhos do usuário, apenas seu contato e se ele quer doar ou receber.

Herança: Criamos uma classe "Mãe" chamada Usuario. Tanto o Doador quanto o Beneficiario são "filhos" dela. Isso evita repetição de código (ambos têm nome e e-mail, por exemplo).

Encapsulamento: Protegemos dados sensíveis. O contato do usuário não fica "solto" no código, ele é protegido dentro da classe.

* Tecnologias e Processos
Linguagem: Python 3.14

Versionamento: Git & GitHub

*Metodologia: O desenvolvimento será iterativo. Primeiro, focaremos em definir quem usaria o sistema (classes), depois o que seria trocado (objetos) e, por fim, as interações entre eles.

Possíveis usos da nossa solução
(Componente Extensionista)

Embora este seja um projeto acadêmico, o potencial de aplicação no mundo real é imediato e tangível:

Redes de Escolas Públicas: Secretarias de educação poderiam utilizar o sistema para remanejar livros didáticos sobrando em uma escola para outra que esteja com déficit, economizando verba pública.

ONGs e Coletivos de Bairro: O sistema pode servir como o "cérebro" de campanhas de volta às aulas, organizando quem doa e quem recebe, garantindo que o kit escolar chegue à criança certa.

Economia Circular: Ao facilitar o reuso de uniformes e mochilas, reduzimos o lixo têxtil e ajudamos famílias a economizarem no orçamento doméstico, permitindo que invistam esse dinheiro em outras necessidades, como alimentação ou transporte.

*Estrutura do Código
Para facilitar a leitura por outros desenvolvedores, separamos as responsabilidades:

src/modelos.py: Onde "vivem" as regras de negócio e as definições de Usuários e Materiais.

src/main.py: Onde a mágica acontece (execução e testes das funcionalidades).

* Como contribuir
Sinta-se à vontade para abrir uma issue ou enviar um pull request. Toda ajuda para melhorar a educação é bem-vinda!
