#  note/forms.py
from note.models import Note
from django import forms as form
class NoteForm(form.ModelForm):
    class Meta:
        fields = "__all__"
        model = Note

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
       
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": "3",
            }
        )