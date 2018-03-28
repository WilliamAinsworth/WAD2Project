from pubway.models import User,UserProfile

def create_user():
    # Create a user
    user = User.objects.get_or_create(username="testuser", password="test",first_name="Test", last_name="User", email="testuser@testuser.com")[0]
    user.set_password(user.password)
    user.save()

    # Create a user profile
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.save()

    return user, user_profile