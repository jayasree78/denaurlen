def mute_post(user_id, post_id):
    if not is_post_muted(user_id, post_id):
        update_user_post_settings(user_id, post_id, True)
        return "Post muted successfully."
    else:
        return "Post is already muted."

def is_post_muted(user_id, post_id):
    # Query the database to check if the post is muted
    return database.query(UserPostSettings).filter(user_id=user_id, post_id=post_id).first().is_muted

def update_user_post_settings(user_id, post_id, is_muted):
    # Update the database with the new mute status
    record = database.query(UserPostSettings).filter(user_id=user_id, post_id=post_id).first()
    if record:
        record.is_muted = is_muted
    else:
        new_record = UserPostSettings(user_id=user_id, post_id=post_id, is_muted=is_muted)
        database.add(new_record)
    database.commit()
