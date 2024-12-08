from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

trigger_sql = """
CREATE OR REPLACE FUNCTION update_product_rating() RETURNS TRIGGER AS $$
BEGIN
    -- Пересчитываем средний рейтинг товара
    UPDATE clothing_models
    SET average_rating = (
        SELECT AVG(rate) FROM reviews WHERE cloth_name = NEW.cloth_name
    )
    WHERE name = NEW.cloth_name;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_rating_trigger
AFTER INSERT ON reviews
FOR EACH ROW
EXECUTE FUNCTION update_product_rating();

CREATE OR REPLACE FUNCTION update_order_date() RETURNS TRIGGER AS $$
BEGIN
    -- Обновляем поле update_date на текущее время, если меняется статус
    IF NEW.status <> OLD.status THEN
        NEW.update_date = NOW();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_order_date_trigger
BEFORE UPDATE ON orders
FOR EACH ROW
EXECUTE FUNCTION update_order_date();
"""


engine = create_engine(url=f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# with engine.connect() as connection:
#     connection.execute(connection.execute(text(trigger_sql)))

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()