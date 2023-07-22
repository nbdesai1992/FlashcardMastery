from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('deck/<int:deck_id>/', views.view_deck, name='view-deck'),
    path('deck/<int:deck_id>/study/', views.study_deck, name='study-deck'),
    path('deck/<int:deck_id>/add-card/', views.add_card, name='add-card'),
    path('card/<int:card_id>/', views.view_card, name='view-card'),
    path('card/<int:card_id>/edit/', views.edit_card, name='edit-card'),
    path('card/<int:card_id>/delete/', views.delete_card, name='delete-card'),
    # Add more URL patterns for other views and functionalities as needed
]
