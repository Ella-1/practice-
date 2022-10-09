# using similar methid with that of python_marshal.py file
import marshal

script = """
for i in range(10):
    print(i)
"""
code = compile(script, '<script>', 'exec')

with open('exec.marshal', 'wb') as exec_file:
    marshal.dump(code, exec_file)