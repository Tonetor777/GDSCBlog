import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment

def post():
    post1 = Post.objects.create(title='First Post', content='In the world of technology....', catagory='Tech', tags=['tech', 'technology'])
    post2 = Post.objects.create(title='Second Post', content='Science in the current......', catagory='Science', tags=['science', 'biology', 'life'])
    post3 = Post.objects.create(title='Third Post', content='The new WHO research shows..........', catagory='Food', tags=['food', 'nutrition', 'who'])

    posts_in_Tech = Post.objects.filter(catagory='Tech')
    print("Technology:")
    for post in posts_in_Tech:
        print(f"{post.title} - {post.content}")


    # Updating
    post_to_update = Post.objects.get(title='Third Post')
    post_to_update.content = 'Nutrition'
    post_to_update.save()

    # Deleting
    post_to_delete = Post.objects.get(title='Second Post')
    post_to_delete.delete()

def comment():
    post1 = Post.objects.get(id = 1)
    comment1, created1 = Comment.objects.get_or_create(post=post1, content='Nice!!', author='blogger', publishedDate=timezone.now())

    post3 = Post.objects.get(id = 3)
    comment3, created3 = Comment.objects.get_or_create(post=post3, content='Interesting!', author='sunny', publishedDate=timezone.now())

    # Display comments
    comments_for_post1 = Comment.objects.filter(post__title='First Post')
    print("Comments for First Post:")
    for comment in comments_for_post1:
        print(f"{comment.content}")

    # Update the content of one of the comments
    comment_to_update = Comment.objects.get(author='blogger')
    comment_to_update.content = 'Updated Comment for First Post'
    comment_to_update.save()

    # Delete a comment
    comment_to_delete = Comment.objects.get(author='sunny')
    comment_to_delete.delete()

if __name__ == "__main__":
    # Call the ORM operations functions
    post()
    comment()
