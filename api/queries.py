from .models import Post
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
  try:
    post = Post.query.get(id)
    payload = {
      "success": True,
      "post": post.to_dict()
    }
  except AttributeError:  # todo not found
    payload = {
      "success": False,
      "errors": ["Post item matching {id} not found"]
    }
  return payload