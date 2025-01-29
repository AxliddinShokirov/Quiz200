from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Choice, Submission
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


@api_view(['POST'])
def submit_test(request):
    user = request.user  
    answers = request.data.get('answers')  

    if not answers:
        return Response({"error": "No answers provided"}, status=status.HTTP_400_BAD_REQUEST)

    total_questions = len(answers)
    correct_answers = 0

    for answer in answers:
        question = get_object_or_404(Question, id=answer['question_id'])
        choice = get_object_or_404(Choice, id=answer['choice_id'])

        
        Submission.objects.create(user=user, question=question, choice=choice)

        if choice.is_correct:
            correct_answers += 1

    
    score = (correct_answers / total_questions) * 100

    return Response({
        "score": score,
        "correct_answers": correct_answers,
        "total_questions": total_questions
    }, status=status.HTTP_200_OK)
