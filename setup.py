from setuptools import setup, find_packages

setup(
    name='datapush',
    version='1.0.1',
    packages=find_packages(),
    install_requires=["pymysql"],
    description='MySQL Data Generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hajun Lee',
    author_email='wklee610@gmail.com',
    url='https://github.com/wklee610/datapush',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)