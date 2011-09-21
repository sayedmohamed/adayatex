# in signals.py:
 
def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a matching profile."""
 
    from profiles.models import UserProfile
 
    if created:
        UserProfile(user = instance).save()
        # Do additional stuff here if needed, e.g.
        # create other required related records