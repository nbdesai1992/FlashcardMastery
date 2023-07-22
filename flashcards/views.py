from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Deck, Card, StudySession, GeneratedQuestion

@login_required
def dashboard(request):
    decks = Deck.objects.filter(user=request.user)
    return render(request, 'flashcards/dashboard.html', {'decks': decks})

@login_required
def view_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    cards = Card.objects.filter(deck=deck)
    return render(request, 'flashcards/deck.html', {'deck': deck, 'cards': cards})

@login_required
def study_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    # Add your spaced repetition algorithm logic here to fetch the next card to study
    current_card = None  # Placeholder, get the next card based on the algorithm

    return render(request, 'flashcards/studysession.html', {'deck': deck, 'current_card': current_card})

@login_required
def add_card(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)

    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        Card.objects.create(question=question, answer=answer, deck=deck)

        return redirect('view-deck', deck_id=deck_id)

    return render(request, 'flashcards/addcard.html', {'deck': deck})

@login_required
def view_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, deck__user=request.user)
    return render(request, 'flashcards/card.html', {'card': card})

@login_required
def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, deck__user=request.user)

    if request.method == 'POST':
        card.question = request.POST['question']
        card.answer = request.POST['answer']
        card.save()

        return redirect('view-card', card_id=card_id)

    return render(request, 'flashcards/editcard.html', {'card': card})

@login_required
def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, deck__user=request.user)

    if request.method == 'POST':
        card.delete()
        return redirect('view-deck', deck_id=card.deck.id)

    return render(request, 'flashcards/deletecard.html', {'card': card})

# Add more views and functionalities as needed
