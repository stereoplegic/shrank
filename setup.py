import setuptools
from .src.shrank import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shrank",
    version=version,
    author="Samuel Cahyawijaya",
    author_email="samuel.cahyawijaya@gmail.com",
    description="Automatic Factorization package for PyTorch modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ScienceArtMagic/shrank",
    project_urls={
        "Bug Tracker": "https://github.com/ScienceArtMagic/shrank/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "transformers",
        "torch",
        "tqdm",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)
