from django.test import TestCase
from .models import Project,Profile


# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.project= Project(id=1,title="shopping app",description="a nice app  for  shopping",link="shopping.herokapps.com")
        self.project.save_project()
    
    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = Project.objects.all()
        self.assertTrue(len(project)==0)

    def test_update_project(self):
        self.project.delete_project()
        project = Project.objects.all()
        self.assertFalse(len(project)>0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(name= "Alicia",bio="dev in the making",email="dev101@gmail.com",)
        self.profile.save_profile()
    
    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


    def test_delete_profile(self):
        self.profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)==0)

    def test_update_profile(self):
        self.profile.update_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)==1)