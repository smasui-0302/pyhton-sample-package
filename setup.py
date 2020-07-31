import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    # 必要な依存ライブラリがあれば記述
]

packages = [
    'solima'
]

setuptools.setup(
    name="solima",
    version="0.1.0",
    packages=packages,
    install_requires=install_requires,
    entry_points={'console_scripts': console_scripts},
)