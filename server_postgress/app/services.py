import sqlalchemy
from app.database import engine


def sql_query(query) -> str:
    """Return sql query."""
    return (
        query.statement
        if isinstance(query, sqlalchemy.orm.Query)
        else query
    ).compile(engine, compile_kwargs={"literal_binds": True}).string
