coverage:
	pytest --cov=pyretem

test:
	pytest --cov=pyretem 


doc:
	cd docs && make html

wheel:
	rm -rf build
	rm -rf dist
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

clean:
	rm -rf docs/_build
	rm -rf docs/source/api/_generated