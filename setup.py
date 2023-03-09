from distutils.core import setup
import setuptools

with open('README.rst', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name='nornir_pysros',
  packages=['nornir_pysros', 'nornir_pysros.tasks'],
  version='0.1.0',
  license='bsd-3-clause',
  description='pysros plugin for Nornir.',
  long_description="",
  # long_description=long_description,
  long_description_content_type='text/x-rst',
  author='Julien CORSINI',
  author_email='j.corsini@hotmail.co.uk',
  url='https://github.com/akarneliuk/nornir_pygnmi',
  download_url='https://github.com/akarneliuk/nornir_pygnmi/archive/v0.2.0.tar.gz',
  keywords=['pysros', 'automation', 'nokia', 'network', 'netconf'],
  install_requires=[
          'nornir',
          'pysros'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Telecommunications Industry',
    'Operating System :: OS Independent',
    'Topic :: System :: Networking',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
  ],
  python_requires=">=3.7",
    entry_points="""
    [nornir.plugins.connections]
    pygnmi=nornir_pysros.connection:PysrosNornirConnectionPlugin
    """
)
