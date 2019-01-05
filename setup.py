import setuptools


setuptools.setup(
    name="dgconfig",
    version="0.0.1",
    author="Fako Berkers",
    author_email="email@fakoberkers.nl",
    description="A configuration package for Django to store configurations in the database and/or transfer them to for instance Celery",
    long_description="A configuration package for Django to store configurations in the database and/or transfer them to for instance Celery",
    long_description_content_type="text/markdown",
    url="https://github.com/edubadges/dgconfig",
    packages=setuptools.find_packages(),
    install_requires=[
        "Django>=1.11"
    ],
    python_requires="~=2.7",
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ),
)
