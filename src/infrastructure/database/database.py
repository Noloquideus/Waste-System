from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.config import CONFIG


engine = create_async_engine(CONFIG.DATABASE_URL, pool_size=10, max_overflow=20)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
