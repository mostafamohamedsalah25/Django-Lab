from django import forms
from .models import Trainee


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-700 bg-gray-900 px-4 py-3 text-sm text-gray-100 placeholder-gray-500 shadow-sm transition focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/30',
                'placeholder': 'Enter first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-700 bg-gray-900 px-4 py-3 text-sm text-gray-100 placeholder-gray-500 shadow-sm transition focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/30',
                'placeholder': 'Enter last name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-xl border border-gray-700 bg-gray-900 px-4 py-3 text-sm text-gray-100 placeholder-gray-500 shadow-sm transition focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/30',
                'placeholder': 'name@example.com',
            }),
            'track': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-700 bg-gray-900 px-4 py-3 text-sm text-gray-100 placeholder-gray-500 shadow-sm transition focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/30',
                'placeholder': 'Open Source',
            }),
            'branch': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-700 bg-gray-900 px-4 py-3 text-sm text-gray-100 placeholder-gray-500 shadow-sm transition focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/30',
                'placeholder': 'Assiut',
            }),
            'course': forms.Select(attrs={
                'class': 'w-full rounded-xl border border-gray-700 bg-gray-900 px-4 py-3 text-sm text-gray-100 shadow-sm transition focus:border-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500/30',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full rounded-xl border border-dashed border-gray-600 bg-gray-900 px-4 py-3 text-sm text-gray-300 file:mr-4 file:rounded-lg file:border-0 file:bg-cyan-500 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-gray-950 hover:file:bg-cyan-400',
            }),
        }
