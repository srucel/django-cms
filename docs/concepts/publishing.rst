##########
Publishing
##########

Each page in the CMS exists in two versions: public and draft. The staff users
generally use the draft version to edit content and change settings for the
pages. None of these changes are visible on the public site until the page is
published.

When a page is published, the page must also have all parent pages published
in order to become available on the web site. If a parent page is not published
at the moment, the page goes into a "pending" state where it will become
automatically published once the parent page is published. This enables you to
edit an entire subsection of the website and publishing it once all the work is
complete.

**************
Code and Pages
**************

If you need to manipulate pages by code be sure to filter on ``publisher_is_draft=True``.
This will give you only the draft versions of pages and this are the ones you actually see
in the admin and in draft mode in the frontend. There is a publish signal fired
every time a page is published. In this moment a second page is created and all titles,
placeholders and plugins are copied to the public version.
