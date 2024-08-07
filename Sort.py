def calculate_relevance_score(post, user):
    relevance_score = 0
    if post['topic'] in user['interests']:
        relevance_score += 5  # Interest match
    if post['author'] in user['frequent_authors']:
        relevance_score += 3  # Author match
    if post['id'] in user['interacted_posts']:
        relevance_score += 2  # Interaction match
    return relevance_score

'''Step 2: Combine Scores with Recency
We combine the relevance score with a recency score. Recency score is calculated by giving more weight to recent posts.'''

def calculate_combined_score(post, user):
    relevance_score = calculate_relevance_score(post, user)
    recency_score = (10 / (post['timestamp'] + 1))  # Adjust recency weight as needed
    combined_score = relevance_score * 0.7 + recency_score * 0.3  # Example weights
    return combined_score


'''Step 3: Sort Posts
Sort the posts based on the combined score in descending order.'''
def sort_posts(posts, user):
    posts.sort(key=lambda post: calculate_combined_score(post, user), reverse=True)
    return posts
