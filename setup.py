import setuptools

setuptools.setup(
	name = 'Data Preprocess', #this should be unique
	include_package_data=True,
	version = '0.1.0',
	author = 'Avinash Gunda',
	author_email = 'avinash.gunda1994@gmail.com',
	description = 'This is preprocessing package',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)
