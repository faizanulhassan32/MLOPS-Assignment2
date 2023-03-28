install: 
	@echo "Installing requirements"
	# pip install --upgrade pip && 
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --fail-under=-1 train.py
	pylint --fail-under=-1 inference.py


codestyle:
	pycodestyle --show-source --show-pep8 train.py
	pycodestyle --show-source --show-pep8 inference.py

lint:
	pylint --fail-under=-1 app.py

