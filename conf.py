# -*- coding: utf-8 -*-

extensions = ['webuni.sphinx.symfonydocs']

html_title = project = 'Symfony dokumentace'
master_doc = 'index'
language = 'cs'

version = '2.3'
release = '2.3'

exclude_patterns = ['build', 'ENV', 'github']

html_theme = 'symfonydocs_cs'

highlight_language = 'php'

# use PHP as the primary domain
primary_domain = 'php'

# set url for API links
api_url = 'http://api.symfony.com/2.3/%s'

# set branch for edit links
html_context = {
    'github_branch': '2.3',
    'github_repository': 'webuni/symfony-docs-cs'
}

github_dir = 'github'
github_docs = [
    dict(group_name = 'Symfony dokumentace', repository ='symfony/symfony-docs', sha ='2.3', target_path = ''),
    dict(group_name = 'Symfony CMF dokumentace', repository ='symfony-cmf/symfony-cmf-docs', sha ='master', target_path = 'cmf'),
    dict(group_name = 'SensioFrameworkExtraBundle dokumentace', repository ='sensiolabs/SensioFrameworkExtraBundle', sha ='master', source_path = 'Resources/doc', target_path = 'bundles/SensioFrameworkExtraBundle'),
    dict(group_name = 'SensioGeneratorBundle dokumentace', repository ='sensiolabs/SensioGeneratorBundle', sha ='master', source_path = 'Resources/doc', target_path = 'bundles/SensioGeneratorBundle'),
    dict(group_name = 'DoctrineFixturesBundle dokumentace', repository ='doctrine/DoctrineFixturesBundle', sha ='master', source_path = 'Resources/doc', target_path = 'bundles/DoctrineFixturesBundle'),
    dict(group_name = 'DoctrineMigrationsBundle dokumentace', repository ='doctrine/DoctrineMigrationsBundle', sha ='master', source_path = 'Resources/doc', target_path = 'bundles/DoctrineMigrationsBundle'),
    dict(group_name = 'DoctrineMongoDBBundle dokumentace', repository ='doctrine/DoctrineMongoDBBundle', sha ='master', source_path = 'Resources/doc', target_path = 'bundles/DoctrineMongoDBBundle'),
]
