from setuptools import setup

setup(
    name='volly',
    version='0.1.1',
    description='A Python client for volatile.wtf',
    long_description='''volatile.wtf is a public service for storing arbitrary key-value pairs. Documentation at https://volatile.wtf

This code allows the storage to be used quickly and easily from Python code.''',  # noqa: E501
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
