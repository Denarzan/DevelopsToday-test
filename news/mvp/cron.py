from api.models import Post


def cronjob():
    """
    Function to delete all votes every day at midnight.
    :return: posts without votes.
    """
    Post.objects.filter(amount_of_upvotes__gt=0).update(amount_of_upvotes=0)
