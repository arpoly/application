# Hosts
VK_HOST = "https://api.vk.com"
GET_TOKEN_URL = "https://oauth.vk.com/authorize"
REDIRECT_URL = "http://localhost/vk-auth"

# Endpoints:
DELETE_LIKES = "/method/likes.delete"
GETLIST_LIKES = "/method/likes.getList"
ISLIKED_LIKES = "/method/likes.isLiked"

# Media Data
MEDIA_TYPES = ["post", "comment", "video", "photo"]
ITEM_ID = ["179172", "179231", "456239036", "456272322"]
POST = MEDIA_TYPES[0]
COMMENT = MEDIA_TYPES[1]
VIDEO = MEDIA_TYPES[2]
PHOTO = MEDIA_TYPES[3]
POST_IDS = ["179866"]
COMMENT_IDS = ["179878"]
VIDEO_IDS = ["456239036"]
PHOTO_IDS = ["456272322"]
ADD_LIKES = "/method/likes.add"
