use zhihu_daily_report;
/*
1、	除了django_session和django_migrations 这2个表，分别对其他的表都实现 insert 操作，每个操作都是一个接口
2、	根据用户id，查询所有发表过的文章
3、	根据用户id，查询所有发表过的评论和评论对应的文章信息（文章信息包括标题，内容）
4、	根据用户id，查询所有收藏夹中的文章信息
5、	根据用户id，查询所有拥有的权限名
PS：权限有2种关系获取，都要获取到
6、	根据 话题 id，查询所有文章信息
7、	根据评论 id，查询对应的文章信息和评论用户的信息

*/
#2、根据用户id，查询所有发表过的文章
select daily_article.title from auth_user, daily_article where 
auth_user.id=daily_article.user_id and auth_user.id=2;
#3、根据用户id，查询所有发表过的评论和评论对应的文章信息（文章信息包括标题，内容）
select comments.content, daily_article.title, daily_article.content from auth_user, comments, daily_article where 
auth_user.id=comments.user_id and comments.article_id=daily_article.id and auth_user.id=5;
#4、根据用户id，查询所有收藏夹中的文章信息
select daily_article.title, daily_article.content from auth_user, collections, collections_articles,
daily_article
where auth_user.id=collections.user_id and collections.id=collections_articles.collection_id 
and collections_articles.article_id=daily_article.id and auth_user.id=4;
#6、根据话题id，查询所有文章信息
select daily_article.title, daily_article.content from daily_article, tags 
where daily_article.tags_id=tags.id and tags.id=4;
#7、根据评论 id，查询对应的文章信息和评论用户的信息
select daily_article.title, daily_article.content, auth_user.* from comments, daily_article, auth_user
where comments.article_id=daily_article.id and comments.user_id=auth_user.id and comments.id=3;
     

