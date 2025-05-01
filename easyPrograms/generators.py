def generators():

    yield 'generators'
    yield 'testing'
    yield'final gen'
gen = generators()

print(f'this is an {next(gen)}')

for i in gen:
    print(i)
   
