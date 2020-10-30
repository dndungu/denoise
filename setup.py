import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="denoise-pkg-dndungu",
    version="0.0.2",
    author="David Ndungu",
    author_email="david@ndungu.dev",
    description="Denoise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dndungu/denoise",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
