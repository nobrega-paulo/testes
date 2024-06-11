run:
	@uvicorn env_api.main:app --reload 

create-migrations:
	@PYTHONPATH=$PYTHONPATH{$(pwd) alembic revision --autogenerate -m $("initi_db")}

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head