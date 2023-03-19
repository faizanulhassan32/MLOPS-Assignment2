install: 
	@echo "Installing requirements"
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black app.py

lint:
	pylint --fail-under=-1 app.py

codestyle:
	pycodestyle --show-source --show-pep8 app.py

execute:
	@echo "Starting the web application"
	python app.py
