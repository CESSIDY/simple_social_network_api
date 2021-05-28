API:
* POST: register - account/api/register/ | kwarg = ('username','email', 'password', 'password2', 'first_name', 'last_name')
* POST: login - account/api/login/ | kwarg = ('username','password')

After login(with Token):
* POST: create post - post/api/create/ | kwarg = ('title','body')
* POST: like post - post/api/like/<int:pk>/
* POST: unlike post - post/api/unlike/<int:pk>/
* GET: analytics - analytics/api/likes_count/date_from=<yyyy:date_from>&date_to=<yyyy:date_to>/

