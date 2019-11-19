# Volly - a Python client for volatile.wtf

volatile.wtf is a public service for storing arbitrary key-value pairs. Documentation at https://volatile.wtf

This code allows the storage to be used quickly and easily from Python code.

>>> from volly import Service
>>> svc = Service("https://volatile.wtf")
>>> svc.store("H734B2OWTA", "Hello, world!")
>>> svc["H734B2OWTA"]
b'Hello, world!'

You can use a different version of this service if you provide the URL as an argument to Service()