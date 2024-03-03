import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="web3_calculator",
    version="0.0.7",
    py_modules=["web3_calculator"],
    author="Zcb991",
    author_email="2952964392@qq.com",
    description="A simple web3 calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zcb991/web3-calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)