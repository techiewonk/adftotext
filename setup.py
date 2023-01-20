from setuptools import setup, find_packages

VERSION = '0.0.18'
DESCRIPTION = 'Convert ADF (Atlassian Document Format) to Plain Texts'
LONG_DESCRIPTION = 'ADF is basically JSON Document. To use it in places like Google Sheet, it needs to parsed and converted to Simple Texts. This is what is being done here.'

# Setting up
setup(
    name="adftotxt",
    version=VERSION,
    author="Koushik Choudhury",
    author_email="<koushikchoudhury0@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    keywords=['python', 'atlassian', 'adf', 'text', 'simpletext'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)