from setuptools import setup

setup(name="changathi", 
    version="0.0.1",
    description="changathi first version",
    py_modules = ["changathi"],
    author="Doodle.ai",
    packages=['src'],
    author_email='contact.doodleai@gmail.com',    
    install_requires=["gensim==3.8.3",
        "SciPy==1.5.1",
        "scikit-learn==0.23.1",
        "pandas==1.0.5",
        "matplotlib==3.1.1",
        "nltk==3.5",
        "pyemd==0.5.1",
        "plac==0.9.6",
        "spacy==2.2.1",
        "beautifulsoup4==4.8.0",
        "Django==3.1.1",
        "django-cors-headers==3.5.0",
        "schedule==0.6.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE Version 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Abhijithm2447/changathi"
    )
