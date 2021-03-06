from setuptools import setup

setup(name='structcol',
      version='0.2',
      description='Python package for modeling structural color in colloidal systems.',
      url='https://github.com/manoharan-lab/structural-color',
      author='Manoharan Lab, Harvard University',
      author_email='vnm@seas.harvard.edu',
      packages=['structcol'],
      install_requires=['pint', 'numpy', 'scipy'])
