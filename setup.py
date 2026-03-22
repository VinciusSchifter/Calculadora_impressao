from setuptools import setup, find_packages


setup(
    name="meu_projeto_ci",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov", "flake8", "bandit"]
    },
)
