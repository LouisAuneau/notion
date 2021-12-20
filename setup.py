import setuptools

with open("VERSION", "r", encoding="utf-8") as f:
    version = f.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notion",
    version=version,
    author="Louis AUNEAU",
    author_email="louis.auneau.c@gmail.com",
    description="Python library to interact with Notion API.",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6.10',
    install_requires=requirements
)
