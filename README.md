API:
* POST: register - account/api/register/ | kwargs = ('username','email', 'password', 'password2', 'first_name', 'last_name')
* POST: login - account/api/login/ | kwargs = ('username','password')

After login(with Token):
* POST: create post - post/api/create/ | kwargs = ('title','body')
* POST: like post - post/api/like/\<int:pk\>/
* POST: unlike post - post/api/unlike/\<int:pk\>/
* GET: analytics - analytics/api/likes_count/date_from=%Y-%m-%d&date_to=%Y-%m-%d/

