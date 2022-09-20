VENV := .venv

CI_BRANCH := $(shell git branch | grep \* | cut -d ' ' -f2)
CI_COMMIT_ID := $(shell git rev-parse HEAD)

clean_venv:
	source deactivate || true
	rm -rf $(VENV)

requirements.txt: requirements.in
	test -r $(VENV) || make $(VENV)
	source $(VENV)/bin/activate \
	&& pip-compile --no-emit-index-url --output-file requirements.txt requirements.in

setup:
	test -r $(VENV) || make $(VENV)
	test -f requirements.txt || make requirements.txt
	source $(VENV)/bin/activate && pip install -r requirements.txt

pip_sync: requirements.txt
	source $(VENV)/bin/activate && pip-sync requirements.txt


spec=test
runtest:
	source $(VENV)/bin/activate \
	&& PYTHONDONTWRITEBYTECODE=1 $(VENV)/bin/pytest -vvv '${spec}'
