from app import create_app, User, Post, db

app = create_app()
app.app_context().push()

u1 = User(name='John', email_address='john.doe@gmail.com')
db.session.add(u1)
db.session.commit()

p1 = Post(
    title='some other post',
    body_content='This is the body of the post bla bla bla',
    user_id=u1.id)

db.session.add(p1)
db.session.commit()