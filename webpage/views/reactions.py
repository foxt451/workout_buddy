from webpage import models
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect

class SayInterested:
    def post(self, request):
        workout_id = request.POST['workout_id']
        how_to_contact = request.POST['how_to_contact']
        
        workout = get_object_or_404('webpage.WorkoutSession', id=workout_id)
        reaction = models.InterestedInWS(user=request.user, workout=workout, how_to_contact=how_to_contact)
        reaction.save()
        return redirect(workout.get_absolute_url())
        