from django.db import models

# Create your models here.

class Puzzle(models.Model):
    """A published crossword puzzle."""
    title = models.CharField(max_length=250, blank=True)
    date = models.DateField()
    byline = models.CharField(max_length=250)
    publisher = models.CharField(max_length=12)

    def __str__(self):
        """String representation for factory_boy tests"""
        return f"Title: {self.title}; Date: {self.date}; Byline: {self.byline}; Publisher: {self.publisher}"

class Entry(models.Model):
    """An entry with text."""
    entry_text=models.CharField(max_length=50, unique=True)

    def __str__(self):
        """String representation for factory_boy tests"""
        return f"Entry Text: {self.entry_text}"

class Clue(models.Model):
    """A clue."""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    clue_text = models.TextField(max_length=512)
    theme = models.BooleanField(default=False)

    def __str__(self):
        """String representation for factory_boy tests"""
        return f"Entry: {str(self.entry)}; Puzzle: {str(self.puzzle)}; Clue Text: {self.clue_text}"
