from django.shortcuts import render,redirect
# Create your views here.
from note.form import NoteForm
from note.models import Note
# Create your views here.

def note(request):
    """
    This method is used to create new note instance and view all the instances
    """
    # create instance for the form
    form = NoteForm()
    if request.method=="POST":
        form = NoteForm(request.POST)
        # save the modal instance if the form is valid
        if form.is_valid():
            form.save()
      # clearing the form data by redirecting to the same view  
            return redirect(note)           
    # get all note objects
    notes = Note.objects.all()
    return render(request,"form.html",{"form":form,"notes":notes})
  
  
def update_note(request,id):
    """
    This method is used to update the note instances
    """
    # get the instance
    instance = Note.objects.get(id=id)
    # initialise form instance with the note instance
    form = NoteForm(instance=instance)
    if request.method=="POST":
        form = NoteForm(request.POST,instance=instance)
        # save the modal instance if the form is valid
        if form.is_valid():
            form.save()
            # redirect to the note method or '/' path if the form is valid
            return redirect(note)
    return render(request,"form.html",{"form":form})
   

def delete_note(request,id):
    """
    This method is used to delete note instance
    """
    Note.objects.get(id=id).delete()
    return redirect(note)