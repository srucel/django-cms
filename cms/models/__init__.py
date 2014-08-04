# -*- coding: utf-8 -*-
from django.conf import settings as d_settings
from cms.utils.compat import DJANGO_1_6
from cms.utils.compat.dj import is_installed

from .settingmodels import *  # nopyflakes
from .pagemodel import *  # nopyflakes
from .permissionmodels import *  # nopyflakes
from .placeholdermodel import *  # nopyflakes
from .pluginmodel import *  # nopyflakes
from .titlemodels import *  # nopyflakes
from .placeholderpluginmodel import *  # nopyflakes
from .static_placeholder import *  # nopyflakes
from .aliaspluginmodel import *  # nopyflakes
# must be last
from cms import signals as s_import  # nopyflakes


def validate_settings():
    if "django.core.context_processors.request" not in d_settings.TEMPLATE_CONTEXT_PROCESSORS:
        raise ImproperlyConfigured('django-cms needs django.core.context_processors.request in settings.TEMPLATE_CONTEXT_PROCESSORS to work correctly.')
    if not is_installed('mptt'):
        raise ImproperlyConfigured('django-cms needs django-mptt installed.')
    if 'cms.middleware.multilingual.MultilingualURLMiddleware' in d_settings.MIDDLEWARE_CLASSES and 'django.middleware.locale.LocaleMiddleware' in d_settings.MIDDLEWARE_CLASSES:
        raise ImproperlyConfigured('django-cms MultilingualURLMiddleware replaces django.middleware.locale.LocaleMiddleware! Please remove django.middleware.locale.LocaleMiddleware from your MIDDLEWARE_CLASSES settings.')


def validate_dependencies():
    # check for right version of reversions
    if is_installed('reversion'):
        from reversion.admin import VersionAdmin
        if not hasattr(VersionAdmin, 'get_urls'):
            raise ImproperlyConfigured('django-cms requires never version of reversion (VersionAdmin must contain get_urls method)')

if DJANGO_1_6:
    validate_dependencies()
    validate_settings()
