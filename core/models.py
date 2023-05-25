from django.db import models

class TextCorrection(models.Model):
    original_txt = models.TextField()
    corrected_txt = models.TextField()

    # def __str__(self):
    #     return f'Original: {self.original_txt}\nCorrected: {self.corrected_txt}'
