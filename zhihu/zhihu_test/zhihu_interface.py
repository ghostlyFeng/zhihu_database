#!/usr/bin/env python
# -*- coding: utf-8 -*-
import contextlib

import pymysql

from zhihu_test.zhihu_config import spe_config
from zhihu_test.zhihu_const import INSERT_INTO_TABLES

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def _mysql():

    conn = pymysql.connect(**spe_config)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

def _query(sql, args):
    with _mysql() as cursor:
        row_count = cursor.execute(sql, args)
        return row_count

def _query_result(sql, args):
    with _mysql() as cursor:
        cursor.execute(sql, args)
        return cursor.fetchall()

def _query_many(sql, args):
    with _mysql() as cursor:
        row_count = cursor.executemany(sql, args)
        return row_count

def insertInto_auth_group(*args):
    """
        向auth_group表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['auth_group'], args)

def insertInto_auth_group_permissions(*args):
    """
        向auth_group_permissions表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['auth_group_permissions'], args)

def insertInto_content_type_id(*args):
    """
        向content_type_id表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['content_type_id'], args)

def insertInto_auth_user(*args):
    """
        向auth_user表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['auth_user'], args)

def insertInto_auth_user_groups(*args):
    """
        向auth_user_groups表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['auth_user_groups'], args)

def insertInto_auth_user_user_permissions(*args):
    """
        向auth_user_user_permissions表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['auth_user_user_permissions'], args)

def insertInto_collections(*args):
    """
        向collections表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['collections'], args)

def insertInto_collections_articles(*args):
    """
        向collections_articles表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['collections_articles'], args)

def insertInto_comments(*args):
    """
        向comments表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['comments'], args)

def insertInto_daily_article(*args):
    """
        向daily_article表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['daily_article'], args)

def insertInto_django_admin_log(*args):
    """
        向django_admin_log表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['django_admin_log'], args)

def insertInto_django_content_type(*args):
    """
        向django_content_type表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['django_content_type'], args)

def insertInto_django_migrations(*args):
    """
        向django_migrations表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['django_migrations'], args)

def insertInto_django_session(*args):
    """
        向django_session表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['django_session'], args)

def insertInto_tags(*args):
    """
        向tags表插入信息
    :param args:  插入的记录元组
    :return:  插入成功的条数
    """

    return _query(INSERT_INTO_TABLES['tags'], args)

import time
if __name__ == '__main__':

    # insertInto_auth_user('123', f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 1, 'hf', 'f', 'h',
    #                               'hf@123.com', 1, 1, '2018-05-04')
    # insertInto_auth_user('123', f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 0, '张三', '三', '张',
    #                               'zhangsan@123.com', 0, 1, '2018-05-06')
    # insertInto_auth_user('123', f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 0, '李四', '四', '李',
    #                               'lisi@123.com', 0, 1, '2018-05-06')
    # insertInto_auth_user('123', f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 0, '王五', '五', '王',
    #                               'wangwu@123.com', 0, 1, '2018-05-06')
    # insertInto_auth_user('123', f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 0, '赵六', '六', '赵',
    #                               '赵六@123.com', 0, 1, '2018-05-06')
    # insertInto_tags('2018-05-04','法学')
    # insertInto_tags('2018-05-04', '经济学')
    # insertInto_tags('2018-05-04', '心理学')
    # insertInto_tags('2018-05-04', '历史学')
    # insertInto_tags('2018-05-04', '工学')
    # insertInto_daily_article('2018-05-06', '张三的第一篇历史学文章', '张三的第一篇历史学文章的内容', '张三的第一篇历史学文章的图片',
    #                                  f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 4, 2)
    # insertInto_daily_article('2018-05-06', '李四的第一篇经济学文章', '李四的第一篇经济学文章的内容', '李四的第一篇经济学文章的图片',
    #                                  f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 2, 3)
    # insertInto_daily_article('2018-05-06', '王五的第一篇法学文章', '王五的第一篇法学文章的内容', '王五的第一篇法学文章的图片',
    #                                  f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 1, 4)
    # insertInto_daily_article('2018-05-06', '张三的第一篇工学文章', '张三的第一篇工学文章的内容', '张三的第一篇工学文章的图片',
    #                                  f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 5, 2)
    # insertInto_daily_article('2018-05-06', '张三的第二篇历史学文章', '张三的第二篇历史学文章的内容', '张三的第二篇历史学文章的图片',
    #                                  f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", 4, 2)
    # insertInto_comments(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}",
    #                               '赵六对张三的第一篇历史学文章的评论', 4, 5)
    # insertInto_comments(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}",
    #                               '赵六对李四的第一篇经济学文章的评论', 2, 5)
    # insertInto_comments(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}",
    #                               '张三对王五的第一篇法学文章的评论', 1, 2)
    # insertInto_comments(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}",
    #                               '李四对张三的第二篇历史学文章的评论', 4, 3)
    # insertInto_comments(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}",
    #                               '王五对李四的第一篇经济学文章的评论', 2, 4)
    # insertInto_collections(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", '张三的收藏夹', 2)
    # insertInto_collections(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", '李四的收藏夹', 3)
    # insertInto_collections(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", '王五的收藏夹', 4)
    # insertInto_collections(f"{time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))}", '赵六的收藏夹', 5)
    # insertInto_collections_articles(1, 2)
    # insertInto_collections_articles(1, 3)
    # insertInto_collections_articles(2, 1)
    # insertInto_collections_articles(2, 3)
    # insertInto_collections_articles(2, 4)
    # insertInto_collections_articles(3, 1)
    # insertInto_collections_articles(3, 2)
    # insertInto_collections_articles(3, 4)
    # insertInto_collections_articles(3, 5)
    # insertInto_collections_articles(4, 1)
    # insertInto_collections_articles(4, 2)
    # insertInto_collections_articles(4, 3)
