from setuptools import setup, find_packages

version = '2.0b3'
readme = open("README.txt").read()
history = open('CHANGES.txt').read()

setup(name = 'collective.solr',
      version = version,
      description = 'Solr integration for external indexing and searching.',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],
      keywords = 'plone cmf zope indexing searching solr lucene',
      author = 'Jarn AS',
      author_email = 'info@jarn.com',
      url = 'http://plone.org/products/collective.solr',
      license = 'GPL version 2',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages = ['collective'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
        'Acquisition',
        'collective.indexing >1.6',
        'collective.js.showmore',
        'DateTime',
        'elementtree',
        'Plone >=4.0',
        'plone.app.content',
        'plone.app.controlpanel',
        'plone.app.layout',
        'plone.browserlayer',
        'plone.indexer',
        'Products.Archetypes',
        'Products.CMFCore',
        'Products.CMFDefault',
        'Products.GenericSetup',
        'setuptools',
        'transaction',
        'ZODB3',
        'zope.component',
        'zope.formlib',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.publisher',
        'zope.schema',
        'Zope2',
      ],
      extras_require = { 'test': [
        'cElementTree',
        'collective.testcaselayer',
        'Products.LinguaPlone >=3.1a1',
        'Products.PloneTestCase',
      ]},
      entry_points = '''
        [z3c.autoinclude.plugin]
        target = plone
        [zopectl.command]
        solr_clear_index = collective.solr.commands:solr_clear_index
        solr_dump_catalog = collective.solr.commands:solr_dump_catalog
        solr_import_dump = collective.solr.commands:solr_import_dump
      ''',
)
