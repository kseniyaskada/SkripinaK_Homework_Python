import pytest
from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:1234@localhost:5432/QA"


@pytest.mark.positive_test
def test_insert_user():
    db = create_engine(db_connection_string)

    all_entity = db.execute(text("select * from users")).fetchall()

    sql = text(
        "insert into users (user_email, user_id, subject_id)"
        "VALUES ( :email , :user_id, :subj_id)")

    my_params = {
        'email': 'mariafedotova@yandex.ru',
        'user_id': '82900',
        'subj_id': '3'
    }

    db.execute(sql, my_params)

    after_insert = db.execute(text("select * from users")).fetchall()

    sql_1 = text("delete from users where subject_id = :id")
    db.execute(sql_1, id='3')

    assert len(after_insert) == len(all_entity)+1


@pytest.mark.positive_test
def test_update_user():
    db = create_engine(db_connection_string)

    all_entity = db.execute(text("select * from users")).fetchall()

    sql = text(
        "insert into users (user_email, user_id,"
        "subject_id) VALUES ( :email , :user_id, :subj_id)")

    my_params = {
        'email': 'mariafedotova@yandex.ru',
        'user_id': '82900',
        'subj_id': '3'
    }

    db.execute(sql, my_params)

    sql_1 = text(
        "update users set user_email = :user_email where user_id = :id")
    db.execute(sql_1, user_email="New email", id='82900')

    after_insert = db.execute(text("select * from users")).fetchall()

    sql_1 = text("delete from users where subject_id = :id")
    db.execute(sql_1, id='3')

    final = db.execute(text("select * from users")).fetchall()

    assert after_insert[-1]["user_email"] == "New email"
    assert len(final) == len(all_entity)


@pytest.mark.positive_test
def test_delete_user():
    db = create_engine(db_connection_string)
    all_entity = db.execute(text("select * from users")).fetchall()

    sql = text("insert into users (user_email, user_id, subject_id) VALUES ( :email , :user_id, :subj_id)")

    my_params = {
        'email': 'mariafedotova@yandex.ru',
        'user_id': '82900',
        'subj_id': '3'
    }

    db.execute(sql, my_params)

    sql_1 = text("delete from users where subject_id = :id")
    db.execute(sql_1, id='3')

    final = db.execute(text("select * from users")).fetchall()
    deleted_user = db.execute(text("select * from users where user_id = :id"), id='82900').fetchone()

    assert deleted_user is None
    assert len(final) == len(all_entity)
