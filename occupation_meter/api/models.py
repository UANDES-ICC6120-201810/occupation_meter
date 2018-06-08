from django.db import models

class CountRequest(models.Model):
    """This class represents the count request model."""
    source_endpoint = models.CharField(max_length=512, blank=False)
    source_bucket = models.CharField(max_length=255, blank=True)
    source_folder = models.CharField(max_length=255, blank=False)
    source_filename = models.CharField(max_length=255, blank=False)
    count = models.PositiveIntegerField(blank=True, null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{endpoint}/{bucket}/{filename}".format(endpoint=self.source_endpoint,
                                                       bucket=self.source_bucket,
                                                       filename=self.source_filename)

    def get_endpoint(self):
        """Return the andpoint for the image to be processed"""
        return "{endpoint}/{bucket}/{folder}/{filename}".format(endpoint=self.source_endpoint,
                                                               bucket=self.source_bucket,
                                                               folder=self.source_folder,
                                                               filename=self.source_filename)
