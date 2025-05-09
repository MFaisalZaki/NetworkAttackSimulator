import pathlib

from setuptools import setup, find_packages

extras = {
    'dqn': [
        'torch>=1.5',
        'tensorboard>=2.2'
    ],
    'docs': [
        'sphinx>=3.0',
        'sphinx-rtd-theme>=0.4'
    ],
    'test': [
        'pytest>=8.3.2'
    ]
}

extras['all'] = [item for group in extras.values() for item in group]


def get_version():
    """Gets the posggym version."""
    path = pathlib.Path(__file__).absolute().parent / "nasim" / "__init__.py"
    content = path.read_text()

    for line in content.splitlines():
        if line.startswith("__version__"):
            return line.strip().split()[-1].strip().strip('"')
    raise RuntimeError("bad version data in __init__.py")


setup(
    name='nasim',
    version=get_version(),
    url="https://networkattacksimulator.readthedocs.io",
    description="A simple and fast simulator for remote network pen-testing",
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author="Jonathon Schwartz",
    author_email="Jonathon.Schwartz@anu.edu.au",
    license="MIT",
    packages=[
        package for package in find_packages()
        if package.startswith('nasim')
    ],
    install_requires=[
        'gymnasium>=0.26.3',
        'numpy==1.26.0',
        'networkx>=3.3',
        'matplotlib>=3.9.2',
        'pyyaml>=6.0.2',
        'prettytable>=3.11.0'
    ],
    extras_require=extras,
    python_requires='>=3.12.0',
    package_data={
        'nasim': ['scenarios/benchmark/*.yaml']
    },
    project_urls={
        'Documentation': "https://networkattacksimulator.readthedocs.io",
        'Source': "https://github.com/Jjschwartz/NetworkAttackSimulator/",
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12.4',
    ],
    zip_safe=False
)
