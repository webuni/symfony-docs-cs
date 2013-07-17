# -*- coding: utf-8 -*-

project = 'Symfony dokumentace'
master_doc = 'index'
language = 'cs'

highlight_language = 'php'

# enable highlighting for PHP code not between ``<?php ... ?>`` by default
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)

# use PHP as the primary domain
primary_domain = 'php'

# set url for API links
api_url = 'http://api.symfony.com/master/%s'
