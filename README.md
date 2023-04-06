# API

Example of integrating API Gateway + Starlite using PDM for dependency management and AWS SAM for deployment.

## Project structure

See the AWS SAM `template.yaml` to apply your customizations.

### `dependencies`

Contains production `requirements.txt` automatically exported from `pdm.lock`. Will be deployed to a lambda layer.

### `library`

Contains shared code beetwen lambdas. It'll be available to all your lambda code locally too after running `pdm install`. Also deployed as a lambda layer.

### `src`

The lambdas code, one folder per lambda. Inspect the teams lambda for the boilerplate required.

### `src/main.py`

Entrypoint to locally execute the Starlite app. A PDM script is available `pdm run dev` or `pdm dev`. You should add the per-lambda subroutes to this file.

## How to use

1. Clone this repo.
2. Run `pdm config venv.use_pip True` to include `pip` in your virtual environment. This is needed by AWS SAM.
3. Run `pdm install`.
4. Run locally with `pdm run dev`.

### Deploy

Run `sam build` and `sam deploy` and follow instructions.
