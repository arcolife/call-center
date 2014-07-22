from functools import wraps

from flask import g, flash, redirect, url_for, request, session

def requires_login(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if g.user is None:
      flash(u'You need to be signed in for this page.')
      return redirect(url_for('users.login', next=request.path))
    return f(*args, **kwargs)
  return decorated_function

def logout_user():
    '''
    Logs a user out. (You do not need to pass the actual user.) This will
    also clean up the remember me cookie if it exists.
    '''
    if 'user_id' in session:
        print "Logged out: %s" % (session.pop('user_id'))
    return True
