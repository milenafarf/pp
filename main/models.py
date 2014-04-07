from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=80)


class User(models.Model):
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.IntegerField(default=1)  #type=1 to bedzie uzytkownik zwykly
    ban = models.BooleanField(default=False)
    date_created = models.DateTimeField(
        auto_now_add=True)  #Automatically set the field to now when the object is first created. Useful for creation of timestamps
    last_update = models.DateTimeField(auto_now=True)


class Project(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.CharField(
        max_length=160)  #krotki opis projktu,mozeby byc wyswietlany na st glownej, razem z paskiem postepu itd
    full_description = models.TextField()  #pelny opis projektu
    funding_goal = models.DecimalField(max_digits=8, decimal_places=2)  #ilosc pieniedzy planowanych do zebrania
    money_raised = models.DecimalField(max_digits=8, decimal_places=2)  #ilosc pieniedzy juz zebranych
    deadline = models.DateField(default=datetime.date.today)  #data zakonczenia projektu
    date_created = models.DateTimeField(
        auto_now_add=True)  #Automatically set the field to now when the object is first created. Useful for creation of timestamps
    last_update = models.DateTimeField(
        auto_now=True)  #Automatically set the field to now every time the object is saved. Useful for 'last-modified' timestamps
    rating = models.IntegerField() #ocena projektu
    ban = models.BooleanField(default=False)
    visit_counter = models.IntegerField()
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)


class Perk(models.Model):
    # poziomy wsparcia projektu i przewidziane nagrody za wsparcie taka suma pieniedzy
    amount = models.DecimalField(max_digits=8, decimal_places=2)  #ilosc pieniedzy w danym poziomie
    title = models.CharField(max_length=80)  #tytul, nazwa poziomu
    description = models.TextField()  #opis poziomu
    number_available = models.IntegerField(blank=True)  #blank=True znaczy, ze wartosc moze byc null
    #jesli amount=null, to liczba danej nagrody za wsparcie jest nieograniczona
    project = models.ForeignKey(Project)


class Comment(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)


class Message(models.Model):
    subject = models.TextField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user_from = models.ForeignKey(User, related_name='message_user_from')
    user_to = models.ForeignKey(User, related_name='message_user_to')


class Donation(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    perk = models.ForeignKey(Perk)