from django.db import models


class Sleep(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        start_time = self.start.strftime('%H:%M')  # Format as hours:minutes
        end_time = self.end.strftime('%H:%M')      # Format as hours:minutes
        return f"Sleep record from {start_time} to {end_time}"
