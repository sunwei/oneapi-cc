# coding: utf-8

from flask import url_for
from oneapi.exceptions import USER_NOT_FOUND


def _register_user(testapp, **kwargs):
    return testapp.post_json(url_for('user.register_user'), {
          "user": {
              "email": 'foo@bar.com',
              "username": 'foobar',
              "password": 'myprecious'
          }}, **kwargs)


class TestProfile:

    def test_get_profile_not_existing(self, testapp):
        resp = testapp.get(url_for('profiles.get_profile', username='foobar'), expect_errors=True)
        assert resp.status_int == 404
        assert resp.json == USER_NOT_FOUND['message']

