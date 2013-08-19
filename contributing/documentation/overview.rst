Jak přispívat do dokumentace
============================

Dokumentace je stejně důležitá jako samotný kód a tak pro ni platí stejné zásady:
musí být stručná, testovatelná, jednoduše udržovatelná, rozšířitelná a musí se
neustále vylepšovat. A samozřejmě také dokumentace obsahuje chyby, překlepy a špatně
čitelné kapitoly.

Spolupráce
----------

Před přispíváním do dokumentace se musíte seznámit s :doc:`značkovacím
jazykem <format>` používaným pro její zápis.

Repozitář Symfony2 dokumentace je umístěn na GitHubu:

.. code-block:: text

    https://github.com/symfony/symfony-docs

Pokud chcete poslat opravu, vytvořte `fork`_ (kopii) oficiálního repozitáře na GitHubu
a potom si naklonujte vaši kopii:

.. code-block:: bash

    $ git clone git://github.com/YOURUSERNAME/symfony-docs.git

Repozitář dokumentace je rozdělen na několik větví, stejně jako je tomu u repozitáře
se zdrojovým kódem Symfony. Každá větev odpovídá konkrétní verzi Symfony. Větev ``master``
obsahuje dokumentaci pro vývojovou větev zdrojového kódu.

Pokud píšete dokumentaci pro funkci, která byla představena *po* vydání Symfony 2.2
(např. v Symfony 2.3), měly by být vaše změny vždy založeny na větvi 2.2.
Proto nejprve proveďte checkout větve 2.2:

.. code-block:: bash

    $ git checkout 2.2

.. tip::

    Základní větev (např. 2.2) bude uvedena v sekci "Applies to",
    jak si ukážeme později v kapitole :ref:`doc-contributing-pr-format`.

Dále vytvořte novou větev pro vaše změny:

.. code-block:: bash

    $ git checkout -b improving_foo_and_bar

V této větvi udělejte změny a komitněte je. Když jste hotovi, nahrajte větev s úpravami
do *vašeho* repozitáře na GitHubu a vytvořte pull request.

Vytvoření Pull Requestu
~~~~~~~~~~~~~~~~~~~~~~~

Podle výše uvedeného příkladu bude pull request vytvořen mezi větví ``improving_foo_and_bar``
a větví ``master`` v repozitáři ``symfony-docs``.

Pokud jste provedli změny na větvi 2.2, pak se také na tuto větev musíte přepnout
kliknutím na tlačítko ``edit`` v horní části stránky:

.. image:: /images/docs-pull-request-change-base.png
   :align: center

.. note::

  Všechny změny provedené ve větvi (např. 2.2) budou začleněny do "novější"
  větve (např. 2.3, master atd.).

Jak se používají `pull requesty`_ je podrobně popsáno na stránkách GitHubu.

.. note::

    Symfony2 dokumentace podléhá licenci Creative Commons
    Attribution-Share Alike 3.0 Unported :doc:`License <license>`.

Před název pull requestu můžete v určitých situacích dát následující předpony:

* ``[WIP]`` (Work in Progress) se použije pokud nejste s prací sice ještě hotovi,
  ale byli byste rádi, aby se někdo na vaši práci podíval a zkontroloval. Až řeknete,
  že je pull request hotov, bude sloučen.

* ``[WCM]`` (Waiting Code Merge) se používá v případě, že jste zdokumentovali
  funkci, která ještě nebyla začleněna do repozitáře se zdrojovým kódem. Pull
  request bude sloučen v okamžiku, až bude nová funkčnost začleněna do
  repozitáře s kódem. Pokud navrhovaná funkčnost bude odmítnuta, tak bude pull
  request uzavřen.

.. _doc-contributing-pr-format:

Formát Pull Requestu
~~~~~~~~~~~~~~~~~~~~

Pokud jste opravili drobné chyby, pull requestu **musí** obsahovat popis
s následujícími údaji, aby mohl být přezkoumán bez zbytečných průtahů a co
nejrychleji začleněn:

.. code-block:: text

    | Q             | A
    | ------------- | ---
    | Doc fix?      | [yes|no]
    | New docs?     | [yes|no] (případně uvést číslo PR v repozitáři symfony/symfony)
    | Applies to    | [čísla verzí Symfony, kterých se úprava týká]
    | Fixed tickets | [čárkou oddělený seznam úkolů, které PR opravuje]

Správně vyplněný popis může vypadat třeba takhle:

.. code-block:: text

    | Q             | A
    | ------------- | ---
    | Doc fix?      | yes
    | New docs?     | yes (symfony/symfony#2500)
    | Applies to    | all (or 2.3+)
    | Fixed tickets | #1075

.. tip::

    Buďte prosím trpěliví. Vaše začleněné změny se na stránkách symfony.com mohou
    projevit do 15 minut, ale také až za několik dnů. Na stránce
    `Documentation Build Errors`_ můžete zkontrolovat, zda vaše úpravy nezpůsobily
    nějaké chyby během vytváření dokumentace. Tato stránka je aktualizována vždy ve
    3 hodiny ráno.

Zdokumentování nové funkce nebo změny chování
---------------------------------------------

Pokud jste vytvořili dokumentaci pro novou funkci Symfony2, měli byste před
jejím popisem uvést informaci pomocí příkazu ``.. versionadded:: 2.X``, ve které
verzi Symfony byla tato funkce přidaná:

.. code-block:: rest

    .. versionadded:: 2.3
        Metoda ``askHiddenResponse`` byla přidána v Symfony 2.3.

    Můžete také položit otázku a skrýt odpověď. To je zvláště...

Pokud jste zdokumentovali změnu chování je velmi užitečné, tuto změnu chování
*krátce* popsat.

.. code-block:: rest

    .. versionadded:: 2.3
        Funkce ``include()`` je novou Twig funkcí, která je dostupná také
        v Symfony 2.3. Předtím se používal tag ``{% include %}``.

Při každém vydání nové verze Symfony2 (např. 2.4, 2.5, atd.) je vytvořena
odpovídající větev z ``master`` větve. V tomto okamžiku jsou odstraněny všechny
tagy ``versionadded``, které se týkají nepodporovaných verzí Symfony2. Pokud
by tedy byla vydaná například Symfony 2.5 a Symfony 2.2 by se stala nepodporovanou
verzí, všechny tagy  ``.. versionadded:: 2.2`` by byly odstraněny z 2.5 větve.

Standardy
---------

Všechny stránky Symfony dokumentace musí odpovídat
:doc:`pravidlům pro psaní dokumentace <standards>`.

Oznámení chyby
--------------

Nejsnadněji můžete do dokumentace přispět opravou překlepu, gramatické chyby,
špatného příkladu nebo nesprávného vysvětlení.

Postup:

* Nahlaste chybu v systému pro evidenci chyb.

* *(volitelně)* Pošlete opravu.

Překlady
--------

Přečtěte is samostatný :doc:`dokument o překladech <translations>`.

.. _`fork`: https://help.github.com/articles/fork-a-repo
.. _`pull requesty`: https://help.github.com/articles/using-pull-requests
.. _`Documentation Build Errors`: http://symfony.com/doc/build_errors

Udržování verzí
---------------

Symfony má standardizovaný proces vydávání verzí, o kterém se dočtete v dokumentu
:doc:`/contributing/community/releases`.

S ohledem na tento proces musí dokumentační tým dělat několik změn v dokumentaci.

Když se verze stane "neudržovanou verzí"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Každá verze se jednou stane "neudržovanou". Více informací je uvedeno
v kapitole :ref:`contributing-release-maintenance`.

Když se verze přestane udržovat, provedou se v dokumentaci následující kroky.
Předpokládejme pro tento případ, že verze 2.1 se právě stala neudržovanou verzí:

* Změny a pull requesty již nebudou začleněny do větve 2.1, kromě bezpečnostních
  aktualizací, které jsou začleňování až do okamžiku ukončení podpory verze.

* Do všech udržovaných větví (např. 2.2 a vyšší) budou začleňovány pull
  requesty, které budou založeny na aktuálně nejstarší udržované verzi (tj. 2.2)
  nebo novější.

* Z ``master`` větve se odstraní příkazy ``.. versionadded:: 2.1`` a všechny
  další poznámky o přidaných nebo změněných funkcí, týkající se neudržované větve.
  Tím se dosáhne toho, že další verze, která bude první *po* ukončení údržby
  příslušné větve, nebude obsahovat zmínky o staré verzi (tj. 2.1).

Je-li vytvořena nová větev pro novou verzi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Během :ref:`stabilizační fáze<contributing-release-development>` se vytvoří nová
větev pro dokumentaci. Pokud je tedy například verze 2.3 ve fázi stabilizace,
vytvoří se nová větev s názvem 2.3. Potom se provedou následující změny:

* Změní se všechny odkazy na správnou verzi (např. 2.3). Například v kapitole
  o instalaci je odkaz na verzi, kterou byste měli použít pro instalaci. Podívejte
  se blíže na změny provedené v `PR #2688`_.

.. _`PR #2688`: https://github.com/symfony/symfony-docs/pull/2688
