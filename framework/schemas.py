ISLIKED = {"response": {"type": "dict", "schema": {"liked": {"type": "integer"}, "copied": {"type": "integer"}}}}

ADDLIKE = {"response": {"type": "dict", "schema": {"likes": {"type": "integer"}}}}

DELETELIKE = {"response": {"type": "dict", "schema": {"likes": {"type": "integer"}}}}

GETLIST = {"response": {"type": "dict", "schema": {"count": {"type": "integer"}, "items": {"type": "list"}}}}
