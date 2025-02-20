Dockerfile:
j'ai tenté avec python slim et l'image passe de plus d'un G a 250M environ
J'ai rajouter un no cache dir
UPDATE: en écrivant les manifest kubernetes j'ai réalisé qu'on pouvait mettre l'URL de la db dans le programme en ENV car les valeurs db user d
**ne pas oublié de modifié avec les variable environnement**
code: config/db.py
    from sqlalchemy import create_engine, MetaData
    import os

    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:password@db:5432/storedb")
    engine = create_engine(DATABASE_URL)

    meta = MetaData()

    conn = engine.connect()

