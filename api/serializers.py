from rest_framework import serializers

from .models import Assignment, Question, User, Choice


class StringSerializer(serializers.StringRelatedField):
  def to_internal_value(self, value):
    return value

class AssignmentSerializer(serializers.ModelSerializer):
  questions = serializers.SerializerMethodField()
  teacher   = StringSerializer(many=False)

  class Meta:
    model = Assignment
    fields = ('__all__')

  def get_questions(self,obj):
    questions = QuestionSerializer(obj.questions.all(),many=True).data
    return questions

  def create(self, request):
    data = request.data
    assignment = Assignment()
    teacher = User.objects.get(email = data['teacher'])
    assignment.teacher = teacher
    assignment.title = data['title']
    assignment.save()
    order = 0
    for question in data['questions']:
      newQ = Question()
      newQ.question = question['title']
      newQ.order = order
      newQ.save()

      for c in question['choices']:
          newC = Choice()
          newC.title = c
          newC.save()
          newQ.choices.add(newC)

      newQ.answer = Choice.objects.get(title=question['answer'])
      newQ.assignment = assignment
      newQ.save()
      order += 1
    return assignment

class QuestionSerializer(serializers.ModelSerializer):
  choices = StringSerializer(many=True)
  class Meta:
    model = Question
    fields = ('id', 'choices', 'title', 'order')

