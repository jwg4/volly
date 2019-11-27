from setuptools import setup

setup(
    name='volly',
    version='0.1.0',
    description='A Python client for volatile.wtf',
    long_description='Volatile - https://volatilie.wtf is a public service which provides a key-value pair API. This package provides a convenient Python wrapper for that service.',
    url='http://github.com/jwg4/volly',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    license='MIT',
    packages=['volly'],
    zip_safe=False,
    test_suite="tests",
    install_requires=[
        "requests"
    ]
)
