import sqlalchemy.ext.declarative as dec
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Constraint naming to avoid downgrade issues
meta = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

SqlAlchemyBase = dec.declarative_base(metadata=meta)

#local: postgresql://donovan:@localhost:5432/dev
#remote: postgresql://postgres:Phenomenon7@webappdb.cz3nb50vl311.us-east-1.rds.amazonaws.com:5432/webapp
Engine = create_engine('postgresql://postgres:Phenomenon7@database-1.cz3nb50vl311.us-east-1.rds.amazonaws.com:5432/', pool_size=1000, max_overflow=0)

Session = sessionmaker(bind=Engine)
