# Makefile

PROJECT_NAME=FlashcardMastery
VENV_NAME=$(PROJECT_NAME)_venv
PYTHON=$(VENV_NAME)/bin/python

# Default target executed when no arguments are given to make.
default: venv

# Sets up a virtual environment for Python
venv:
	test -d $(VENV_NAME) || virtualenv $(VENV_NAME)
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements.txt

# Echo the command to activate the virtual environment
activate:
	@echo "To activate the virtual environment, run:"
	@echo "source $(VENV_NAME)/bin/activate"

# Run the Django development server
run:
	$(PYTHON) manage.py runserver

# Migrate the database
migrate:
	$(PYTHON) manage.py migrate

# Create migrations based on model changes
makemigrations:
	$(PYTHON) manage.py makemigrations

# Collect static files into the staticfiles directory
collectstatic:
	$(PYTHON) manage.py collectstatic

# Create a superuser for the Django Admin
createsuperuser:
	$(PYTHON) manage.py createsuperuser

# Delete the virtual environment
clean:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Virtual environment is not active. Proceeding with deletion..."; \
		rm -rf $(VENV_NAME); \
	else \
		echo "Virtual environment is currently active. Deactivate it before proceeding."; \
	fi

.PHONY: venv activate run migrate makemigrations collectstatic createsuperuser clean
