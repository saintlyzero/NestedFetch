from setuptools import setup, find_packages

setup(
  name = 'nestedfetch',
  packages = ['nestedfetch'],
  version = '0.1.1',
  license='MIT',
  description = 'Syntactic sugar to perform GET, SET and FLATTEN values from nested dictionaries and nested lists.',
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  author = 'Shubham Dalvi',
  author_email = 'shubham.dalvi97@gmail.com', 
  url = 'https://github.com/saintlyzero/NestedFetch',
  download_url = ('https://github.com/saintlyzero/NestedFetch/archive/v_011.tar.gz'),
  keywords = ['dict','nested dictionary','nested list','list','flatten','scalpl','nestedfetch','addict','box','Nested Fetch'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    "Programming Language :: Python :: 3.7"
  ]
)