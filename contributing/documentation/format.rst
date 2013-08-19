Formátování
===========

Symfony2 dokumentace se píše do obyčejných textových souborů, v nichž se používá
značkovací jazyk `reStructuredText`_. Z těchto souborů se pomocí nástroje `Sphinx`_
generuje dokumentace v požadovaném formátu (HTML, PDF, ...).

reStructuredText
----------------

reStructuredText "je snadno čitelný a přehledný textový značkovací jazyk a zároveň
systém pro parsování tohoto jazyka".

Syntaxi se lze naučit jednak ze zdrojových souborů Symfony2 `dokumentace`_
nebo z kapitoly `Základy reStructuredText`_ dostupné na domovské stránce
nástroje Sphinx.

Pokud znáte značkovací jazyk Markdown buďte opatrní, protože některé značky jsou
si velmi podobné, ale liší se jejich význam:

* Položky seznamu začínají na začátku řádku (není nutné odsazení).

* Řádkové bloky kódu používají dvoje uvozovky (````takhle````).

Sphinx
------

Sphinx je generátor dokumentace ze souborů psaných ve formátu reStructuredText.
Navíc ke standardním reST `značkám`_ přidává nová rozšíření, příkazy a role.

Zvýraznění kódu
~~~~~~~~~~~~~~~

Výchozím jazykem pro zvýrazňování kódu je PHP. Změnu jazyka lze provést
pomocí ``code-block``:

.. code-block:: rst

    .. code-block:: yaml

        { foo: bar, bar: { foo: bar, bar: baz } }

Pokud PHP kód začíná značkou ``<?php``, potom je nutné změnit jazyk pro zvýrazňování
na ``html+php``:

.. code-block:: rst

    .. code-block:: html+php

        <?php echo $this->foobar(); ?>

.. note::

    Seznam podporovaných jazyků je dostupný na stránkách knihovny `Pygments`_.

.. _docs-configuration-blocks:

Konfigurační bloky
~~~~~~~~~~~~~~~~~~

Kdykoliv chcete uvést konfiguraci ve všech podporovaných formátech
(``PHP``, ``YAML`` a ``XML``), musíte použít příkaz ``configuration-block``

.. code-block:: rst

    .. configuration-block::

        .. code-block:: yaml

            # Konfigurace v YAML

        .. code-block:: xml

            <!-- Konfigurace v XML //-->

        .. code-block:: php

            // Konfigurace v PHP

Předchozí kód se vykreslí jako:

.. configuration-block::

    .. code-block:: yaml

        # Konfigurace v YAML

    .. code-block:: xml

        <!-- Konfigurace v XML //-->

    .. code-block:: php

        // Konfigurace v PHP

Seznam podporovaných formátů:

+-----------------+-------------+
| Zápis           | Zobrazí se  |
+=================+=============+
| html            | HTML        |
+-----------------+-------------+
| xml             | XML         |
+-----------------+-------------+
| php             | PHP         |
+-----------------+-------------+
| yaml            | YAML        |
+-----------------+-------------+
| jinja           | Twig        |
+-----------------+-------------+
| html+jinja      | Twig        |
+-----------------+-------------+
| html+php        | PHP         |
+-----------------+-------------+
| ini             | INI         |
+-----------------+-------------+
| php-annotations | Anotace     |
+-----------------+-------------+

Vkládání odkazů
~~~~~~~~~~~~~~~

Chcete-li přidat odkaz na jinou stránku z dokumentace, použijte následující zápis:

.. code-block:: rst

    :doc:`/path/to/page`

Použijte cestu a název souboru bez přípony, například:

.. code-block:: rst

    :doc:`/book/controller`

    :doc:`/components/event_dispatcher/introduction`

    :doc:`/cookbook/configuration/environments`

Jako text odkazu bude použit hlavní nadpis odkazované stránky. Txet odkazu
však můžete změnit:

.. code-block:: rst

    :doc:`Spooling Email</cookbook/email/spool>`

Také můžete vytvářet odkazy na API dokumentaci:

.. code-block:: rst

    :namespace:`Symfony\\Component\\BrowserKit`

    :class:`Symfony\\Component\\Routing\\Matcher\\ApacheUrlMatcher`

    :method:`Symfony\\Component\\HttpKernel\\Bundle\\Bundle::build`

A nebo odkazy na PHP dokumentaci:

.. code-block:: rst

    :phpclass:`SimpleXMLElement`

    :phpmethod:`DateTime::createFromFormat`

    :phpfunction:`iterator_to_array`

Generování dokumentace
~~~~~~~~~~~~~~~~~~~~~~

Chcete-li si vyzkoušet dokumentaci před komitem:

* Nainstalujte `Sphinx`_.

* Postupujte podle návodu `rychlé nastavení Sphinx`_.

* Nainstalujte potřebná rozšíření (viz níže).

* Spusťte příkaz ``make html`` a prohlédněte si vygenerovanou HTML dokumentaci v adresáři ``build``.

Instalace Sphinx rozšíření
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    Repozitář českého překladu Symfony2 dokumentace obsahuje všechny potřebné soubory.
    Pro instalaci potřebných rozšíření stačí spustit příkaz:

    .. code-block:: bash

        $ pip install -r requirements.txt

* Stáhněte si požadované rozšíření z jeho `repozitáře`_.

* Zkopírujte adresář ``sensio`` do složky ``_exts`` v hlavním adresáři dokumentace
  (adresář, kde se nachází soubor ``conf.py``).

* Přidejte následující kód do souboru ``conf.py``:

.. code-block:: py

    # ...
    sys.path.append(os.path.abspath('_exts'))

    # adding PhpLexer
    from sphinx.highlighting import lexers
    from pygments.lexers.web import PhpLexer

    # ...
    # add the extensions to the list of extensions
    extensions = [..., 'sensio.sphinx.refinclude', 'sensio.sphinx.configurationblock', 'sensio.sphinx.phpcode']

    # enable highlighting for PHP code not between ``<?php ... ?>`` by default
    lexers['php'] = PhpLexer(startinline=True)
    lexers['php-annotations'] = PhpLexer(startinline=True)

    # use PHP as the primary domain
    primary_domain = 'php'

    # set url for API links
    api_url = 'http://api.symfony.com/master/%s'

.. _reStructuredText:         http://docutils.sourceforge.net/rst.html
.. _Sphinx:                   http://sphinx-doc.org/
.. _dokumentace:              https://github.com/symfony/symfony-docs
.. _Základy reStructuredText: http://sphinx-doc.org/rest.html
.. _značkám:                  http://sphinx-doc.org/markup/
.. _Pygments:                 http://pygments.org/languages/
.. _repozitáře:               https://github.com/fabpot/sphinx-php
.. _rychlé nastavení Sphinx:  http://sphinx-doc.org/tutorial.html#setting-up-the-documentation-sources
