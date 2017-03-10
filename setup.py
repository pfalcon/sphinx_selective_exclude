from setuptools import setup, find_packages

PROJECT_URL = 'https://github.com/pfalcon/sphinx_selective_exclude'
VERSION = '1.0.0'

setup(
    name='sphinx_selective_exclude',
    version=VERSION,
    url=PROJECT_URL,
    download_url=PROJECT_URL + '/tarball/' + VERSION,
    license='MIT license',
    author='Paul Sokolovsky',
    author_email='pfalcon@users.sourceforge.net',
    description='Sphinx eager ".. only::" directive and other selective rendition extensions',
    long_description=open("README.md").read(),
    zip_safe=False,
    classifiers=[],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=None,
    namespace_packages=[],
    keywords = ['sphinx', 'only', 'plugin'],
)