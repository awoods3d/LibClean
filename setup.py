try:
    import setuptools
except ImportError:
    print('WARNING: setuptools not installed')


setuptools.setup(
    name="LibClean", # Replace with your own username
    version="1.0.1",
    author="Max Collins with Andrew Woods",
    author_email="A.Woods@curtin.edu.au",
    description="A package to read library catalogues and update OldPerth website",
    url="https://github.com/awoods3d/LibClean",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=[
        "pymarc", "tqdm","requests","Pillow","pydrive"
    ],
    zip_safe=False
)
