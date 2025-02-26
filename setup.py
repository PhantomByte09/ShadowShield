from setuptools import setup, find_packages

setup(
    name="ShadowShield",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "shadowshield=main:main",
        ],
    },
)
