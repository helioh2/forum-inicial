export FLASK_APP=index
export FLASK_ENV=development
flask db migrate
flask db upgrade