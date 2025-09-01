# CRUD_tasks

## Установка
```bash
git clone https://github.com/Diglander/CRUD_tasks.git
cd CRUD_tasks
pip install -r requirements.txt
uvicorn app:app --reload
```

## Docker
```bash
docker build -t crud_tasks .
docker run -p 8000:8000 crud_tasks
```