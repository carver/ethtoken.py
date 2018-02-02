rm build/lib/ethtoken/*
mv dist/*.whl dist/bak/.
python setup.py bdist_wheel
twine upload dist/*.whl
