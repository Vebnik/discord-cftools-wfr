

def valid_token(func):
  def inner(*args, **kwargs):
    cf_tools_instance = args[0]
    return func(*args, **kwargs)
  return inner