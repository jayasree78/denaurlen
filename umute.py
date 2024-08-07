def unmute_post(user_id, post_id):
    if is_post_muted(user_id, post_id):
        update_user_post_settings(user_id, post_id, False)
        return "Post unmuted successfully."
    else:
        return "Post is not muted."

