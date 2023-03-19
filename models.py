

#Database model. Inherits from the model class and has a foreign key to the USER model

class User(model.Model)
    User_Id=models.PrimaryKey(on_delete=models.CASCADE)
    firstname=models.TextField(max_length=200)
    lastname=models.TextField(max_length=200)
    email=models.TextField(max_length=200)
    password=models.TextField(max_length=200)
    is_active=models.IntegerField(blank=False)
    is_staff=models.IntegerField(blank=False)
 




class Twitter_User_Idddz(models.Model):
    User_Id=models.ForeignKey(User,on_delete=models.CASCADE)
    Tweet=models.TextField(max_length=200)
    Subject_Field=models.TextField(max_length=50,blank=True)
    Date_Time=models.DateTimeField(auto_now=True)
    Noun=models.IntegerField(blank=True)
    Pronoun=models.IntegerField(blank=True)
    Auxilary_Verbs=models.IntegerField(blank=True)
    Verb=models.IntegerField(blank=True)
    Adjective=models.IntegerField(blank=True)
    Sentiment_Score=models.IntegerField(blank=True)
    Customer_Score=models.IntegerField(blank=True)  # This is for the clustering
    Username_Username=models.CharField(max_length=50)
