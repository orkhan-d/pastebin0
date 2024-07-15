from pydantic import BaseModel

def sqlalchemy_to_pydantic[T: type[BaseModel]](sqlalchemy_obj, pydantic_model: T) -> T:
    """
    Convert a SQLAlchemy model instance to a Pydantic model instance.
    
    :param sqlalchemy_obj: SQLAlchemy model instance
    :param pydantic_model: Pydantic model class
    :return: Pydantic model instance
    """
    data = {field: getattr(sqlalchemy_obj, field) for field in pydantic_model.model_fields.keys()}
    return pydantic_model(**data)
