from setuptools import setup, find_packages

PROJECT_URL = 'https://github.com/pfalcon/sphinx_selective_exclude'
VERSION = '1.0.3'

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
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=None,
    namespace_packages=[],
    keywords = ['sphinx', 'only', 'plugin'],
)
