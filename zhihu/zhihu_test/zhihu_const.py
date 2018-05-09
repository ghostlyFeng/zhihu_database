#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'


INSERT_INTO_AUTH_GROUP = 'insert into auth_group(name) values(%s)'
INSERT_INTO_AUTH_GROUP_PERMISSIONS = 'insert into auth_group_permissions(group_id, permission_id) values(%s,%s)'
INSERT_INTO_AUTH_PERMISSION = 'insert into auth_permission(name, content_type_id,codename) values(%s,%s,%s)'
INSERT_INTO_AUTH_USER = '''insert into auth_user(password, last_login, is_superuser, username, first_name,
                                                                      last_name, email, is_staff, is_active, date_joined) values(%s,%s,%s,%s,                                                                        %s,%s,%s,%s,%s,%s)'''
INSERT_INTO_AUTH_USER_GROUPS = 'insert into auth_user_groups(user_id, group_id) values(%s,%s)'
INSERT_INTO_AUTH_USER_USER_PERMISSIONS = 'insert into auth_user_user_permissions(user_id, permission_id) values(%s,%s)'
INSERT_INTO_COLLECTIONS = 'insert into collections(created, name, user_id) values(%s,%s,%s)'
INSERT_INTO_COLLECTIONS_ARTICLES = 'insert into collections_articles(collection_id, article_id) values(%s,%s)'
INSERT_INTO_COMMENTS = 'insert into comments(created, content, article_id, user_id) values(%s,%s,%s,%s)'
INSERT_INTO_DAILY_ARTICLE = 'insert into daily_article(created, title, content, image ,updated, tags_id, user_id) values(%s,%s,%s,%s,%s,%s,%s)'
INSERT_INTO_DJANGO_ADMIN_LOG = 'insert into django_admin_log(action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) values(%s,%s,%s,%s,%s,%s,%s)'
INSERT_INTO_DJANGO_CONTENT_TYPE = 'insert into django_content_type(app_label, model) values(%s,%s)'
INSERT_INTO_DJANGO_MIGRATIONS = 'insert into django_migrations(app, name, applied) values(%s,%s,%s)'
INSERT_INTO_DJANGO_SESSION = 'insert into django_session(session_key, session_data, expire_date) values(%s,%s,%s)'
INSERT_INTO_TAGS = 'insert into tags(created, tag) values(%s,%s)'


INSERT_INTO_TABLES = {
    'auth_group': INSERT_INTO_AUTH_GROUP,
    'auth_group_permissions': INSERT_INTO_AUTH_GROUP_PERMISSIONS,
    'auth_permission': INSERT_INTO_AUTH_PERMISSION,
    'auth_user': INSERT_INTO_AUTH_USER,
    'auth_user_groups': INSERT_INTO_AUTH_USER_GROUPS,
    'auth_user_user_permissions': INSERT_INTO_AUTH_USER_USER_PERMISSIONS,
    'collections': INSERT_INTO_COLLECTIONS,
    'collections_articles': INSERT_INTO_COLLECTIONS_ARTICLES,
    'comments': INSERT_INTO_COMMENTS,
    'daily_article': INSERT_INTO_DAILY_ARTICLE,
    'django_admin_log': INSERT_INTO_DJANGO_ADMIN_LOG,
    'django_content_type': INSERT_INTO_DJANGO_CONTENT_TYPE,
    'django_migrations': INSERT_INTO_DJANGO_MIGRATIONS,
    'django_session': INSERT_INTO_DJANGO_SESSION,
    'tags': INSERT_INTO_TAGS,
}



DELETE_FROM_PUSER_SQL = 'delete from  puser where username=%s'
UPDATE_PUSER_PASSWORD_SQL = 'update puser set pwd=%s where username=%s'
SELECT_PUSER_SQL = 'select puser.username, puser.pwd from puser where username=%s'

INSERT_INTO_STUDENT_SQL = 'insert into student(name, age, password) values(%s, %s, %s)'
DELETE_FROM_STUDENT_SQL = 'delete from student where name=%s'

SELECT_EMP_AND_DEPT_SQL = 'select e.*, d.dname from emp as e , dept as d where e.deptno=d.deptno and e.deptno=%s'


DELTE_TABLE_BY_ID = 'delete from %s where id=%s'



DELETE_FROM_TABLES_SQL = {
    'puser': DELETE_FROM_PUSER_SQL,
    'student': DELETE_FROM_STUDENT_SQL,
}

UPDATE_TABLES_SQL = {
    'puser': UPDATE_PUSER_PASSWORD_SQL,
}

SELECT_TABLES_SQL = {
    'puser': SELECT_PUSER_SQL,
}

