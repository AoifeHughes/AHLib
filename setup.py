from setuptools import setup

setup(name='AH',
      version='0.1',
      description='Library for common functionalities, used to reduce code clutter',
      url='https://github.com/AoifeHuges/AHLib',
      author='Aoife Hughes',
      author_email='Aofie.hughes@jic.ac.uk',
      license='MIT',
      packages=['AH'],
      install_requires=[
          'numpy', 'matplotlib', 'scipy', 'networkx', 'pandas', 'tqdm'
      ],
      zip_safe=True)
