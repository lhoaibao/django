from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Add a avatar field to user """
    avatar = models.ImageField(upload_to='media/avatars/', blank=False)


'------------------Model Comment------------------------'


class Comment(models.Model):
    """
        Comment model

        @author: the user that create the comment.

        @comment_text: text of the comment.

        @create: the created date of comment.

        @update: the last updated date of comment.

        @content_type: movie or actor or award.

        @object_id: the specific primary key of a
                    movie or an actor or an award.

        @selected: the object of movie or actor or award selected by using
                   content_type and object_id.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Generic Foreign Key
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        # Sort comments follow newest create time
        ordering = ['-create']

    def __str__(self):
        return self.comment_text


'---------------------------Model award--------------------------'


class Award(models.Model):
    """
        Award model

        @author: the user that create the award.

        @kind: Movie or Actor that won the award.

        @comments: all the comments related to the award.

        @content_type: movie or actor.

        @object_id: the specific primary key of a movie or an actor.

        @selected: the object of movie or actor selected by using
                   content_type and object_id.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    kind_choices = [
        ('Movie', 'Movie'),
        ('Actor', 'Actor')
    ]

    date = models.DateField(blank=False)
    title = models.CharField(max_length=200, blank=False)
    kind = models.CharField(
        max_length=10,
        choices=kind_choices,
        default='Movie',
        blank=False
    )
    comments = GenericRelation(Comment)
    # Generic Foreign Key
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    selected = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title

    def get_fields(self):
        """ Return all key and value of all the field in award """
        return [(field.name, field.value_to_string(self))
                for field in Award._meta.fields]


'------------------Model Category------------------------'


class Category(models.Model):
    """
        Category model

        @name: name of the category
    """
    name = models.CharField(max_length=200)

    class Meta:
        # order by name
        ordering = ['name']
        # name of the object in plural
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


'---------------------------Model actor----------------------------'


class Actor(models.Model):
    """
        Actor model

        @author: the user that create the actor.

        @first_name: first name of the actor.

        @last_name: last name of the actor.

        @birthdate: birth date of the actor.

        @sex: gender of the actor.

        @nationality: nationality of the actor.

        @image: image of the actor.

        @if_alive: the actor is alive or not.

        @award: award related to actor.

        @comments: comments related to the actor
    """
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    sex_choices = [
        (MALE, MALE.capitalize()),
        (FEMALE, FEMALE.capitalize()),
        (OTHER, OTHER.capitalize()),
    ]
    nationalities_choices = (('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'), ('American', 'American'), ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), ('Antiguans', 'Antiguans'), ('Argentinean', 'Argentinean'), ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Azerbaijani', 'Azerbaijani'), ('Bahamian', 'Bahamian'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'), ('Barbadian', 'Barbadian'), ('Barbudans', 'Barbudans'), ('Batswana', 'Batswana'), ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'), ('Beninese', 'Beninese'), ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'), ('British', 'British'), ('Bruneian', 'Bruneian'), ('Bulgarian', 'Bulgarian'), ('Burkinabe', 'Burkinabe'), ('Burmese', 'Burmese'), ('Burundian', 'Burundian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Cape Verdean', 'Cape Verdean'), ('Central African', 'Central African'), ('Chadian', 'Chadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Comoran', 'Comoran'), ('Congolese', 'Congolese'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'), ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Djibouti', 'Djibouti'), ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), ('Dutchman', 'Dutchman'), ('Dutchwoman', 'Dutchwoman'), ('East Timorese', 'East Timorese'), ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'), ('Emirian', 'Emirian'), ('Equatorial Guinean', 'Equatorial Guinean'), ('Eritrean', 'Eritrean'), ('Estonian', 'Estonian'), ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), ('Filipino', 'Filipino'), ('Finnish', 'Finnish'), ('French', 'French'), ('Gabonese', 'Gabonese'), ('Gambian', 'Gambian'), ('Georgian', 'Georgian'), ('German', 'German'), ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), ('Grenadian', 'Grenadian'), ('Guatemalan', 'Guatemalan'), ('Guinea-Bissauan', 'Guinea-Bissauan'), ('Guinean', 'Guinean'), ('Guyanese', 'Guyanese'), ('Haitian', 'Haitian'), ('Herzegovinian', 'Herzegovinian'), ('Honduran', 'Honduran'), ('Hungarian', 'Hungarian'), ('I-Kiribati', 'I-Kiribati'), ('Icelander', 'Icelander'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Ivorian', 'Ivorian'), ('Jamaican', 'Jamaican'), ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'), ('Kenyan', 'Kenyan'), ('Kittian and Nevisian', 'Kittian and Nevisian'), ('Kuwaiti', 'Kuwaiti'), ('Kyrgyz', 'Kyrgyz'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'), ('Liberian', 'Liberian'), ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), ('Lithuanian', 'Lithuanian'), ('Luxembourger', 'Luxembourger'), ('Macedonian', 'Macedonian'), ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'), ('Maldivan', 'Maldivan'), ('Malian', 'Malian'), ('Maltese', 'Maltese'), ('Marshallese', 'Marshallese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'), ('Mexican', 'Mexican'), ('Micronesian', 'Micronesian'), ('Moldovan', 'Moldovan'), ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), ('Mosotho', 'Mosotho'), ('Motswana', 'Motswana'), ('Mozambican', 'Mozambican'), ('Namibian', 'Namibian'), ('Nauruan', 'Nauruan'), ('Nepalese', 'Nepalese'), ('Netherlander', 'Netherlander'), ('New Zealander', 'New Zealander'), ('Ni-Vanuatu', 'Ni-Vanuatu'), ('Nicaraguan', 'Nicaraguan'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'), ('North Korean', 'North Korean'), ('Northern Irish', 'Northern Irish'), ('Norwegian', 'Norwegian'), ('Omani', 'Omani'), ('Pakistani', 'Pakistani'), ('Palauan', 'Palauan'), ('Panamanian', 'Panamanian'), ('Papua New Guinean', 'Papua New Guinean'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Rwandan', 'Rwandan'), ('Saint Lucian', 'Saint Lucian'), ('Salvadoran', 'Salvadoran'), ('Samoan', 'Samoan'), ('San Marinese', 'San Marinese'), ('Sao Tomean', 'Sao Tomean'), ('Saudi', 'Saudi'), ('Scottish', 'Scottish'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'), ('Seychellois', 'Seychellois'), ('Sierra Leonean', 'Sierra Leonean'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('Slovenian', 'Slovenian'), ('Solomon Islander', 'Solomon Islander'), ('Somali', 'Somali'), ('South African', 'South African'), ('South Korean', 'South Korean'), ('Spanish', 'Spanish'), ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Surinamer', 'Surinamer'), ('Swazi', 'Swazi'), ('Swedish', 'Swedish'), ('Swiss', 'Swiss'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('Tajik', 'Tajik'), ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Togolese', 'Togolese'), ('Tongan', 'Tongan'), ('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'), ('Tuvaluan', 'Tuvaluan'), ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Uruguayan', 'Uruguayan'), ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'), ('Welsh', 'Welsh'), ('Yemenite', 'Yemenite'), ('Zambian', 'Zambian'), ('Zimbabwean', 'Zimbabwean'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    birthdate = models.DateField(blank=False)
    sex = models.CharField(max_length=6, blank=False, choices=sex_choices)
    nationality = models.CharField(
        max_length=50,
        choices=nationalities_choices,
        blank=False
    )
    image = models.ImageField(upload_to='media/actors/', blank=True)
    is_alive = models.BooleanField(default=True)
    award = GenericRelation(Award)
    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_fields(self):
        """ Return all key and value of all the field in award """
        return [(field.name, field.value_to_string(self))
                for field in Actor._meta.fields]

    def get_name(self):
        """ Get actor's full name """
        return self.first_name + ' ' + self.last_name


'------------------Model movie-----------------------------'


class Movie(models.Model):
    """
        Movie model

        @author: user created the movie.

        @title: name of the movie.

        @description: the description about the movie.

        @release_date: the release date of the movie.

        @category: the categories the movie belongs to.

        @image: movie poster.

        @actors: actors and actresses in the movie.

        @award: award related to the movie.

        @comments: comments related to the movie.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    release_date = models.DateField(blank=False)
    category = models.ManyToManyField(
        Category,
        blank=False
    )
    image = models.ImageField(upload_to='media/movies/', blank=True)
    actors = models.ManyToManyField(
        Actor,
        blank=True,
    )
    award = GenericRelation(Award)
    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_fields(self):
        """ Return all key and value of all the field in award """
        return [(field.name, field.value_to_string(self))
                for field in Movie._meta.fields]
