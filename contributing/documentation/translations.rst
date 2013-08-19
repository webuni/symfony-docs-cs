Překlady
========

Dokumentace Symfony2 je sice psána v angličtině, ale mnoho lidí pracuje
na překladech do různých jazyků.

Spolupráce
----------

Nejprve se dobře seznamte s :doc:`formátovacím jazykem <format>` používaným
pro psaní dokumentace.

Potom se přihlaste do `e-mailové konference Symfony dokumentace`_ a domluvte
se s ostatními na spolupráci.

Nakonec najděte *hlavní* repozitář pro překlad do jazyka, na kterém chcete
spolupracovat. Níže je uveden seznam oficiálních *hlavních* repozitářů:

* *Angličtina*:    https://github.com/symfony/symfony-docs
* *Čeština*:       https://github.com/webuni/symfony-docs-cs
* *Francouzština*: https://github.com/symfony-fr/symfony-docs-fr
* *Italština*:     https://github.com/garak/symfony-docs-it
* *Japonština*:    https://github.com/symfony-japan/symfony-docs-ja
* *Polština*:      https://github.com/symfony-docs-pl/symfony-docs-pl
* *Portugalština (Brazílie)*:  https://github.com/andreia/symfony-docs-pt-BR
* *Španělština*:   https://github.com/gitnacho/symfony-docs-es

.. note::

    Jak přeložit dokumentaci do nového jazyka se dozvíte v
    :ref:`samostatné kapitole <translations-adding-a-new-language>`.

Začlenění do překladatelského týmu
----------------------------------

Pokud chcete pomoci přeložit některé dokumenty do vašeho jazyka nebo opravit
chyby, připojte se k nám. Je to velmi jednoduché:

* Zapojte se do `e-mailové konference Symfony dokumentace`_ a dejte o sobě vědět.
* *(volitelně)* Zeptejte se, na jakých dokumentech můžete pracovat.
* Udělejte vlastní fork *hlavního* repozitáře pro daný jazyk (klikněte na tlačítko
  "Fork" na stránce GitHubu).
* Přeložte dokumenty.
* Vytvořte pull request (stiskněte tlačítko "Pull Request" na vašich stránkách
  na GitHubu).
* Správce *hlavního* repozitáře přijme vaše změny a začlení je do repozitáře.
* Webové stránky dokumentace jsou aktualizovány každou noc z hlavního repozitáře.

.. _translations-adding-a-new-language:

Přidání nového překladu
-----------------------

V této kapitole je uveden návod na vytvoření překladu Symfony2 dokumentace
do nového jazyka.

Vytvořit překlad dá hodně práce, a proto napište o tomto plánu do
`e-mailové konference Symfony dokumentace`_ a zkuste najít podobně motivované
lidi, kteří jsou ochotni pomoct.

Když je vytvořen tým lidí, vyberte si správce, který bude zodpovědný za *hlavní*
úložiště překladu.

Vytvořte repozitář a zkopírujte dokumenty z *anglické* verze dokumentace.

Tým se může pustit do samotného překladu.

Když je vše přeloženo nebo nepřeložené dokumenty jsou odstraněny z obsahu
(soubory pojmenované ``index.rst`` a ``map.rst.inc``), může správce poslat
email Fabienovi (fabien at symfony.com) s žádostí o přidání repozitáře do
seznamu oficiálních *hlavních* repozitářů.

Udržování překladu
------------------

Překlad se nemůže zastavit ve chvíli, kdy jsou všechny dokumenty přeloženy.
Dokumentace se stále mění, přidávají se nové dokumenty, opravují se chyby,
přeuspořádávají se odstavce. Překladatelský tým musí pozorně sledovat repozitář
s anglickou verzí dokumentace a změny co nejdříve promítnout do přeložených dokumentů.

.. caution::

    Neudržované překlady budou odstraněny z oficiálního seznamu, protože
    zastaralá dokumentace je nebezpečná.

.. _e-mailové konference Symfony dokumentace: http://groups.google.com/group/symfony-docs
