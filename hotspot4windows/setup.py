import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hotspot4windows",
    version="1.19.1",
    author="ying2002",
    author_email="877259039@qq.com",
    description="Wireless hotspot Python package in Windows environment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ying2002/hotspot4windows",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)
