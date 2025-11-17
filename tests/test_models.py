from sqlalchemy import select

from projeto_fastapi.models import User


def test_create_user(session):
    user = User(username='Phzinn', email='ph@ziinn.com', password='slaa')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'ph@ziinn.com'))

    assert result.username == 'Phzinn'
