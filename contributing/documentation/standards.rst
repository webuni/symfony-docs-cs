Pravidla pro psaní dokumentace
==============================

Aby dokumentace co nejlépe čtenářům pomohla, je nutné mít dobře a jednotně vypadající
příklady a dodržovat následující standardy.

Sphinx
------

* Pro jednotlivé úrovně nadpisů se označují následujícími znaky:
  ``=`` pro 1. úroveň, ``-`` 2. úroveň, ``~`` 3. úroveň, ``.`` 4 úroveň
  a ``"`` pro 5. úroveň.
* Každý řádek by měl být zalomen za prvním slovem, které následuje za 72. znakem.
  Takže většina řádků bude mít 72-78 znaků.
* Pro označení PHP kódu je *upřednostňován* zkrácený zápis ``::`` před příkazem``.. code-block:: php``
  (přečtěte si `Sphinx dokumentaci`_, abyste věděli, kdy lze použít tento zkrácený zápis).
* Vložené http odkazy se **nesmí** používat. Oddělte text odkazu od jeho adresy, kterou
  uvedete až na konci stránky.
* Text by se měl být psát formou *vy* místo *my*.

Příklad
~~~~~~~

.. code-block:: rest

    Příklad
    =======

    Při práci na dokumentaci byste se měli řídit standardy pro `Symfony dokumentaci`_.

    2. úroveň
    ---------

    Ukázka PHP kódu::

        echo 'Hello World';

    3. úroveň
    ~~~~~~~~~

    .. code-block:: php

        echo 'Zde nemůžete použít zkácený zápis s ::';

    .. _`Symfony dokumentaci`: http://symfony.com/doc/current/contributing/documentation/standards.html

Ukázky kódu
-----------

* Kód musí dodržovat jak :doc:`Symfony pravidla pro psaní kódu</contributing/code/standards>`,
  tak také `Pravidla pro psaní Twig šablon`_;
* Aby nebylo nutné skrolovat kód do stran, je lepší zalomit řádek tak, aby měl maximálně 85 znaků.
* Pokud vynecháte více řádků kódu, napiště v tomto místě komentář s textem ``...```.
  Zápisy komentářů jsou: ``// ...`` (php), ``# ...`` (yaml/bash), ``{# ... #}``
  (twig), ``<!-- ... -->`` (xml/html), ``; ...`` (ini) a ``...`` (text).
* Pokud vynecháte část řádku kódu (např. hodnota proměnné), nahraďte vynechané místo
  textem ``...`` (bez dodatečných komentářů).
* Popis vynechaného kódu: (volitelné)
  pokud jste vynechali několik řádků kódu, tak popis umístěte za text ``...``,
  pokud jste vynechali pouze část řádku, tak umístěte popis na předchozí řádek.
* Pokud je to vhodné, tak by blok kódu měl začínat komentářem s názvem souboru,
  ze kterého je daná ukázka. Za tímto komentářem nepřidávejte prázdný řádek kromě případu,
  kdy další řádek obsahuje také komentář.
* Před každým řádkem konzole by měl být znak ``$``.

Formáty
~~~~~~~

Příklady konfigurací by měly být uvedeny ve všech podporovaných formátech
pomocí :ref:`konfiguračních bloků <docs-configuration-blocks>`. Jednotlivé formáty
a jejich doporučované pořadí:

* **Konfigurace** (včetně služeb a routování): Yaml, Xml, Php
* **Validace**: Yaml, Anotace, Xml, Php
* **Doctrine mapování**: Anotace, Yaml, Xml, Php

Příklad
~~~~~~~

.. code-block:: php

    // src/Foo/Bar.php

    // ...
    class Bar
    {
        // ...

        public function foo($bar)
        {
            // set foo with a value of bar
            $foo = ...;

            // ... check if $bar has the correct value

            return $foo->baz($bar, ...);
        }
    }

.. caution::

    V Yaml souborech by se měla udělat mezera u složených závorek, tj. za ``{`` a před ``}``
    (např. ``{ _controller: ... }``), ale v Twig šablonách se žádné mezery u složených závorek
    nepřidávají (např. ``{'hello' : 'value'}``).

.. _`Sphinx dokumentaci`: http://sphinx-doc.org/rest.html#source-code
.. _`Pravidla pro psaní Twig šablon`: http://twig.sensiolabs.org/doc/coding_standards.html
