from django.contrib.auth.base_user import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, photo, name, role, password="12345678"):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.username = email
        user.name = name
        user.photo = photo
        user.role = role
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password, name="superuser", role=1, photo=None)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user
