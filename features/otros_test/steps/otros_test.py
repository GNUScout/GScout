#--conding# -*- encoding: utf-8 -*-
from behave import *

@given(u'un usuario permitido del dominio')
def step_impl(context):
   from django.contrib.auth.models import User
   u = User(username='foo', email='foo@example.com')
   u.set_password('bar')
   u.save()
   assert True

@then(u'nosotros veremos la página principal.')
def step_impl(context):
    assert False
