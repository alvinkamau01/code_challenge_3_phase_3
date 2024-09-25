from __future__ import with_statement
import os
from alembic import context
from sqlalchemy import engine_from_config, pool
from models.concert import Base  # Import Base from your models
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

# This is the Alembic Config object, which provides access to
# the values within the .ini file in use.
config = context.config

# This is the target metadata for 'autogenerate' support
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# This is the entry point for Alembic's migration operations.
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
