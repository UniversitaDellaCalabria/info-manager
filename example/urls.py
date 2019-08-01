...

import info_manager.urls
urlpatterns += path('', include(info_manager.urls, namespace='info_manager')),
