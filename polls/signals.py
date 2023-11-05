from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Poll

@receiver(post_save, sender=Poll)
def poll_created(sender, instance, **kwargs):
    """
    Signal handler function called when a new Poll object is created.
    You can add your custom logic here.
    """
    # Example: Print a message when a new poll is created
    print(f"New poll created: {instance.question}")
    
    # Add your custom logic here (e.g., send notifications, perform additional actions)

# You can define more signals and handlers as needed for your app
