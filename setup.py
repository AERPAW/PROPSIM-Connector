from setuptools import setup

setup(
        name="pchem",
        version="0.1.0",
        description="PROPSIM connection framework",
        author="Simran Singh",
        # author_email="",
        packages=["pchem"],
        install_requires=[
            "sphinx",
            "sphinx-rtd-theme",
            "sphinx-argparse",
            "sphinx-simplepdf",
            "enum-tools[sphinx]",
            "flake8",
            "myst-parser",
            "toml",
            "flask",
            "numpy",
            "pyproj",
            ]
        )
