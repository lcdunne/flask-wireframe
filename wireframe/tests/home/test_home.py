import pytest

try:
    from flask import _app_ctx_stack as ctx_stack
except ImportError:
    from flask import _request_ctx_stack as ctx_stack

class TestCase:
    # set a Flask app config value using a pytest mark
    @pytest.mark.options(VERIFY_IDENTITY=True)
    def test_foo(self, client, session):
        # set user identity in app context
        ctx_stack.top.claims = {'sub': 'user1', 'tid': 'expected-audience'}

        # mock a class
        mocked_batch_client = mocker.patch('backend_class.BackendClient')
        assert(mocked_batch_client.return_value.list.return_value = ['a', 'b'])

        # test a view - it uses BackendClient (mocked now)
        resp = client.get('/api/items')
        data = json.loads(resp.data)
        assert(len(data['results']) > 0)

        # insert data into the database - will get rolled back after test completion
        item = YourModel()
        item.foo = "bar"
        session.add(item)
        session.commit()
