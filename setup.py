from setuptools import setup, find_packages

setup(
    name='enp-ai',
    version='0.1.0',
    description='Evolving Neural Protocol – Framework de IA inspirado em redes neurais esparsas e aprendizado evolutivo',
    author='Specter Software LTDA',
    author_email='contato@spectersoftware.com.br',
    url='https://github.com/SpecterLTDA/ENP',
    packages=find_packages(include=['enp', 'enp.*']),
    install_requires=[
        'numpy>=1.21.0',
        'matplotlib>=3.4.0',
        'pytest>=6.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    python_requires='>=3.8',
)
